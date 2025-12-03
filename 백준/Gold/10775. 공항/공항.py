import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    # 비행기를 최대 몇 대 도킹 가능?
    g = int(input()) # 게이트 수 <=10^5
    p = int(input()) # 비행기 수 <=10^5 -> O(n^2)는 시간초과
    # 게이트 도킹 문제 -> union-find(서로소 집합)로 접프하기
    parents = list(range(g+1))
    def find(x): # x이하의 사용가능한 가장 큰 게이트 찾기
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    cnt = 0
    for _ in range(p):
        gate = int(input())
        docking = find(gate) # gate를 요구하는 비행기의 최종 할당 위치 찾기
        if docking == 0: # 더 이상 도킹할 곳 없음
            break
        cnt += 1
        # find(docking)의 대표를 docking-1로 변경
        parents[docking] = docking-1 # docking 게이트를 사용했으므로 docking-1로 연결
    print(cnt)
solution()