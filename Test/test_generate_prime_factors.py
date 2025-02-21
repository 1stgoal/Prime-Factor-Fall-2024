import pytest
from prime import generate_prime_factors


def test_string():
    with pytest.raises(ValueError):
        generate_prime_factors("f")


def test_floatinput():
    with pytest.raises(ValueError):
        generate_prime_factors(.5)
