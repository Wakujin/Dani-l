values_list = [3, 'play', False]
values_dict = {'a': 1, 'b': 'trap', 'c': True}
values_list2 = ['cow', True]


def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(1,4)
print_params(False,1,'проверка')
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2, 42)
