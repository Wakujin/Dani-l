def custom_write(file_name, strings):
    strings_positions = {}
    string_numb = 0
    file = open(file_name, 'w',encoding='utf-8')
    for i in strings:
        byte_position = file.tell()
        file.write(i+'\n')
        string_numb += 1
        strings_positions[(string_numb,byte_position)] = i
    file.close()
    return strings_positions



info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]

result = custom_write('test.txt', info)
for elem in result.items():

  print(elem)