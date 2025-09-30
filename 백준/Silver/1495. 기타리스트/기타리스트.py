import sys
input = sys.stdin.readline
def solution():
    n, s, m = map(int, input().split()) # 곡 수, 시작 볼륨, 최대 볼륨
    v = list(map(int, input().split()))
    dp = {s}
    for vol in v:
        nxt_dp = set()
        for volume in dp:
            up = volume+vol
            down = volume-vol
            if 0<=up<=m:
                nxt_dp.add(up)
            if 0<=down<=m:
                nxt_dp.add(down)
        dp = nxt_dp
    if dp:
        print(max(dp))
    else:
        print(-1)
solution()