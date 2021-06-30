from flask import Flask
import os
from flask import Response
from flask import request
import requests
import json
app = Flask(__name__)

@app.route("/",methods = ['POST', 'GET'])
#@app.after_request
def handleRequest():
    req_data = request.get_json()
    head = (os.environ["apim_token"])
    url = (os.environ["apim_url"])
    botResponse = Response(status = 200)
    headers = {"Ocp-Apim-Subscription-Key" : head, "Content-Type" : "application/json" }
    postResponse = requests.post(url, data = json.dumps(req_data), headers = headers)
    return botResponse
