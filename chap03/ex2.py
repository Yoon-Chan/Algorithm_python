# 시각

"""
    책에 있는 답안
    h = int(input())

    count = 0
    for i in range(h+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k)
                    count += 1

    print(count)

"""


#내가 푼 것

#숫자
n = int(input())

result =0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if n < 10 :
                if (i%10) == 3 or (i//10) ==3 or (j % 10) == 3 or (j // 10) == 3 or (k % 10) == 3 or (k // 10) == 3:
                    result += 1
print(result)