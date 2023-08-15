from employee import Employee


def test_age():
    test = Employee("Test", "05/10/2002", 1000)
    print(f"Test = {test.age()}")


test_age()
