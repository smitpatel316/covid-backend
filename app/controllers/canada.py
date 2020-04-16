from flask import Blueprint, jsonify
import json
from app.services import canada as service

canada = Blueprint("canada", __name__, url_prefix="/canada")


@canada.route("/")
def canada_data():
    return json.dumps(service.all_data().to_dict())


@canada.route("/cases/total")
def canada_total():
    return str(service.total_cases())


@canada.route("/cases/active")
def canada_daily_active():
    return str(service.active_cases())


@canada.route("/daily/cases")
def canada_daily_cases():
    return json.dumps(service.daily_cases())


@canada.route("/daily/rate")
def canada_daily_rate():
    return json.dumps(service.daily_rate_change())