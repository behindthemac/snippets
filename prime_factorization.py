from sieve_of_eratosthenes import sieve_of_eratosthenes


def prime_factorization(n):
    """Get the prime factorization of an integer.

    Argument:
    n -- integer

    Return:
    factors: prime factorization of the integer
    """
    prime_numbers = sieve_of_eratosthenes(n)

    factors = {prime_number: 0 for prime_number in prime_numbers}

    i = 0
    while n > 1:
        prime_number = prime_numbers[i]

        while n % prime_number == 0:
            factors[prime_number] += 1
            n //= prime_number

        i += 1

    return {prime_number: count for prime_number, count in factors.items() if count > 0}
