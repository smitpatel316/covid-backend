from app.utils import utils


def regions():
    return utils.available_regions()


def all_data(name):
    return utils.data_by_name(name)


def total_cases(name):
    return utils.total_cases(name)


def daily_cases(name):
    return utils.daily_cases(name)


def daily_rate_change(name):
    return utils.daily_rate_of_change(name)


def active_cases(name):
    return utils.active_cases(name)


def daily_active_cases(name):
    return utils.daily_active_cases(name)


def daily_total_cases(name):
    return utils.daily_total_cases(name)


def info(name):
    return utils.info(name)


def daily_recoveries(name):
    return utils.daily_recoveries(name)


def daily_tests(name):
    return utils.daily_tests(name)