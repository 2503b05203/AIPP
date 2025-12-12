#include <iostream>
#include <stdexcept>

/**
 * Calculates the factorial of a non-negative integer n using recursion.
 * 
 * @param n A non-negative integer.
 * @return The factorial of n.
 * @throws std::invalid_argument If n is negative.
 */
int factorial(int n) {
    // Check for invalid input
    if (n < 0) {
        throw std::invalid_argument("Factorial is not defined for negative numbers.");
    }

    // Base case: 0! = 1 and 1! = 1
    if (n == 0 || n == 1) {
        return 1;
    }

    // Recursive step: n! = n * (n-1)!
    return n * factorial(n - 1);
}

int main() {
    // Example usage
    try {
        int test_number;
        std::cout << "Enter a non-negative integer to compute its factorial: ";
        std::cin >> test_number;

        int result = factorial(test_number);
        std::cout << "The factorial of " << test_number << " is: " << result << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
    return 0;
}
