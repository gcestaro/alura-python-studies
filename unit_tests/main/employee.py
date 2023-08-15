from datetime import date


class Employee:
    def __init__(self, name, date_of_birth, salary):
        self._name = name
        self._date_of_birth = date_of_birth
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    def age(self):
        year_of_birth = self._date_of_birth.split("/")[-1]
        return date.today().year - int(year_of_birth)
