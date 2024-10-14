immutable_var = (1, True, "осень")
print(immutable_var)
# immutable_var [0] = 2 - Кортеж не имеет свойства изменяться, в отличие от списка []
mutable_list = [1, True, "осень"]
mutable_list[0] = 3
mutable_list[1] = False
mutable_list[2] = 'лето'
mutable_list.extend([1, 'зима'])
print(mutable_list)
