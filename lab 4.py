
import timeit
import matplotlib.pyplot as plt

def fact_recursive(n: int) -> int:
    """Рекурсивный факториал"""
    if n == 0:
        return 1
    return n * fact_recursive(n - 1)


def fact_iterative(n: int) -> int:
    """Нерекурсивный факториал"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def benchmark(func, n, number, repeat):
    """Возвращает среднее время выполнения func(n)"""
    times = timeit.repeat(lambda: func(n), number=number, repeat=repeat)
    return min(times)


numbers = list(range(10, 300, 10))

res_recursive = []
res_iterative = []

for n in numbers:
    res_recursive.append(benchmark(fact_recursive, n, number=10000, repeat=5))
    res_iterative.append(benchmark(fact_iterative, n, number=10000, repeat=5))

# Визуализация
plt.plot(numbers, res_recursive, label="Рекурсивный")
plt.plot(numbers, res_iterative, label="Итеративный")
plt.xlabel("n")
plt.ylabel("Время (сек)")
plt.title("Сравнение рекурсивного и итеративного факториала")
plt.legend()
plt.show()


