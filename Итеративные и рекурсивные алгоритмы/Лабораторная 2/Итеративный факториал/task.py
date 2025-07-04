def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
     # TODO реализовать итеративный алгоритм нахождения факториала
    if not isinstance(n, int):
        raise TypeError
    if n < 0:
        raise ValueError


    if n == 0:
        res = 1
        return res

    res = 1
    while n > 0:
        res *=  n
        n = n - 1
    return res