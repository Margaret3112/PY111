def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    stack = []
    for element in brackets_row:
        if element == "(":
            stack.append(element)
        elif element == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    return not stack


     # TODO реализовать проверку скобочной группы


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
