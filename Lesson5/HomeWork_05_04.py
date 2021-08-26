# Напишите программу - дневник, которая при каждом запуске:
# 1. Спрашивает у пользователя дату и просит ввести краткую запись о событиях на эту дату;
# 2. Добавляет в файл дневника новую запись;
# 3. Считывает и выводит на экран все записи из дневника.
# Обратите внимание, что каждая запись в дневнике должна быть отдельной строкой
# (подумайте, какой специальный символ нужно для этого использовать).

date = input('Укажите дату: ')
entry = input('Событие/наблюдение: ')

# Открытие на запись и дозапись
with open('diary.txt', 'a') as file:
    # Запись в файл с переносом строки
    file.write('\nДата: ' + date + '\n')
    file.write(entry + '\n')

# Открытие на чтение
with open('diary.txt', 'r') as file:
    data = file.read()
    print(data + '\n')








