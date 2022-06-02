#서로소 집합을 활용한 사이클 판별 소스코드
#위와 같은 방법은 모든 수를 확인하는 경우가 생겨 비효율성이 생긴다.
#이를 해결하기 위해 경로 압축 하는 방법
def find_parent(parent, x):
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1) #부모 테이블 초기화

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i


cycle = False

for i in range(e):
    a, b = map(int, input().split())
    #사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b) :#두 부모의 노드가 같다면 사이클 생성
        cycle= True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")