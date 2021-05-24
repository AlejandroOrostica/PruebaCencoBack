from fastapi import FastAPI, WebSocket
from typing import Optional
from fastapi.responses import HTMLResponse


import requests
import os
import random
from locations import get_coords, get_weather, store_error

from resdis import redis_connect
import time

client = redis_connect()

app = FastAPI()

cities = ['Santiago', 'Zurich', 'Auckland', 'Sydney', 'Londres', 'Georgia']


get_coords(client)


@app.get("/get-weather")
def get_weathers():

    return get_weather(client)






@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    i = 1
    while True:
        prob = random.randint(0,10)
        print('prob: ', prob)
        if prob < 1:
            store_error(client)
            time.sleep(10)
        else:
            await websocket.send_json(get_weather(client))
            time.sleep(10)



# a = client.get('Santiago-lat').decode('utf-8')

# a = get_weather(client)

# print(a)
