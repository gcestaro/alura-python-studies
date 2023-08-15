from unit_tests.main.employee import Employee


class TestClass:

    def test_when_age_05_10_2000_should_return_23(self):
        # Given (context)
        input = "05/10/2000"
        expected = 23
        test_employee = Employee("Test", input, 1000)

        # When (action)
        result = test_employee.age()

        # Then (conclusion)
        assert result == expected
