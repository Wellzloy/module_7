def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    for info_single in info:
        file.write(f'{info_single}\n')
    file.close()

info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)




# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
# а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
users_tuple = ((("+111", "123455"), "Tom"), ("+384767557", "Bob"), ("+958758767", "Alice"))
users_dict = dict(users_tuple)
print(users_dict)

users_list = [["+111123455", "Tom"], ["+384767557", "Bob"], ["+958758767", "Alice"]]
users_dict = dict(users_list)
print(users_dict)

# Пример полученного словаря: {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}