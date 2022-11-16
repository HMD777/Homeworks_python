print('Напишите программу, удаляющую из текста все слова, содержащие ""абв"".')
data = input ('Введите текст через пробел\n')
find_txt = 'абв'
data_list = [i for i in data.split() if find_txt not in i]
print (f'Результат: {" ".join(data_list)}')