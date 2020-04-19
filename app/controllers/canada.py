import json

from flask import Blueprint

from app.services import canada as service

canada = Blueprint("canada", __name__, url_prefix="/canada")


@canada.route("/")
def canada_data():
    return json.dumps(service.all_data().to_dict())


@canada.route("/cases/total")
def canada_total():
    return str(service.total_cases())


@canada.route("/cases/active")
def canada_total_active():
    return str(service.active_cases())


@canada.route("/daily/active")
def canada_daily_active():
    return json.dumps(service.daily_active_cases())


@canada.route("/daily/cases")
def canada_daily_cases():
    return json.dumps(service.daily_cases())


@canada.route("/daily/rate")
def canada_daily_rate():
    return json.dumps(service.daily_rate_change())


@canada.route("/daily/total")
def canada_daily_total():
    return json.dumps(service.daily_total_cases())


@canada.route("/info")
def canada_info():
    return json.dumps(service.info())
