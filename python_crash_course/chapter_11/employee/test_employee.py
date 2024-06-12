from c11_employee_class import Employee
import pytest

@pytest.fixture
def employee():
    employee = Employee("Harry", "Potter", 100000)
    return employee

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 105000

def test_give_custom_raise(employee):
    employee.give_raise(7500)
    assert employee.salary == 107500
    