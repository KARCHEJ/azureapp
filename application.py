from flask import Flask
import os
from flask import Response
from flask import request
import json
app = Flask(__name__)

@app.route("/",methods = ['POST', 'GET'])
#@app.after_request
def hello():
    req_data = request.get_json()
    head = (os.environ["test"])
    url = (os.environ["apim_url"])
    response = Response()
    response.headers["Ocp-Apim-Subscription-Key"] = head
    response.data = json.dumps(req_data)
    postResponse = request.post(url,data = response.data,header = response.headers)
    return response
