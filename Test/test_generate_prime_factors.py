import pytest
import sys
import os

# Letting the test program know where the program being tested is located (path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from prime import generate_prime_factors


# testing the string input
def test_string():
    with pytest.raises(ValueError):
        generate_prime_factors("f")


# testing the float input
def test_float_input():
    with pytest.raises(ValueError):
        generate_prime_factors(.5)


# testing when input is 1
def test_input_one():
    assert generate_prime_factors(1) == []
