calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(),string.lower()


def is_contains(string, list_of_search):
    count_calls()
    return string.lower in (i.lower for i in list_of_search)


print(string_info('Voldemort'))
print(string_info('Potter Harry'))
print(string_info('Hag rid'))

print(is_contains('Theravada', ['Theravada', 'cruciform', 'imperil']))
print(is_contains('123', ['223', '1233','1233']))
print(calls)
