"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

from collections import deque


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 10  # наименьший приоритет

    def __init__(self):
       self.new = {priority: deque() for priority in range(self.HIGH_PRIORITY, self.LOW_PRIORITY + 1)}
  # TODO использовать deque для реализации очереди с приоритетами

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемент в конец очереди c учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """
        self.new[priority].append(elem)
        # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        for priority in range(self.HIGH_PRIORITY, self.LOW_PRIORITY + 1):
            if self.new[priority]:
                return self.new[priority].popleft()
        raise IndexError("Очередь пуста")  # TODO реализовать метод dequeue

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)
        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Индекс должен быть целым числом")
        if priority < self.HIGH_PRIORITY or priority > self.LOW_PRIORITY:
            raise ValueError(f"Приоритет должен быть от {self.HIGH_PRIORITY} до {self.LOW_PRIORITY}")

        queue = self.new[priority]
        if ind < 0 or ind >= len(queue):
            raise IndexError("Индекс вне границ очереди")
        return queue[ind]
        # TODO реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        for q in self.new.values():
            q.clear() # TODO реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. """
        return sum(len(q) for q in self.new.values())
# TODO реализовать метод __len__
