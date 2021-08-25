shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}


def get_names(key, value):
    series_name = []
    for i in shows.keys():
        if key[i] == value:
            series_name.append(i)
    print('Названия сериалов для указанного жанра: ', series_name)
    return series_name


series_name = get_names(shows, value=input('Введите название жанра: '))


def get_rating(key, value):
    series_rating = []
    for i in value:
        series_rating.append(key[i])
    print('Рейтинги этих сериалов: ', series_rating)


get_rating(ratings, series_name)
