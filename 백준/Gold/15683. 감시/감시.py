import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# cctv들 돌려서 사각 지대의 최소 크기를 구하기
def solution():
    n, m = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(n)]
    # 방향 벡터: 상(0), 우(1), 하(2), 좌(3)
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    # CCTV 종류별 가능한 방향 조합 (각 번호에 대해 리스트로 관리)
    cctv_directions = {
        1: [[0], [1], [2], [3]], # 한 방향
        2: [[0, 2], [1, 3]], # 상하, 좌우
        3: [[0, 1], [1, 2], [2, 3], [3, 0]], # 상우, 우하, 하좌, 좌상
        4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], #상우하, 우하좌, 하좌상, 좌상우
        5: [[0, 1, 2, 3]] # 상우하좌
    }
    # 감시 방향 정하기 위해 CCTV 단위로 반복해야 함-> 모든 cctv를 리스트로 모아서 처리하자. (탐색 대상 분리)
    cctvs = [(i,j,office[i][j]) for i in range(n) for j in range(m) if 1<=office[i][j]<=5]
    
    # 주어진 좌표에서 dirs에 따른 방향으로 cctv 하나가 감시할 수 있는 영역 표시
    def watch(x, y, dirs, office):
        watched = [] # 감시받는 좌표 저장 배열
        for d in dirs: # ex. [0], [0, 2], [1, 3] 등
            dx, dy = directions[d]
            nx, ny = x+dx, y+dy
            while 0<=nx<n and 0<=ny<m:
                if office[nx][ny] == 6:
                    break
                if office[nx][ny] == 0:
                    office[nx][ny] = -1 # 감시 표시
                    watched.append((nx, ny))
                nx += dx # 일직선으로 쭉 감시
                ny += dy
        return watched
    
    result = n*m # 나올 수 있는 최댓값(아무것도 없는 경우)
    def backtracking(cnt, office):
        nonlocal result
        if cnt == len(cctvs):
            total = sum(row.count(0) for row in office)
            result = min(result, total)
            return
        # cctv 담아논 배열에서 cctv 한개 꺼내기
        x, y, cctv_kind = cctvs[cnt]

        for dirs in cctv_directions[cctv_kind]:
            watched_positions = watch(x, y, dirs, office)
            backtracking(cnt+1, office)
            # 원상복구
            for wx, wy in watched_positions:
                office[wx][wy] = 0

    backtracking(0, office) # cctv에 담긴 배열이 없더라고 위의 if절에서 처리 후 return 하기 때문에 인덱스 에러 안남
    print(result)

solution()