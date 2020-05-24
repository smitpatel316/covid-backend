class Record(object):
    def __init__(
        self,
        date,
        confirmed_cases,
        probable_cases,
        deaths,
        tested,
        recoveries,
        recovery_percentage=None,
        testing_rate=None,
        new_cases_today=None,
        percentage_today=None,
    ):
        self.date = date
        if confirmed_cases in ["", "N/A"]:
            confirmed_cases = 0
        if probable_cases in ["", "N/A"]:
            probable_cases = 0
        if deaths in ["", "N/A"]:
            deaths = 0
        if tested in ["", "N/A"]:
            tested = 0
        if recoveries in ["", "N/A"]:
            recoveries = 0
        self.confirmed_cases = int(confirmed_cases)
        self.probable_cases = int(probable_cases)
        self.deaths = int(deaths)
        self.tested = int(tested)
        self.recoveries = int(recoveries)
        # Optionals, data not showing up recently from gov
        self.recovery_percentage = recovery_percentage
        self.testing_rate = testing_rate
        self.new_cases_today = new_cases_today
        self.percentage_today = percentage_today

    def get_confirmed_cases(self):
        return self.confirmed_cases

    def get_date(self):
        return self.date

    def get_deaths(self):
        return self.deaths

    def get_recovered(self):
        return self.recoveries

    def get_tests(self):
        return self.tested

    def get_active_cases(self):
        return self.get_confirmed_cases() - self.get_deaths() - self.get_recovered()


def __str__(self):
    return (
        f"Date: {self.date}, Confirmed Cases: {self.confirmed_cases}, Probable Cases: {self.probable_cases},"
        f" Deaths: {self.deaths}, Tested: {self.tested}, Recoveries: {self.recoveries}"
    )
