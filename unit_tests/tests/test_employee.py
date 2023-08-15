import sys

import pytest
from pytest import mark

from unit_tests.main.employee import Employee

TEST_EMPLOYEE_NAME = "Unit Test"
TEST_EMPLOYEE_DATE_OF_BIRTH = "05/10/2000"

"""
    More on markers: https://docs.pytest.org/en/7.1.x/how-to/mark.html#mark
"""


class TestClass:

    # @pytest.fixture(scope='package')
    # @pytest.fixture(scope='session')
    # @pytest.fixture(scope='module')
    # @pytest.fixture(scope='class')
    # @pytest.fixture(scope='function') # default
    @pytest.fixture
    def employee(self):
        return Employee(TEST_EMPLOYEE_NAME, TEST_EMPLOYEE_DATE_OF_BIRTH, 1000)

    @pytest.fixture
    def director_employee(self):
        return Employee(TEST_EMPLOYEE_NAME + " Bragança", TEST_EMPLOYEE_DATE_OF_BIRTH, 100_000)

    @pytest.fixture
    def employee_without_bonus(self):
        return Employee(TEST_EMPLOYEE_NAME, TEST_EMPLOYEE_DATE_OF_BIRTH, 10_001)

    # Not needed, check .coverage on project's root folder
    # def test_str(self, employee):
    #     expected = "Employee: Unit Test, age: 23, salary: $1000"
    #     assert employee.__str__() == expected

    @mark.age
    def test_when_age_05_10_2000_should_return_23(self, employee):
        # Given (context)
        expected = 23

        # When (action)
        result = employee.age()

        # Then (conclusion)
        assert result == expected

    @mark.naming
    def test_when_name_unit_test_return_test(self, employee):
        expected = "Test"
        result = employee.lastname()
        assert result == expected

    @mark.naming
    def test_when_name_unit_test_return_test(self, employee):
        expected = "Unit Test"
        result = employee.name
        assert result == expected

    @mark.decrease_salary
    def test_when_decrease_salary_from_100k_return_90k(self, director_employee):
        expected = 90_000
        director_employee.decrease_salary()
        result = director_employee.salary
        assert result == expected

    @mark.bonus_calculation
    def test_when_salary_higher_than_10k_bonus_raise_exception(self, employee_without_bonus):
        with pytest.raises(ValueError):
            result = employee_without_bonus.calculate_bonus()
            assert result

    @mark.bonus_calculation
    def test_when_salary_lower_than_10k_bonus_10_percent(self, employee):
        expected = 100
        result = employee.calculate_bonus()
        assert result == expected

    @mark.skip(reason="Ignore this for now")
    def test_ignored(self):
        pass

    @mark.skipif(sys.version_info < (3, 10), reason="Python 3.10 or higher required")
    def test_ignored_if(self):
        pass

    @mark.xfail
    def test_should_fail(self):
        raise Exception("This will fail")
