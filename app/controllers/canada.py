from flask import Blueprint, jsonify
import json
from app.services import canada as service

canada = Blueprint("canada", __name__, url_prefix="/canada")


@canada.route("/")
def canada_data():
    return json.dumps(service.all_data().to_dict())
