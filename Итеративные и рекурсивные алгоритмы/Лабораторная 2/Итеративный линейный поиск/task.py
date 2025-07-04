"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        raise ValueError

    min_element = 0
    for i, value in enumerate(arr):
        if value < arr[min_element]:
            min_element = i
    return min_element
      # TODO реализовать итеративный линейный поиск
