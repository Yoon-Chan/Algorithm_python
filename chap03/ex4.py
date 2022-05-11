#게임 개발 문제
#못풀어서 답지를 봄..
# N, M을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

#방문한 위치를 저장하기 위한 맵을 생성.
d =  [[0] * m for _ in range(n)]

#현재 캐릭터의 x,y좌표와 방향
x, y ,direction = map(int, input().split())
#현재 좌표 방문 처리
d[x][y] = 1

#전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
#북, 동, 남, 선 방향 정리
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전하기
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


#시물레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전한 이후 정면에 가보지 않은 같이 존재하는 경우 이동
    if d[nx][ny] ==0 and array[nx][ny] == 0 :
        array[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]
        
        #뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
        
#정답 출력
print(count)
        
    