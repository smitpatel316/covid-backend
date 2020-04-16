from app.models.data import Data
from app.models.record import Record
import csv
from requests import get

URL = "https://health-infobase.canada.ca/src/data/covidLive/covid19.csv"


def data_by_name(name="Canada") -> Data:
    response = get(url=URL)
    records = list(csv.reader(response.content.decode("utf-8").splitlines(), delimiter=","))
    data = Data(name)
    for record in records:
        if record[1] == name:
            data.add_record(
                Record(
                    date=record[3],
                    confirmed_cases=record[4],
                    probable_cases=record[5],
                    deaths=record[6],
                    tested=record[7],
                    recoveries=record[8],
                )
            )
    return data
