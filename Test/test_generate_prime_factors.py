
import pytest
from prime import generate_prime_factors



def test_valuerror():
    with pytest.raises(ValueError):
        generate_prime_factors(0)