# Даны два массива чисел длины n. 
# Составьте из них один массив длины 2n, в котором числа из входных массивов 
# чередуются (первый — второй — первый — второй — ...). 
# При этом относительный порядок следования чисел из одного массива должен быть сохранён.

n = int(input())

r = list()

a = input().split()

b = input().split()

for i in range(0, n):
    r.append(a[i])
    r.append(b[i])

print(*r)