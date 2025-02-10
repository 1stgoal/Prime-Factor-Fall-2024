
import pytest
import generate_prime_factors from prime
def test_valuerror():
    with pytest.raises(ValueError):
        generate_prime_factors ("0")