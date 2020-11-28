def sum_all_numbers(n):
    if n == 0:
        return 0
    return n + sum_all_numbers(n-1)

def sum_even_numbers(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + sum_even_numbers(n-1)
    return sum_even_numbers(n-1)

def sum_odd_numbers(n):
    if n == 0:
        raise ValueError('0 is not an odd number')
    if n == 1:
        return 1
    if n % 2 == 1:
        return n + sum_odd_numbers(n-1)
    return sum_odd_numbers(n-1)