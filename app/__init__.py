from flask import Flask
import os

from app.controllers.canada import canada

app = Flask(__name__)


@app.after_request
def after_request(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    header["Access-Control-Allow-Headers"] = "*"
    return response


app.register_blueprint(canada)