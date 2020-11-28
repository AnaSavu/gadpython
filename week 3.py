from my_package_week_3 import *

if __name__ == '__main__':
    print('sum for: 1, 5, -3, \"abc", [12, 56, \"cad"]: ', end='')
    print(sum_of_int_float_numbers(1, 5, -3, 'abc', [12, 56, 'cad']))
    print('sum for: ', end='')
    print(sum_of_int_float_numbers())
    print('sum for: 2, 4, \"abc", param_1=2: ', end='')
    print(sum_of_int_float_numbers(2, 4, 'abc', param_1=2))

    n = input_is_integer()
    while n == 'input not integer':
        print(n)
        n = input_is_integer()

    print('sum of all numbers: ', sum_all_numbers(n))
    print('sum of all even numbers: ', sum_even_numbers(n))
    print('sum of all odd numbers: ', end='')
    try:
        print(sum_odd_numbers(n))
    except ValueError as ve:
        print(ve)
