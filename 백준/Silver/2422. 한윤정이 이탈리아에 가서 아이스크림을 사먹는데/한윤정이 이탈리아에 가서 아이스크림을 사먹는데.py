import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # n: 아이스크림 종류의 수, m: 섞어먹으면 안되는 조합의 수
    cnt = 0
    forbidden = [[False]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        forbidden[a][b] = True
        forbidden[b][a] = True # 금지 관계는 서로 양방향인거 주의하기!
    # 1-23, 3-4끼리 섞어 먹으면 안된다. -> 145 235 245
    for i in range(1, n-1):
        for j in range(i+1, n):
            if forbidden[i][j]:
                continue
            for k in range(j+1, n+1):
                if forbidden[i][k]:
                    continue
                if forbidden[j][k]:
                    continue
                cnt += 1
                # print(i, j, k)
    print(cnt)
solution()