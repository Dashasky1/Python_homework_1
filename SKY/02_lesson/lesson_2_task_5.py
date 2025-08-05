
def month_to_season(month):
    if 1 <= month <= 2 or month == 12:
        return "Зима"
    if 3 <= month <= 4 or month == 5:
        return "Весна"
    if 6 <= month <= 7 or month == 8:
        return "Лето"
    if 9 <= month <= 10 or month == 11:
        return "Осень"
    else:
        return "Такого месяца нет"

try:
    month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(month))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")



