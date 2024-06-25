def get_multiplied_digits(number):
    str_number = str(number)
    while str_number and str_number[0] == '0':
        str_number = str_number[1:]
    if not str_number:
        return 1
    if len(str_number) == 1:
        return int(str_number)
    first = int(str_number[0])
    return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits('0040203')
print(result)
