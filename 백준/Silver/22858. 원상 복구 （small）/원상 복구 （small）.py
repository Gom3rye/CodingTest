import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    s = [0]+list(map(int, input().split())) # k번 셔플된 결과
    d = [0]+list(map(int, input().split())) # 셔플규칙
    p = [0]*(n+1) # 우리가 구해야 하는 것
    for _ in range(k):
        for i in range(1, n+1):
            p[d[i]] = s[i]
        s = p[:]
    print(*p[1:])
    # p[d[i]]를 s[i]로
    # 원래 카드 배치는?
solution()