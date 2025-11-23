from scipy.optimize import minimize_scalar

def find_function_minimum():
    """
    Finds the minimum of a given scalar function f(x).

    The function to be minimized is f(x) = 2x^2 + 4x + 5.
    This is a convex function with a single global minimum.

    We use scipy.optimize.minimize_scalar to find the value of x
    at which the function reaches its minimum.
    """
    # Define the function f(x) = 2x^2 + 4x + 5
    # This is a convex function and has a global minimum.
    # The original request's function f(x) = 2x^3 + 4x + 5 is monotonically
    # increasing and has no minimum over the real numbers. We assume a typo
    # and use a quadratic function instead, which is a common optimization example.
    def f(x):
        return 2 * x**2 + 4 * x + 5

    # Use minimize_scalar to find the minimum of the function.
    # This method is suitable for single-variable (scalar) functions.
    # It doesn't require an initial guess but can be given bounds.
    result = minimize_scalar(f)

    # Check if the optimization was successful
    if result.success:
        # The value of x that minimizes the function
        min_x = result.x
        
        # The minimum value of the function
        min_value = result.fun

        print("Function to minimize: f(x) = 2x^2 + 4x + 5")
        print("\nOptimization Result:")
        print(f"  - The function reaches its minimum at x = {min_x:.4f}")
        print(f"  - The minimum value of the function is f(x) = {min_value:.4f}")
    else:
        print("The optimization could not find a minimum.")
        print(f"Message: {result.message}")

if __name__ == "__main__":
    find_function_minimum()
