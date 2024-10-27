values_list = [3, 'play', False]
values_dict = {'a': 1, 'b': 'trap', 'c': True}
values_list2 = ['cow', True]


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2, 42)
