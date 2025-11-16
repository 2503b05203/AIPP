def is_prime_simple(n: int) -> bool:
    """
    Return True if n is prime, False otherwise.
    This is a simple implementation for demonstration purposes.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    print("Simple Prime Checker. Enter integers to test; type 'q' or press Enter on an empty line to quit.")
    while True:
        s = input("Enter an integer (or 'q' to quit): ").strip()
        if s == "" or s.lower() in ("q", "quit", "exit"):
            print("Goodbye.")
            break
        try:
            n = int(s)
        except ValueError:
            print("Invalid input — please enter a valid integer.")
            continue
        if is_prime_simple(n):
            print(f"{n} is prime.")
        else:
            print(f"{n} is composite.")
