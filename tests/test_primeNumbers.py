import pytest
from src.primeNumbers import isPrime, collectPrimes


def test_isPrime():
    assert isPrime(1, []) is True
    assert isPrime(2, [1]) is True
    assert isPrime(3, [1,2]) is True
    assert isPrime(4, [1,2,3]) is False
    assert isPrime(5, [1,2,3]) is True
    assert isPrime(6, [1,2,3,5]) is False

def test_collectPrimes():
    assert collectPrimes() is 54 ##Total of prime numbers from 1 to 250