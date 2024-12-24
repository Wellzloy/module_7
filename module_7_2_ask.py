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

example_str = ('Text for tell.\n')
print(type(example_str))
result_str = example_str.replace("\n ", "")
print(result_str)

l = ['Name1\n', '7.3', '6.9\n', '6.6', '6.6', '6.1', '6.4', '7.3\n']
print(list(map(str.strip,file_line)))