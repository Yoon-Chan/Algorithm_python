#왕실의 나이트
"""
    책 답안
    input_data = input()
    row = int(input_data[1])
    column = int(ord(input_data[0]) - int(ord('a')) + 1

    #나이트가 이동할 수 있는 8가지 방향
    steps = [(-2,-1) , (-1, -2) , (1,-2), (2,-1), (2,1), (1,2), (-1,2) , (-2,1)]

    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]

        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 0 :
            result +=1

"""


#내가 푼 방법
y = ['a', 'b','c','d','e','f','g','h']
x = ['1','2','3','4', '5','6','7','8']

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [1, -1, 1, -1, -2, 2, -2, 2]

row, col = 0,0

h = input()
for idy, i in enumerate(y):
    for idx, j in enumerate(x):
        if h in i+j:
            row, col = idx, idy

count  = 0

for i in range(8):
    rowdx = row + dx[i]
    coldy = col + dy[i]

    if rowdx < 0 or rowdx > len(x)-1 or coldy < 0 or coldy > len(y)-1:
        continue
    count +=1

print(count)