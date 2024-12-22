def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    for info_single in info:
        file.write(f'{info_single}\n')
    file.close()

info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)




# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
# а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.