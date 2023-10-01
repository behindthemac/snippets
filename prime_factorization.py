from sieve_of_eratosthenes import sieve_of_eratosthenes


def prime_factorization(n):
    """Returns all prime factors of an integer.

    Args:
        n: A positive integer

    Returns:
        All prime factors of the integer
    """
    prime_numbers = sieve_of_eratosthenes(n)

    factors = {prime_number: 0 for prime_number in prime_numbers}
    index = 0
    prime_number = prime_numbers[index]
    while True:
        if n % prime_number == 0:
            factors[prime_number] += 1
            n //= prime_number
            if n <= 1:
                break
        else:
            index += 1
            prime_number = prime_numbers[index]

    return {prime_number: count for prime_number, count in factors.items() if count > 0}
