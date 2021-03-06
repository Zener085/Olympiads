"""
Дана шахматная доска размера n×n. Строки и столбцы доски пронумерованы от 1 до n.
Клетка (x,y) лежит на пересечении столбца номер x и строки номер y.

Ладья это шахматная фигура, которая за один ход может переместиться на любое количество клеток по вертикали,
либо по горизонтали. На доске размещены m ладей (m<n), которые не бьют друг друга. То есть, нет пары ладей,
стоящих на одной вертикали или горизонтали.

За один ход можно сделать ход одной из ладей. То есть,
переместить ее на любое количество клеток по вертикали или горизонтали.
При этом, после хода ладья снова не должна оказаться под боем других ладей.
Какое минимальное количество ходов нужно сделать, чтобы разместить все ладьи на главной диагонали?

Главной диагональю называются клетки (i,i), где 1≤i≤n.

Входные данные
В первой строке дано целое число t — количество тестовых случаев (1≤t≤103). Далее дано описание t тестовых случаев.

В первой строке даны два целых числа n и m — размер поля и количество ладей (2≤n≤105, 1≤m<n).
Следующие m строк содержат пары целых чисел xi и yi — позиции ладей,
i-я ладья исходно стоит в клетке (xi,yi) (1≤xi,yi≤n).
Гарантируется, что в исходной расстановке ладьи не бьют друг друга.

Сумма n по всем тестовым случаям не превышает 105.

Выходные данные
Для каждого из t тестовых случаев в новой строке выведите наименьшее количество ходов, которые требуются,
чтобы поставить все ладьи на главную диагональ.

Можно доказать, что это всегда возможно.
"""

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    res = 0
    a = [0] * n

    for j in range(m):
        x, y = map(int, input().split())
        if x != y:
            temp = a[x - 1] + a[y - 1]

            res += temp

        a[x - 1] = 1
        a[y - 1] = 1

    print(res + 1)
