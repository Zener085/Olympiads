'''
Технокубок, 1 отборочный раунд

Дана строка, состоящая из букв латинского алфавита. В целях ее компрессии разрешается любые ее непустые подстроки (подстрокой называется последовательность идущих подряд символов строки) сжимать по следующему правилу. Строка A, состоящая из повторений некоторой непустой строки B, записывается как символ «(», затем количество повторений (целое число от 1 до 105, записанное без ведущих нулей), затем строка B, и, наконец, символ «)». Например, строку ababab можно сжать, записав ее как (3ab).

В данной задаче допускается повторное сжатие подстрок строки. Разумеется, можно сжимать лишь части, состоящие только из букв латинского алфавита. Например, строку acacacaacacaca можно сжать, записав ее в виде (2acacaca), и осуществить дальнейшую компрессию: (2(3ac)a).

Ваша задача осуществить обратное преобразование, то есть преобразовать строку из сжатого вида в несжатый.

Входные данные
Во входном файле записана непустая строка в сжатом виде. Длина строки не превосходит 1000 символов.

Выходные данные
Выведите результат декомпрессии строки. Гарантируется, что длина ответа не превосходит 105 символов. Заметим, что в результате декомпрессии длина строки может уменьшиться.

Задача не доделана.
'''

n = input()
while '(' in n:
    n = n[1:-1]
    a = 0
    qount = 0
    for i in n:
        try:
            i = int(i)
            a = a * 10 + i
            qount += 1
        except:
            break
    n = n[qount:]
    print(n)
    