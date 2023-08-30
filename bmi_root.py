def input_height():
    """
    Функция принимает значение от юзера согласно подсказке ввода (рост в см), 
    проверяет корректность ввода и возвращает значение в программу

    """
    while True:
        try:
            h = int(input("Рост в см: "))
        except ValueError:
            print("Введите целое число!")
            continue
        if h >= 300 or h <= 50:
            print("Рост вне допустимого диапазона, введите верное значение!")
            continue
        else:
            return h


def input_weight():
    """
    Функция принимает значение от юзера согласно подсказке ввода (вес в кг), 
    проверяет корректность ввода и возвращает значение в программу

    """
    while True:
        try:
            w = int(input("Вес в кг: "))
        except ValueError:
            print("Введите целое число!")
            continue
        if w >= 300 or w <= 10:
            print("Вес вне допустимого диапазона, введите верное значение!")
            continue
        else:
            return w


def calculate_bmi(h, w):
    """
    
    Функция непосредственного расчёта индекса массы тела. Принимает возвраты
    функций input_height и input_weight, то есть рост и вес, рассчитывает
    значение индекса массы тела. Возвращает число ИМТ с округлением до одного
    знака после запятой и заключение по рассчитанному значению согласно
    условиям.

    """
    res = round((w * 10000) / (h ** 2))
    print("Индекс массы тела =", res, "кг/м2")
    if res <= 18:
        return "Дефицит"
    elif 19 <= res <= 25:
        return "Норма"
    elif 26 <= res <= 29:
        return "Избыточный вес"
    elif 30 <= res < 35:
        return "Ожирение I степени"
    elif 35 <= res < 40:
        return "Ожирение II степени"
    else:
        return "Ожирение III степени (морбидное)"


while True:
    result_calculate_bmi = calculate_bmi(input_height(), input_weight())
    print(result_calculate_bmi)
    print("*" * len(result_calculate_bmi))
