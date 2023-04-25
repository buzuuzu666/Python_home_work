#Задача 22: 
#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, 
#которые встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
#m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

set_1 = list(set(map(int, input("Введите элементы первого массива через пробел: ").split())))
set_2 = list(set(map(int, input("Введите элементы второго массива через пробел: ").split())))

el = []
for i in set_1:
    if i in set_2 and i not in el:
        count_1 = set_1.count(i)
        count_2 = set_2.count(i)
        for j in range(min(count_1, count_2)):
            el.append(i)

el.sort()

for i in el:
    print(el, end=" ")
print()


#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
#Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
#Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, 
#находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
#находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input())
arr = list()
for i in range(n):
    x = int(input())
    arr.append(x)

arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])
print(max(arr_count))
