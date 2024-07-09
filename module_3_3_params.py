def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(1, 2, 3)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['Шанти', 146, False]
values_dict = {'a': 'cat', 'b': 3 < 2, 'c': 22}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [6 != 5, 'Дорогу освоит идущий']
print_params(*values_list_2, 42)
