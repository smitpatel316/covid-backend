from app.models.record import Record


class Data(object):
    def __init__(self, name):
        self.name = name
        self.records: [Record] = []

    def add_record(self, record: Record):
        self.records.append(record)

    def total_cases(self) -> int:
        return self.records[-1].get_confirmed_cases()

    def active_cases(self) -> int:
        return (
            self.records[-1].get_confirmed_cases()
            - self.records[-1].get_deaths()
            - self.records[-1].get_recovered()
        )

    def get_records(self):
        return self.records

    def __str__(self):
        return "\n".join([str(record) for record in self.records])

    def to_dict(self):
        return {
            "name": self.name,
            "records": [record.__dict__ for record in self.records],
        }
