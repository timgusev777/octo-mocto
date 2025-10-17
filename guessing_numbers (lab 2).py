import unittest

def lin_guess_number(number, start, finish):
    steps = 0
    """функция ищет загаданное число и возвращает само число и количество 'шагов' необходимых для линейного поиска"""
    lst = []
    for i in range(start, finish+1):
        lst.append(i)

    for j in range(len(lst)):
        if lst[j] == number:
            steps += 1
            break
        else:
            steps += 1
    return(number, steps)

def bin_guess_number(number, start, finish):
    lst = []
    steps = 0
    """функция ищет загаданное число и возвращает само число и количество 'шагов' необходимых для бинарного поиска"""
    for i in range(start, finish+1):
        lst.append(i)

    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == number:
            return (number, steps + 1)

        elif number > lst[mid]:
            low = mid + 1
            steps += 1
        else:
            high = mid - 1
            steps += 1

    return(None, steps)


def guess_number():
    """Принимает на вход 4 значения: искомое и диапозон для поиска (начало и конец диапозона), а также вариацию
    поиска. Запускает одну из функций *_guess_number"""
    number = int(input("Введите искомое число: "))
    start = int(input("Введите начало диапозона: "))
    finish = int(input("Введите конец диапозона: "))
    var = int(input("Введите вариацию поиска: "))
    if var == 1:
        target, steps_count = lin_guess_number(number, start, finish)

    if var == 2:
        target, steps_count = bin_guess_number(number, start, finish)

    return target, steps_count


class TestMath(unittest.TestCase):
    def test_lin_guess_number_1(self):
        self.assertEqual(lin_guess_number(5, 1, 10), (5, 5))

    def test_lin_guess_number_2(self):
        self.assertEqual(lin_guess_number(1, 1, 3), (1, 1))

    def test_bin_guess_number_1(self):
        self.assertEqual(bin_guess_number(5, 1, 10), (5, 1))

    def test_bin_guess_number_2(self):
        self.assertEqual(bin_guess_number(1, 1, 10), (1, 3))

unittest.main(argv=[''], verbosity=2, exit=False)
