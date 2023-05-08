import factorization
import pytest


def test_prime_factors():
    assert factorization.prime_factors(3958159172) == [2, 2, 11, 2347, 38329]
    assert factorization.prime_factors(3958159172.0) == [2, 2, 11, 2347, 38329]
    assert factorization.prime_factors('3958159172') == [2, 2, 11, 2347, 38329]

    with pytest.raises(ValueError):
        assert factorization.prime_factors('test')

    with pytest.raises(TypeError):
        assert factorization.prime_factors([1, 2, 3])
