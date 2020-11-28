def input_is_integer():
    keyboard_input = input('Input: ')
    try:
        n =  int(keyboard_input)
        return n
    except ValueError:
        return 'input not integer'