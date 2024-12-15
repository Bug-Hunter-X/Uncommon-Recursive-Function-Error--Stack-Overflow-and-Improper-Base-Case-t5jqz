def function_with_uncommon_error(n):
    if n == 0:
        return 0  # This will cause an error if n is negative
    else:
        return n / function_with_uncommon_error(n-1)