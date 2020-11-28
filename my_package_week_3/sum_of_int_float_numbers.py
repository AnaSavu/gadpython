def sum_of_int_float_numbers(*args, **kwargs):
    sum = 0
    for parameter in args:
        if isinstance(parameter, int) or isinstance(parameter, float):
            sum += parameter
    return sum