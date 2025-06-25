from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """

    main = container[0]
    left_cont = []
    for i in container:
        if i < main:
            left_cont.append(i)


    right_cont = []
    for i in container:
        if i > main:
            right_cont.append(i)

    return left_cont + right_cont

    # TODO реализовать алгоритм быстрой сортировки
