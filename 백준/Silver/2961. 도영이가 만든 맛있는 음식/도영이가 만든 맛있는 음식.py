import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def solution():
    n = int(input())
    min_d = float('inf') # 가장 작은 차이
    sours = [0]*n
    bitters = [0]*n
    for i in range(n):
        sv, bv = map(int, input().split())
        sours[i], bitters[i] = sv, bv
    def backtracking(s_idx, c, sour, bitter):
        nonlocal min_d
        if c == count:
            diff = abs(sour-bitter)
            min_d = min(min_d, diff)
            return
        for i in range(s_idx, n):
            sour *= sours[i]
            bitter += bitters[i]
            backtracking(i+1, c+1, sour, bitter)
            sour //= sours[i]
            bitter -= bitters[i]

    # 1~n개의 조합을 선택해서 최적의 해를 구하기
    for i in range(n):
        count = i+1 # 재료를 고르는 횟수
        sour, bitter = 1, 0
        backtracking(0, 0, sour, bitter)
    print(min_d)
solution()