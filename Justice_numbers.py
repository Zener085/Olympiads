"""
Назовём натуральное число справедливым, если оно делится на каждую из своих ненулевых цифр.
Например, число 102 справедливое (так как оно делится и на 1, и на 2), а число 282 — нет, потому что не делится на 8.
По данному n найдите минимальное x, такое что n≤x и x — справедливое.

Входные данные
В первой строке содержится t — количество тестовых случаев (1≤t≤103).
В каждой из следующих t строк по одному целому числу n (1≤n≤1018).

Выходные данные
Для каждого из t тестовых случаев в новой строке выведите наименьшее справедливое число, не меньшее n.
"""


def divension(number):
    x = int(number)
    b = True

    for j in range(len(number)):
        if int(number[j]) != 0 and x % int(number[j]) != 0:
            b = False

    return b


t = int(input())

for i in range(t):
    n = str(input())
    while not divension(n):
        n = str(int(n) + 1)

    print(n)
