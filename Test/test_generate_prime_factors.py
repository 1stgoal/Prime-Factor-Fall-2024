import pytest
import sys
import os

# Letting the test program know where the program being tested is located (path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from prime import generate_prime_factors


# Testing the string input.
def test_string():
    with pytest.raises(ValueError):
        generate_prime_factors("f")


# Testing the float input.
def test_float_input():
    with pytest.raises(ValueError):
        generate_prime_factors(.5)


# Testing when input is 1.
def test_input_one():
    assert generate_prime_factors(1) == []


# Testing when input is 2.
def test_input_two():
    assert generate_prime_factors(2) == [2]


# Testing when input is 3.
def test_input_three():
    assert generate_prime_factors(3) == [3]


# Testing when input is 4.
def test_input_four():
    assert generate_prime_factors(4) == [2, 2]


# Testing when input is 6.
def test_input_six():
    assert generate_prime_factors(6) == [2, 3]


# Testing when input is 8.
def test_input_eight():
    assert generate_prime_factors(8) == [2, 2, 2]


# Testing when input is 9.
def test_input_nine():
    assert generate_prime_factors(9) == [3, 3]


