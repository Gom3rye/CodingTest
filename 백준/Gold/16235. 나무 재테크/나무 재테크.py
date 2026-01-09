import sys
from collections import deque
input = sys.stdin.readline
def solution():
    # K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하기
    n, m, k = map(int, input().split()) # 땅사이즈 <=10, #나무 <=100, 년 <=1000
    # 겨울에 추가될 양분 양
    a = [list(map(int, input().split())) for _ in range(n)]
    # 나무의 나이가 어린 순으로 먹이를 주니까 deque로 관리하자(새 나무 생겨도 appendleft()하면 나이 순으로 정렬 유지할 수 있으니까)
    tree = [[deque() for _ in range(n)] for _ in range(n)]
    # 입력으로 주어지는 나무의 위치는 모두 다르다고 했으니까 어린 순으로 정렬하지 않아도 된다.
    for _ in range(m):
        x, y, z = map(int, input().split())
        tree[x-1][y-1].append(z) # 0based index
    # 초기 양분은 5로 시작
    nutrition = [[5]*n for _ in range(n)]
    # 격자 단위로 끊어서 생각해도 된다.
    for _ in range(k): # <=1000
        for x in range(n): # <=10
            for y in range(n): # <=10
                dead = []
                new_tree = deque()
                # 봄) 나이만큼 양분 먹고 나이 +1, 못하면 죽음
                for year in tree[x][y]: # <=100
                    if nutrition[x][y]-year >= 0:
                        nutrition[x][y] -= year
                        new_tree.append(year+1)
                    else: # 양분이 부족해 못 먹는다면
                        dead.append(year) # 죽은 나무의 나이 저장
                tree[x][y] = new_tree # 나무 갱신
                # 여름) 죽은 나무가 양분으로 추가됨
                for year in dead:
                    nutrition[x][y] += year//2
        for x in range(n):
            for y in range(n):
                # 가을) 나이가 5의 배수면 인접 8칸에 나이1인 나무 번식함
                for year in tree[x][y]:
                    if year%5 == 0:
                        for nx, ny in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:
                            if 0<=nx<n and 0<=ny<n:
                                tree[nx][ny].appendleft(1)
                # 겨울) 양분 추가
                nutrition[x][y] += a[x][y]

    # 살아있는 나무 개수 구하기
    total_trees = 0
    for i in range(n):
        for j in range(n):
            total_trees += len(tree[i][j])
    print(total_trees)
solution()