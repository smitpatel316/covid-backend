from app.models.record import Record


class Data(object):
    def __init__(self, name):
        self.name = name
        self.records: [Record] = []

    def add_record(self, record: Record):
        self.records.append(record)

    def __str__(self):
        return "\n".join([str(record) for record in self.records])

    def to_dict(self):
        return {
            "name": self.name,
            "records": [record.__dict__ for record in self.records],
        }
