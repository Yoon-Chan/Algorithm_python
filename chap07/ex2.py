#떡볶이 떡 만들기

N, M = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

def Search(array,start, end, M):
    r = 0

    while start <= end:
        count = 0
        mid = (start + end)//2
        for i in array:
            if mid < i:
                count += (i-mid)

        if count == M:
            return mid
        elif count < M:
            end = mid
        else :
            r = max(r, mid)
            start = mid

    return r


result = Search(array, 0, array[-1], M)
print(result)