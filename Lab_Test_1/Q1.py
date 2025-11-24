import math


def is_prime(n: int) -> bool:
    """
    Check whether the provided integer is prime.

    Args:
        n: Integer to test.

    Returns:
        True if n is prime, otherwise False.
    """
    if not isinstance(n, int):
        raise TypeError("is_prime expects an integer input")

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.isqrt(n))
    for candidate in range(3, limit + 1, 2):
        if n % candidate == 0:
            return False
    return True


test_cases = [
    (0, False, "Numbers less than 2 are not prime by definition."),
    (1, False, "1 is excluded from primes even though it has one divisor."),
    (2, True, "2 is the only even prime, validating the even-number edge case."),
    (13, True, "13 is a typical small odd prime to check general flow."),
    (25, True, "25 has an odd divisor (5), exercising composite detection."),
    (7919, True, "Large prime ensures the square-root loop handles bigger values."),
    (10000, False, "Even composite verifies quick elimination of multiples of 2."),
]


for value, expected, reason in test_cases:
    result = is_prime(value)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: is_prime({value}) == {result} | Expected: {expected} | {reason}")

