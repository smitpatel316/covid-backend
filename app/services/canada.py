from app.utils import utils


def all_data():
    return utils.data_by_name("Canada")


def total_cases():
    return utils.total_cases("Canada")


def daily_cases():
    return utils.daily_cases("Canada")


def daily_rate_change():
    return utils.daily_rate_of_change("Canada")


def active_cases():
    return utils.active_cases("Canada")


def daily_active_cases():
    return utils.daily_active_cases("Canada")