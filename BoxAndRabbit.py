'''
Кролик пытается передвинуть коробку с едой для остальных обитателей зоопарка на координатной плоскости из точки с координатами (x1,y1) в точку с координатами (x2,y2).

У него есть веревка, которую он может использовать для того, чтобы тянуть коробку. Он может двигать коробку, только если он находится на расстоянии ровно 1 от коробки в направлении одной из двух координатных осей. Тогда он может передвинуть коробку в то место, где он сейчас находится, и сам подвинуться на 1 в том же направлении.

Например, если коробка находится в точке (1,2), и кролик находится в точке (2,2), он может передвинуть коробку вправо на 1, поместив коробку в точку (2,2). Сам кролик переместится в точку (3,2).

Также кролик может переместиться на 1 вправо, влево, вверх или вниз, не двигая коробку. В этом случае он не обязательно должен находиться на расстоянии 1 от коробки в направлении одной из координатных осей. Чтобы снова передвинуть коробку, он должен снова оказаться в точке рядом с коробкой. Кроме того, кролик не может переместиться в точку с коробкой.

Кролик может стартовать в любой точке. Он тратит 1 секунду на то, чтобы переместиться на 1 вправо, влево, вверх или вниз независимо от того, тянет ли он коробку при движении или нет.

Определите минимальное время, которое требуется, чтобы переместить коробку из точки (x1,y1) в точку (x2,y2). Обратите внимание, что неважно, в какой точке при этом в конце окажется кролик.

Входные данные
Каждый тест состоит из нескольких наборов входных данных. В первой строке находится единственное целое число t (1≤t≤1000): количество наборов входных данных. Описание наборов входных данных следует.

Каждая из следующих t строк содержит четыре целых числа x1, y1,x2,y2 (1≤x1,y1,x2,y2≤109), описывающих очередной набор входных данных.

Выходные данные
Для каждого набора входных данных выведите единственное целое число: минимальное время в секундах, которое нужно кролику, чтобы переместить коробку из (x1,y1) в (x2,y2).
'''

def move_y(y1, y2):
    t_y = 0
    
    if y1 < y2:
        t_y += y2 - y1
    else:
        t_y += y1 - y2
    if t_y < 0:
        t_y *= (-1)
    
    return t_y
    print(t_y)

def move_x(x1, x2, y1, y2):
    t_x = 0
    if x1 < x2:
        t_x += x2 - x1
    else:
        t_x += x1 - x2
    if t_x < 0:
        t_x *= (-1)

    if y1 != y2:
        t1 = move_y(y1, y2)
        return t_x + t1 + 2
    else:
        return t_x

x = int(input())
for i in range(x):
    x1, y1, x2, y2 = map(int, input().split())
    t = 0

    if x1 != x2:
        t = move_x(x1, x2, y1, y2)
    else:
        if y1 != y2:
            t = move_y(y1, y2)

    print(t)
