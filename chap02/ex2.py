
#n은 행 m을 열
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    #가장 적은수 들에서 가장 큰 수 찾기

    result = max(result, min_value)

print(result)
