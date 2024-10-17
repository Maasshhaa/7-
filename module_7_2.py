def custom_write(file_name, strings):
    file = open(file_name, 'r+', encoding='utf-8')
    strings_positions = {}
    k = 1   # номер строки
    for i in strings:
        strings_positions[k, (file.tell())] = i
        file.write(f'{i}\n')
        k += 1
    file.close()
    return strings_positions


info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write('file1.txt', info)
for elem in result.items():
    print(elem)
