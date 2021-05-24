import requests 
import os
from datetime import datetime
from resdis import redis_connect

# client= redis_connect()
api_key = os.environ.get('API_KEY')

cities = ['Santiago', 'Zurich', 'Auckland', 'Sydney', 'Londres', 'Georgia'] 


def get_coords(client):

    for city in cities:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        )
        r = r.json()
        client.set(f'{city}-lat', r['coord']['lat'])
        client.set(f'{city}-lon', r['coord']['lon'])

    return None


def get_weather(client):

    response = {}

    for city in cities:

        lat = client.get(f'{city}-lat').decode('utf-8')
        lon = client.get(f'{city}-lon').decode('utf-8')
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
        )
        r = r.json()
        time = datetime.fromtimestamp(
            r["dt"] + r["timezone"]).time().strftime("%H:%M:%S")
        response[city] = {
            'temp': r["main"]["temp"],
            'time': time
        }

    return response 
    

def store_error(client):
    ts = datetime.now().timestamp()
    client.set(ts , 'Error trying to get cities info ! ')