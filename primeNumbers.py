def isPrime(number, primeArray):
    for prime in primeArray:
        if prime != 1 and number != prime and (number % prime == 0):
            return False
    return True

def collectPrimes():
    primeArray = []
    for i in range(1,251):
        if isPrime(i, primeArray):
            primeArray.append(i)
    print("Prime numbers collected: {}".format(primeArray))


if __name__ == '__main__':
    collectPrimes()