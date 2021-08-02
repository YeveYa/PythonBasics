# Задание:
# Вам нужно написать программу, которая считает, сколько вам будет лет в том или ином году. Сначала программа
# спрашивает, в каком году вы родились, потом спрашивает год, к которому нужно будет рассчитать возраст. После этого
# она его печатает.

# Пользователь указывает год рождения
birth = int(input('Укажите год вашего рождения: '))

# Пользователь указывает год, к которому нужно будет рассчитать возраст
calc_age = int(input('К какому году нужно посчитать возраст? '))

# Проверка корректности введенных данных
while calc_age < birth:
    print('Ошибка! Год, к которому вы хотите вычислить Ваш возрат, не может быть меньше года рождения.')
    calc_age = int(input('К какому году нужно посчитать возраст? '))

# Вычисление и вывод возраста пользователя
print('Ваш возраст в', calc_age, 'году будет', calc_age - birth)

