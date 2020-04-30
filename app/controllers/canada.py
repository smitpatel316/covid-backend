import json

from flask import Blueprint

from app.services import canada as service

canada = Blueprint("canada", __name__, url_prefix="/api/v1")


@canada.route("/")
def regions():
    return json.dumps(service.regions())


@canada.route("/<name>")
def canada_data(name):
    return json.dumps(service.all_data(name).to_dict())


@canada.route("/<name>/cases/total")
def canada_total(name):
    return str(service.total_cases(name))


@canada.route("/<name>/cases/active")
def canada_total_active(name):
    return str(service.active_cases(name))


@canada.route("/<name>/daily/active")
def canada_daily_active(name):
    return json.dumps(service.daily_active_cases(name))


@canada.route("/<name>/daily/cases")
def canada_daily_cases(name):
    return json.dumps(service.daily_cases(name))


@canada.route("/<name>/daily/rate")
def canada_daily_rate(name):
    return json.dumps(service.daily_rate_change(name))


@canada.route("/<name>/daily/total")
def canada_daily_total(name):
    return json.dumps(service.daily_total_cases(name))


@canada.route("/<name>/info")
def canada_info(name):
    return json.dumps(service.info(name))
