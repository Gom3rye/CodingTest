import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    order = [] # 자리에 앉을 순서
    likes = {} # 한 학생이 좋아하는 학생들의 정보
    for _ in range(n**2):
        p, l1, l2, l3, l4 = map(int, input().split())
        likes[p] = {l1, l2, l3, l4}
        order.append(p)
    seat = [[-1]*n for _ in range(n)]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    # 필요한 변수 정의: (인접칸에 있는)좋아하는 학생 수, 비어있는 칸 수, 최적의 자리r, c
    for p in order: # <=400
        like_set = likes[p]
        best_r, best_c = -1, -1 # 최적의 자리는 불가능하게 초기화
        max_like_cnt = -1
        max_empty = -1
        for i in range(n): # <= 20
            for j in range(n):
                like_cnt = 0
                empty = 0
                if seat[i][j] != -1: # 이미 자리 차지되고 있는 것
                    continue
                for dx, dy in directions:
                    nx, ny = dx+i, dy+j
                    if 0<=nx<n and 0<=ny<n:
                        if seat[nx][ny] == -1:
                            empty += 1
                        elif seat[nx][ny] in like_set:
                            like_cnt += 1
                # 좋아하는 학생 수, 빈칸 수 고려해서 최적의 자리 찾기
                if like_cnt > max_like_cnt:
                    max_like_cnt = like_cnt
                    max_empty = empty
                    best_r, best_c = i, j
                elif like_cnt == max_like_cnt:
                    if empty > max_empty:
                        max_empty = empty
                        best_r, best_c = i, j
                # (r, c)를 순서대로 탐색하므로 동점일 때는 갱신하지 않으면 자동으로 규칙 만족
        seat[best_r][best_c] = p
    # 만족도 = 10**(학생 수-1) if 학생 수 != 0 else 0
    total = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            for dx, dy in directions:
                nx, ny = dx+i, dy+j
                if 0<=nx<n and 0<=ny<n:
                    if seat[nx][ny] in likes[seat[i][j]]:
                        cnt += 1
            total += 10**(cnt-1) if cnt != 0 else 0
    print(total)
solution()