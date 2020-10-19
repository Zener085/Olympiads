'''
В зоопарке Сингапура есть несколько кроликов. Чтобы накормить их, смотритель зоопарка купил n морковок, имеющих длины a1,a2,a3,…,an. Кролики очень быстро размножаются. У смотрителя зоопарка сейчас есть k кроликов и недостаточно морковок, чтобы прокормить их всех. Чтобы решить эту проблему, он решил разрезать морковки так, чтобы суммарно получилось k кусков. По некоторой причине длины всех получившихся морковок должны быть положительными целыми числами.

Кролику очень сложно кушать длинную морковку, поэтому время, которое требуется, чтобы съесть морковку длины x, равно x2.

Помогите смотрителю зоопарка разделить его морковки и найдите минимальное суммарное время, которое потребуется кроликам, чтобы их съесть.

Входные данные
В первой строке находятся два целых числа n и k (1≤n≤k≤105): изначальное количество морковок и количество кроликов.

В следующей строке находятся n целых чисел a1,a2,…,an (1≤ai≤106): длины морковок.

Гарантируется, что сумма ai не меньше k.

Выходные данные
Выведите одно целое число: минимальное суммарное время, которое потребуется кроликам, чтобы съесть морковки при каком-то их разделении.
'''

# This code is not working, I must fix it.

n, k = map(int, input().split())
a = []

x = input().split()

for i in range(n):
    a.append(int(x[i]))
    

while len(a) != k:
    a.sort()
    x, y = 0, 0
    if a[-1] % 2 == 0:
        x = a[-1] // 2
        y = x
    else:
        x = (a[-1] + 1) // 2
        y = x - 1
    a.pop(len(a) - 1)
    a.append(x)
    a.append(y)

a.sort()
x = 0
for i in a:
    x += i ** 2

print(x)
