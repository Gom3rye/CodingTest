import sys
input = sys.stdin.readline

# 1. 바람 방향 변경 함수 정의
def change_dir(dir, object) :
    # 1-1. 3번 물건인 경우
    if object == 3 :
        # 변경된 바람 방향 반환
        return ChangeDir_3[dir]
    # 1-2. 4번 물건인 경우
    else :
        # 변경된 바람 방향 반환
        return ChangeDir_4[dir]
# 2. 바람 이동 함수 정의
def move(x, y, dir) :
    # 2-1.
    while 0 <= x < n and 0 <= y < m :
        # 2-2-1. 현재 위치에 해당 바람의 방향이 지나간 적이 있다면 return
        if dir in graph[x][y] : return
        # 2-2-2, 그래프에 현재 위치 방향 정보 업데이트
        graph[x][y].append(dir)
        # 2-2-3. 현재 위치에 물건이 있는 경우
        # 물건에 막히는 경우
        # 1번 물건이면서 바람이 좌우로 부는 경우
        # 2번 물건이면서 바람이 상하로 부는 경우
        if (classroom[x][y] == 1 and dir in [2, 3]) or (classroom[x][y] == 2 and dir in [0, 1]) : return
        # 바람이 꺾이는 물건이 있을 경우
        elif classroom[x][y] in [3, 4] :
            # 바람 방향 변경
            dir = change_dir(dir, classroom[x][y])
        # 2-2-4. 다음 위치 설정
        x, y = x + dirs[dir][0], y + dirs[dir][1]
# 3. 앉을 수 있는 자리 계산 함수 정의
def calculate() :
    cnt = 0
    # 3-1.
    for i in range(n) :
        for j in range(m) :
            # 바람이 지나가는 자리 체크
            if graph[i][j] : cnt += 1
    # 3-2. 앉을 수 있는 자리 수 반환
    return cnt

n, m = map(int, input().split())
classroom = [list(map(int, input().split())) for _ in range(n)]

# 4. 3번 물건으로 인한 바람 방향 변경 딕셔너리 생성
ChangeDir_3 = {0 : 3, 1 : 2, 2: 1, 3 : 0}
# 5. 4번 물건으로 인한 바람 방향 변경 딕셔너리 생성
ChangeDir_4 = {0 : 2, 1 : 3, 2: 0, 3 : 1}
# 6. 방향 리스트 생성
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 7. 에어컨 위치 인덱스 리스트 생성
air_conditioner = []
for i in range(n) :
    for j in range(m) :
        if classroom[i][j] == 9 :
            air_conditioner.append((i, j))
# 8. 그래프 생성
graph = [ [ [] for _ in range(m)] for _ in range(n) ]
# 9.
for x, y in air_conditioner :
    # 9-1.
    for dir in range(4) :
        # 바람 이동
        move(x, y, dir)
# 10. 앉을 수 있는 자리 출력
print(calculate())