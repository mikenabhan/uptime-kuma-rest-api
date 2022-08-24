#!/usr/bin/env python3
import json
import random
import os
from flask import Flask, request
from uptime_kuma_api import UptimeKumaApi, MonitorType
from markupsafe import escape

UPTIME_KUMA_URL = os.getenv('UPTIME_KUMA_URL')
UPTIME_KUMA_USER = os.getenv('UPTIME_KUMA_USER')
UPTIME_KUMA_PASSWORD = os.getenv('UPTIME_KUMA_PASSWORD')

api = UptimeKumaApi(UPTIME_KUMA_URL)
api.login(UPTIME_KUMA_USER, UPTIME_KUMA_PASSWORD)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello.'

@app.route('/ping')
def hello():
    return 'Pong.'

@app.route('/add/http', methods=['POST'])
def add_http():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        # return json
        monitor_name=json['name']
        monitor_url=json['url']
        result = api.add_monitor(type=MonitorType.HTTP, name=monitor_name, url=monitor_url)
        # return json['url']
        return result
    else:
        return 'Content-Type not supported!'