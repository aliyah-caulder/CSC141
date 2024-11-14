import pytest
from employee import Employee

@pytest.fixture
def my_employee():
    """An employee that will be available to test all functions."""
    my_employee = Employee('John', 'Smith', 5000)
    return my_employee

def test_give_default_raise(my_employee):
    """Test that the default raise can be given."""
    my_employee.give_raise()
    assert my_employee.salary == 10_000

def test_give_custom_raise(my_employee):
    """Test that a custom raise can be given"""
    my_employee.give_raise(2000)
    assert my_employee.salary == 7000