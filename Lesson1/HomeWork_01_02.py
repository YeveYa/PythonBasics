# Задание:
# Программа спрашивает зарплату 3 человек, потом возвращает среднее число, которое показывает, сколько может тратить
# каждый из членов этой семьи.

print('Укажите зарплату (в рублях) за 1 месяц каждого члена семьи из 3х человек.')
salary1 = float(input('Зарплата 1ого: '))
salary2 = float(input('Зарплата 2ого: '))
salary3 = float(input('Зарплата 3его: '))

spent_size = (salary1 + salary2 + salary3) / 3
print('В случае общего бюджета, каждый член семьи может тратить в месяц по', spent_size)
