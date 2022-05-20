#부품 찾기

N = int(input())
arrayN = list(map(int, input().split()))

M = int(input())
arrayM = list(map(int, input().split()))

def binary_serach(array, target, start, end):
    if start >= end :
        return "no"

    mid = (start + end )// 2

    if array[mid] == target:
        return "yes"

    elif array[mid] >= target:
        return binary_serach(array,target, start, mid-1)
    else:
        return binary_serach(array,target,mid+1, end)


arrayN = sorted(arrayN)

result=[]
for i in arrayM:
    result.append(binary_serach(arrayN, i, 0, len(arrayN) ))


for i in result:
    print(i, end=' ')
