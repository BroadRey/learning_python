from enum import Enum


class Months(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


def is_valid_number_of_month(month_number):
    if not month_of_birth.isdigit():
        return False

    month_number = int(month_of_birth)

    if month_number <= 0 or month_number >= 13:
        return False

    return True


def is_valid_number_of_day(day_number, month_number):
    if not day_number.isdigit():
        return False

    day_number = int(day_number)
    month_number = int(month_number)

    if day_number <= 0:
        return False

    if ((month_number == Months.January.value and day_number > 31) or
            (month_number == Months.February.value and day_number > 29) or
            (month_number == Months.March.value and day_number > 31) or
            (month_number == Months.April.value and day_number > 30) or
            (month_number == Months.May.value and day_number > 31) or
            (month_number == Months.June.value and day_number > 30) or
            (month_number == Months.July.value and day_number > 31) or
            (month_number == Months.August.value and day_number > 31) or
            (month_number == Months.September.value and day_number > 30) or
            (month_number == Months.October.value and day_number > 31) or
            (month_number == Months.November.value and day_number > 30) or
            (month_number == Months.December.value and day_number > 31)):
        return False

    return True


def find_out_the_sign_of_zodiac(day_number, month_number):
    if not is_valid_number_of_month(day_number):
        raise TypeError("Несуществующий месяц рождения")

    if not is_valid_number_of_day(day_number, month_number):
        raise TypeError("Несуществующий день рождения")

    day_number = int(day_number)
    month_number = int(month_number)

    if ((day_number >= 21 and month_number == Months.March.value) or
            (day_number <= 20 and month_number == Months.April.value)):
        return "Овен"
    elif ((day_number >= 21 and month_number == Months.April.value) or
            (day_number <= 21 and month_number == Months.May.value)):
        return "Телец"
    elif ((day_number >= 22 and month_number == Months.May.value) or
            (day_number <= 21 and month_number == Months.June.value)):
        return "Близнецы"
    elif ((day_number >= 22 and month_number == Months.June.value) or
            (day_number <= 22 and month_number == Months.July.value)):
        return "Рак"
    elif ((day_number >= 23 and month_number == Months.July.value) or
            (day_number <= 21 and month_number == Months.August.value)):
        return "Лев"
    elif ((day_number >= 22 and month_number == Months.August.value) or
            (day_number <= 23 and month_number == Months.September.value)):
        return "Дева"
    elif ((day_number >= 24 and month_number == Months.September.value) or
            (day_number <= 23 and month_number == Months.October.value)):
        return "Весы"
    elif ((day_number >= 24 and month_number == Months.October.value) or
            (day_number <= 22 and month_number == Months.November.value)):
        return "Скорпион"
    elif ((day_number >= 23 and month_number == Months.November.value) or
            (day_number <= 22 and month_number == Months.December.value)):
        return "Стрелец"
    elif ((day_number >= 23 and month_number == Months.December.value) or
            (day_number <= 20 and month_number == Months.January.value)):
        return "Козерог"
    elif ((day_number >= 21 and month_number == Months.January.value) or
            (day_number <= 19 and month_number == Months.February.value)):
        return "Водолей"
    elif ((day_number >= 20 and month_number == Months.February.value) or
          (day_number <= 20 and month_number == Months.March.value)):
        return "Рыбы"

try:
    day_of_birthday = input("Введите день рождения: ")
    month_of_birth = input("Введите месяц рождения: ")
    print(find_out_the_sign_of_zodiac(day_of_birthday, month_of_birth))
except TypeError as ex:
    print(ex)
