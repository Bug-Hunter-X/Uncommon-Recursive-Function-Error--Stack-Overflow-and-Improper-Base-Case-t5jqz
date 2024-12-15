def function_with_uncommon_error_solution(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return 1  # Fixed base case
    else:
        return n / function_with_uncommon_error_solution(n-1) 