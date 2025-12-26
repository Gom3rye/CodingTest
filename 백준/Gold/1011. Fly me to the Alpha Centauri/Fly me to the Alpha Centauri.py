import sys, math
input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t):
        s, e = map(int, input().split())
        # e <2^31 으로 매우 크므로 bfs로 풀기 불가능 => 규칙 찾기
        # dist: 1 2 3 4 5 6 7 8 9 10 ..
        # cnt:  1 2 3 3 4 4 5 5 5 6 ..
        # 항상 1 2 3 ... k ... 3 2 1로 돌아온다.
        # -> 이동 횟수는 2k-1, 거리 합은 k^2
        dist = e-s
        k = int(math.sqrt(dist))
        if k*k == dist:
            print(2*k-1)
        elif k*k < dist <= k*(k+1):
            print(2*k)
        else:
            print(2*k+1) 

solution()