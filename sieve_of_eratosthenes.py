def sieve_of_eratosthenes(n):
    """Get all prime numbers up to any given limit.

    Argument:
    n -- limit of prime numbers

    Return:
    all prime numbers up to the given limit
    """
    is_prime = {i: True for i in range(2, n + 1)}

    for number in is_prime.keys():
        if number ** 2 > n:
            break

        if is_prime[number]:
            composite_number = number * 2
            while True:
                is_prime[composite_number] = False
                composite_number += number
                if composite_number > n:
                    break

    return [i for i in range(2, n + 1) if is_prime[i]]
