"""Recursive and iterative versions of a factorial function.

Provides two implementations: recursive and iterative.
Run with: `python "task-4.py" <number>`
"""

from __future__ import annotations

import sys


def factorial_recursive(n: int) -> int:
    """Return n! using recursion.

    Args:
        n: Non-negative integer.

    Returns:
        Factorial of n.

    Raises:
        ValueError: if n < 0.
        RecursionError: if n is very large (stack overflow).
    """
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """Return n! using iteration (loop).

    Args:
        n: Non-negative integer.

    Returns:
        Factorial of n.

    Raises:
        ValueError: if n < 0.
    """
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main(argv=None) -> int:
    """Run factorial calculator from command line.

    Usage examples:
      python "task-4.py" 5
      python "task-4.py" 100

    Returns exit code 0 on success, 2 on error.
    """
    import argparse

    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(description="Calculate factorial using recursive and iterative methods.")
    parser.add_argument("number", help="Non-negative integer", type=int)
    args = parser.parse_args(argv)
    
    n = args.number

    try:
        rec_result = factorial_recursive(n)
    except (ValueError, RecursionError) as e:
        print(f"Recursive error: {e}")
        rec_result = None

    try:
        iter_result = factorial_iterative(n)
    except ValueError as e:
        print(f"Iterative error: {e}")
        iter_result = None

    if rec_result is not None:
        print(f"{n}! (recursive) = {rec_result}")
    if iter_result is not None:
        print(f"{n}! (iterative) = {iter_result}")

    if rec_result is None or iter_result is None:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
    