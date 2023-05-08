import factorization

def test_prime_factors():
    assert factorization.prime_factors(3958159172) == [2, 2, 11, 2347, 38329]
    assert factorization.prime_factors(3958159172.0) == [2, 2, 11, 2347, 38329]
    assert factorization.prime_factors('3958159172') == [2, 2, 11, 2347, 38329]

    # ValueError
    assert factorization.prime_factors('test')
    assert factorization.prime_factors(1.24)

    # TypeError
    assert factorization.prime_factors([1, 2, 3])
