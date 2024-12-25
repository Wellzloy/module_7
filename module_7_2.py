def custom_write(file_name, strings):
    file_tell = []
    file_num = []
    file_line = []
    file = open(file_name, 'a', encoding='utf-8')
    for info_single in info:
        file_tell.append(file.tell())
        file.write(f'{info_single}\n')
    file.close()
    with open(file_name, 'r', encoding='utf-8') as file:
        for num, line in enumerate(file, start=1):
            file_num.append(num)
            file_line.append(line.strip())
    strings_positions = {
        (num, pos): line
        for num, pos, line in zip(file_num, file_tell, file_line)
    }
    return strings_positions


info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
