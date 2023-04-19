countries = {'kg': {'red', 'yellow'},
             'ru': {'white', 'blue', 'red'},
             'us': {'white', 'blue', 'red'},
             'sp': {'orange', 'red', 'white'}}


def find_counties_with_colors(countries, *colors):
    if len(countries) == 0 or len(colors) == 0:
        return -1

    result = []

    if len(colors) == 1:
        for k, v in countries.items():
            for set_value in v:
                if set_value == colors[0]:
                    result.append(k)

        return result

    iterator = 0
    for k, v in countries.items():
        for color in colors:
            for set_value in v:
                if set_value == color:
                    iterator += 1

        if iterator == len(colors):
            result.append(k)

        iterator = 0

    return result


while True:
    colors = input('Введите один или несколько цветов: ')

    if colors == 'q':
        break

    if len(colors) == 0:
        print('Вы ввели пустую строку. Попробуйте еще раз!')
        continue

    if ' ' in colors:
        colors = colors.split()

    result_countries = find_counties_with_colors(countries, colors)

    if result_countries == []:
        print(
            'Заданного цвета нет во влагах стран из списка. Попробуйте ввести другой цвет!')
        continue

    for country in result_countries:
        print(country)
