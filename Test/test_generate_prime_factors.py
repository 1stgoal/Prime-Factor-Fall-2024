import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from prime import generate_prime_factors


def test_string():
    with pytest.raises(ValueError):
        generate_prime_factors("f")


def test_floatinput():
    with pytest.raises(ValueError):
        generate_prime_factors(.5)
