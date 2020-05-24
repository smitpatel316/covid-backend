import csv

from requests import get

from app.models.data import Data
from app.models.record import Record

CANADA_HEALTH = "https://health-infobase.canada.ca/src/data/covidLive/covid19.csv"


def available_regions():
    response = get(url=CANADA_HEALTH)
    records = list(
        csv.reader(response.content.decode("utf-8").splitlines(), delimiter=",")
    )
    regions = []
    for record in reversed(records):
        if record[1] not in regions:
            regions.append(record[1])
        else:
            break
    return regions


def data_by_name(name="Canada") -> Data:
    response = get(url=CANADA_HEALTH)
    records = list(
        csv.reader(response.content.decode("utf-8").splitlines(), delimiter=",")
    )
    data = Data(name)
    prev_record = {}
    for (index, record) in enumerate(records):
        if record[1] == name:
            for (record_index, field) in enumerate(record):
                if field in ["", "N/A"]:
                    if index == 0:
                        record[record_index] = 0
                        prev_record.update({record_index: 0})
                    else:
                        if record_index not in prev_record:
                            prev_record.update({record_index: 0})
                        record[record_index] = prev_record[record_index]
                else:
                    prev_record.update({record_index: field})

            data.add_record(
                Record(
                    date=record[3],
                    confirmed_cases=record[4],
                    probable_cases=record[5],
                    deaths=record[6],
                    tested=record[8],
                    recoveries=record[9],
                )
            )
    return data


def total_cases(name="Canada"):
    data = data_by_name(name)
    return data.total_cases()


def daily_cases(name="Canada"):
    records: [Record] = data_by_name(name).get_records()
    date_to_cases = {}
    for (index, record) in enumerate(records):
        if index == 0:
            date_to_cases.update({record.get_date(): record.get_confirmed_cases()})
        else:
            date_to_cases.update(
                {
                    record.get_date(): record.get_confirmed_cases()
                    - records[index - 1].get_confirmed_cases()
                }
            )
    return date_to_cases


def daily_rate_of_change(name="Canada"):
    cases = daily_cases(name)
    rate_of_change = {}
    prev_case = None
    for (date, daily_case) in cases.items():
        if len(rate_of_change) == 0:
            rate_of_change.update({date: daily_case})
        else:
            rate_of_change.update({date: daily_case - prev_case})
        prev_case = daily_case
    return rate_of_change


def active_cases(name="Canada"):
    return data_by_name(name).active_cases()


def daily_active_cases(name="Canada"):
    return {
        record.get_date(): record.get_active_cases()
        for record in data_by_name(name).get_records()
    }


def daily_total_cases(name="Canada"):
    return {
        record.get_date(): record.get_confirmed_cases()
        for record in data_by_name(name).get_records()
    }


def info(name="Canada"):
    data = data_by_name(name)
    new_cases = data.new_total_cases()
    new_active = data.new_active_cases()
    new_recovered = data.new_recovered_cases()
    new_deaths = data.new_deaths()

    return [
        f"Confirmed: {data.total_cases()} ({'+' if new_cases > 0 else ''}{new_cases})",
        f"Active: {data.active_cases()} ({'+' if new_active > 0 else ''}{new_active})",
        f"Recovered: {data.recovered_cases()} ({'+' if new_recovered > 0 else ''}{new_recovered})",
        f"Deaths: {data.deaths()} ({'+' if new_deaths > 0 else ''}{new_deaths})",
    ]


def daily_recoveries(name="Canada"):
    records: [Record] = data_by_name(name).get_records()
    date_to_recoveries = {}
    for (index, record) in enumerate(records):
        if index == 0:
            date_to_recoveries.update({record.get_date(): record.get_recovered()})
        else:
            date_to_recoveries.update(
                {
                    record.get_date(): record.get_recovered()
                    - records[index - 1].get_recovered()
                }
            )
    return date_to_recoveries


def daily_tests(name="Canada"):
    records: [Record] = data_by_name(name).get_records()
    date_to_tests = {}
    for (index, record) in enumerate(records):
        if index == 0:
            date_to_tests.update({record.get_date(): record.get_tests()})
        else:
            date_to_tests.update(
                {record.get_date(): record.get_tests() - records[index - 1].get_tests()}
            )
    return date_to_tests
