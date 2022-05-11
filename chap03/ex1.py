#상하좌우 문제

"""
    책에 있는 답안예시
    #N 입력 받기
    n = int(input())
    plans = input().split()

    #L, R , U, D에 따른 이동 방향
    dx  =[ 0, 0, -1 , 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    #이동 계획을 하나씩 확인
    for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    #공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n  :
        continue
    #이동 수행
    x , y = nx, nu

    print(x,y)


"""

location = [1,1]

n = map(int, input())

data = map(str, input().split())

def move(l):
    if l == "L" and location[1] != 1:
        location[1] -= 1
    elif l == "R" and location[1] != n:
        location[1] +=1
    elif l == "U" and location[0] != 1:
        location[0] -= 1
    elif l == "D" and location[0] != n:
        location[0] +=1


for m in data:
    move(m)

print(location[0], location[1])