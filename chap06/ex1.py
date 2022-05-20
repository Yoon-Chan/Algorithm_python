#실전문제 위에서 아래로
"""
    책 답안

    n = int(input())

    array =[]
    for i in range(n):
        array.append(int(input())
    array = sorted(array, reverse = True)

   for i in array:
    print(i, end=' ')
"""


N = int(input())

array = [0] * N

for i in range(N):
    array[i] = int(input())


array.sort()
array.reverse()

for i in array:
    print(i, end=' ')