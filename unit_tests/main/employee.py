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

    def lastname(self):
        return self._name.split(" ")[-1]

    def decrease_salary(self):
        if self.is_director() and self._salary >= 100_000:
            self._salary *= 0.9

    def is_director(self):
        directors_lastname = ["Bragança", "Windsor", "Bourbon",
                              "Yamato", "Al Saud", "Khan",
                              "Tudor", "Ptolomeu"]
        return self.lastname() in directors_lastname

    def calculate_bonus(self):
        limit_to_receive_bonus = self._salary * 0.1
        if limit_to_receive_bonus > 1000:
            raise ValueError(f"Bonus is not allowed for the salary {self.salary}")
        return limit_to_receive_bonus

    def __str__(self):
        return f"Employee: {self._name}, age: {self.age()}, salary: ${self._salary}"
