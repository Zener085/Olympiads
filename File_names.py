"""
Петя и Вася любят писать свои операционные системы, поэтому на компьютере Пети установлена операционная система PetOS,
а на компьютере Васи — VasOS.
Однажды Петя захотел передать Васе несколько файлов со своего компьютера, но выяснилось, что сделать это не так просто.
Дело в том, что в PetOS именем файла может быть любая строка, состоящая из латинских букв и точек,
длиной от 1 до 20 символов, а в VasOS поддерживаются только имена файлов вида <filename>.<extension>,
где <filename> и <extension> — непустые строки, состоящие из латинских букв,
при этом длина <filename> должна быть не больше 8, а длина <extension> — не больше 3.
Помогите Пете по списку имен файлов понять, сколько из них он сможет передать на компьютер Васи,
не меняя их имя.

Формат входных данных
Первая строка содержит число n — число файлов в списке Пети (1 6 n 6 100). Следующие n
строк содержат имена файлов. Все имена имеют длину от 1 до 20 символов и содержат только
строчные латинские буквы и точки.

Формат выходных данных
Выведите одно число — число файлов, которые Петя может передать Васе без переименования.

Система оценки
В этой задаче все тесты оцениваются независимо.
"""

n = int(input())
res = 0

for i in range(n):
    x = input().split('.')
    if len(x) != 2:
        continue
    else:
        if 1 <= len(x[0]) <= 8:
            if 1 <= len(x[1]) <= 3:
                res += 1

print(res)
