def summ_all(list_):
    counter = 0

    def rec_summ(element):
        nonlocal counter
        if isinstance(element, int):
            counter += element
        elif isinstance(element, str):
            counter += len(element)
        elif isinstance(element, (tuple, list, set)):
            for sub_element in element:
                rec_summ(sub_element)
        elif isinstance(element, dict):
            for key, value in element.items():
                rec_summ(key)
                rec_summ(value)

    rec_summ(list_)
    return counter


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), 'Hello',
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
print(summ_all(data_structure))
