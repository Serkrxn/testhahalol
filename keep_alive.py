from flask import Flask, request
from os import environ
from math import floor
from threading import Thread
from json import load,dumps
from time import time

app = Flask('')

@app.route('/')
def main():
    return "Bot awaken"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()