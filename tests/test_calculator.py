"""Tests for the calculator module."""

import pytest
from calculator import Calculator


def test_add():
    """Test addition."""
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(0, 0) == 0


def test_subtract():
    """Test subtraction."""
    assert Calculator.subtract(5, 3) == 2
    assert Calculator.subtract(0, 5) == -5
    assert Calculator.subtract(10, 10) == 0


def test_multiply():
    """Test multiplication."""
    assert Calculator.multiply(3, 4) == 12
    assert Calculator.multiply(-2, 3) == -6
    assert Calculator.multiply(0, 100) == 0


def test_divide():
    """Test division."""
    assert Calculator.divide(10, 2) == 5
    assert Calculator.divide(9, 3) == 3
    assert Calculator.divide(7, 2) == 3.5


def test_divide_by_zero():
    """Test division by zero raises error."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(10, 0)


def test_power():
    """Test exponentiation."""
    assert Calculator.power(2, 3) == 8
    assert Calculator.power(5, 2) == 25
    assert Calculator.power(10, 0) == 1
