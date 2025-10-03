
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
    mid = len(lst) // 2
    high = len(lst) - 1

    while lst[mid] != number and low <= high:
        if number > lst[mid]:
            low = mid + 1
            steps += 1
        else:
            high = mid - 1
            steps += 1
        mid = (low + high) // 2
    if low > high:
        return (None, steps)
    else:
        return (number, steps)


def guess_number():
    """Принимает на вход 4 значения: искомое и диапозон для поиска (начало и конец диапозона), а также вариацию
    поиска. Запускает функцию guess_number"""
    number = int(input("Введите искомое число: "))
    start = int(input("Введите начало диапозона: "))
    finish = int(input("Введите конец диапозона: "))
    var = int(input("Введите вариацию поиска: "))
    if var == 1:
        target, steps_count = lin_guess_number(number, start, finish)

    if var == 2:
        target, steps_count = bin_guess_number(number, start, finish)

    return "Искомое число: " + str(target), "количество шагов: " + str(steps_count)


print(guess_number())
