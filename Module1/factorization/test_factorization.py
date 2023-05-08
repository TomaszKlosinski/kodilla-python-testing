import factorization

def test_prime_factors() -> list[int]:
    assert factorization.prime_factors(3958159172) == [2, 2, 11, 2347, 38329]
