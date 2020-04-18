from app.models.data import Data
from app.models.record import Record
import csv
from requests import get

CANADA_HEALTH = "https://health-infobase.canada.ca/src/data/covidLive/covid19.csv"
CORONA_NINJA = "https://corona.lmao.ninja/v2/countries/Canada"


def data_by_name(name="Canada") -> Data:
    response = get(url=CANADA_HEALTH)
    records = list(
        csv.reader(response.content.decode("utf-8").splitlines(), delimiter=",")
    )
    data = Data(name)
    for record in records:
        if record[1] == name:
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
