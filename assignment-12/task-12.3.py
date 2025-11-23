from scipy.optimize import linprog

def solve_chocolate_problem():
    """
    Solves the chocolate production linear optimization problem.

    The problem is to maximize the profit from producing two types of chocolates,
    A and B, subject to constraints on available milk and choco.

    Objective function to maximize: Profit = 6x + 5y
    (where x is units of A, y is units of B)

    Constraints:
    1. Milk: 1x + 1y <= 5
    2. Choco: 3x + 2y <= 12
    3. Non-negativity: x >= 0, y >= 0

    The `linprog` function solves minimization problems, so we minimize the
    negative of the profit function: -6x - 5y.
    """
    # Coefficients of the objective function to be minimized (-Profit)
    # c = [-profit_A, -profit_B]
    c = [-6, -5]

    # Coefficients of the inequality constraints (LHS)
    # A_ub = [[milk_A, milk_B], [choco_A, choco_B]]
    A_ub = [[1, 1], 
            [3, 2]]

    # Right-hand side of the inequality constraints (available resources)
    # b_ub = [total_milk, total_choco]
    b_ub = [5, 12]

    # Bounds for each variable (x and y must be non-negative)
    x_bounds = (0, None)  # Units of chocolate A
    y_bounds = (0, None)  # Units of chocolate B

    # Solve the linear programming problem
    result = linprog(c=c, A_ub=A_ub, b_ub=b_ub, bounds=[x_bounds, y_bounds], 
                     method='highs')

    # Check if the optimization was successful
    if result.success:
        # The optimal values for x and y
        optimal_A = result.x[0]
        optimal_B = result.x[1]
        
        # The maximum profit is the negative of the minimized objective function value
        max_profit = -result.fun

        print("Optimal Production Plan:")
        print(f"  - Units of Chocolate A: {optimal_A:.0f}")
        print(f"  - Units of Chocolate B: {optimal_B:.0f}")
        print(f"\nMaximum Profit: Rs {max_profit:.2f}")
    else:
        print("The optimization problem could not be solved.")
        print(f"Message: {result.message}")

if __name__ == "__main__":
    solve_chocolate_problem()
