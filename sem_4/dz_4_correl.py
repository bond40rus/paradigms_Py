import math


def pearson_correlation(array_1, array_2):
    """
    Расчет корреляции Пирсона между двумя массивами.
    """

    if len(array_1) != len(array_2):
        raise ValueError("Массивы должны быть одинаковой длины")

    n = len(array_1)

    # Расчет среднего значения
    avg_x = sum(array_1) / n
    avg_y = sum(array_2) / n

    variance_x = sum([(xi - avg_x) ** 2 for xi in array_1]) / float(len(array_1))
    variance_y = sum([(yi - avg_y) ** 2 for yi in array_2]) / float(len(array_2))
    # функция zip  создает картежи  паралейно с двумя массиввами
    covariance = sum([(xi - avg_x) * (yi - avg_y) for xi, yi in zip(array_1, array_2)]) / float(len(array_1))
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation


array_1 = [10, 22, 33, 14, 25, 37, 7]
array_2 = [16, 27, 38, 19, 25, 16, 17]

correlation = round(pearson_correlation(array_1, array_2), 3)
print(f"Корреляция Пирсона: {correlation}")
