class Date:
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year

    def print(self):
        print(f"{self.date}/{self.month}/{self.year}")
