def sieve_of_eratosthenes(n):
    """Returns all prime numbers up to a given limit.

    Args:
        n: The upper limit of prime numbers

    Returns:
        All prime numbers up to the given limit
    """
    is_prime = {i: True for i in range(2, n + 1)}

    prime_number = 2
    while prime_number ** 2 <= n:
        composite_number = prime_number * 2
        while True:
            is_prime[composite_number] = False
            composite_number += prime_number
            if composite_number > n:
                break

        while True:
            prime_number += 1
            if is_prime[prime_number]:
                break

    return [number for number, prime in is_prime.items() if prime]
