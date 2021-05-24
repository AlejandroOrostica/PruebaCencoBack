FROM python:3.7-alpine

# Setting environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip3 install --upgrade pip
RUN pip install -U --force-reinstall pip

# Installing dependencies
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt



# Setting Up directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app


# Adding and run as non-root user
RUN adduser -D user
USER user
