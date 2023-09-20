from random import randint
from typing import List

numbers = [randint(0, 100) for i in range(7)]
print(numbers)


def bubble_sort_imp(ls: List[int]) -> List[int]:
    """Метод сортировки списка пузырьком.
    Попарно сравниваем соседние элементы и меняем местами если правый больше левого.
    В первую итерацию проходим все пары. Затем еще раз. И так, пока список не будет отсортирован"""
    if len(ls) == 0:
        raise ValueError(
            'Список пуст')
    for i in range(0, len(ls) - 1):
        for j in range(len(ls) - 1):
            if ls[j] < ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls

###########################


def bubble_sort_dec(ls: List[int]) -> List[int]:
    if len(ls) == 0:
        raise ValueError(
            'Список пуст')
    return sorted(ls, reverse=True)


print(f'императивный стиль {bubble_sort_imp(numbers)}')
print(f'декларативный стиль {bubble_sort_dec(numbers)}')
