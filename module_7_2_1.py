file_tell = (0, 16, 66, 98)
file_num = (1, 2, 3, 4)
file_num_tell = ((1, 0), (2, 16), (3, 66), (4, 98))

file_line = ['Text for tell.\n', 'Используйте кодировку utf-8.\n', 'Because there are 2 languages!\n', 'Спасибо!\n']


# def sum_file(a, b):
#     return list(a, b)
# x = map(sum_file, ([1, 2, 3, 4], [0, 16, 66, 98]))
# print(list(x))

def myfunc(a, b):
    return (a, b)

x = map(myfunc, file_num_tell, file_line)
print(tuple(x))