from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
      # TODO реализовать прямой метод расчета
    count_stairs = len(stairway)

    if count_stairs < 0:
        raise ValueError

    if count_stairs == 0:
        return 0

    if count_stairs == 1:
        return stairway[0]

    matrix_state = [0] + list(stairway)

    for i in range(2, count_stairs + 1):
        matrix_state[i] = matrix_state[i]   + min (matrix_state[i - 1], matrix_state[i - 2])

    return matrix_state[count_stairs]

if __name__ == '__main__':
    print(stairway_path([1, 3, 1, 5]))  # 7
