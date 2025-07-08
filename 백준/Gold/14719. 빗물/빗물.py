import sys
input = sys.stdin.readline
def solution():
    h, w = map(int, input().split()) # 세로 길이, 가로 길이
    blocks = list(map(int, input().split()))
    # 2차원 배열 형태로 블록 세우기
    graph = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if blocks[j] >= 1:
                graph[i][j] = True
                blocks[j] -= 1
    count = 0
    for i in range(h):
        j_idx = [] # 열 좌표 모아둘 리스트
        for j in range(w):
            if graph[i][j]: # true면
                j_idx.append(j)
        if len(j_idx) >= 2:
            for i in range(len(j_idx)-1):
                count += (j_idx[i+1]-j_idx[i]-1)
    print(count)
solution()