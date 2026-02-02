import sys, math, heapq
input = sys.stdin.readline
INF = float('inf')
def solution():
    a, b = map(int, input().split()) # 도착 지점의 좌표, -10^9~10^9
    n = int(input()) # #간판 <=2000
    # 중요: 원과 원사이의 거리가 1이하면 거리(받는 스트레스)는 0이 된다.
    v = n+2 # 총 점들
    xs = [0.0]*v # x좌표들
    ys = [0.0]*v
    rs = [0.0]*v
    for i in range(1, v-1):
        x, y = map(int, input().split())
        xs[i], ys[i], rs[i] = x, y, 1.0 # i번째 점의 x,y좌표, 반지름 저장(1길이만큼 볼 수 있음)
    # 끝점은 a,b,0
    xs[-1], ys[-1], rs[-1] = float(a), float(b), 0.0 # 끝점은 그냥 도착점이지 원이 아니니까 반지름 0
    q = []
    heapq.heappush(q, (0.0, 0)) # cost, start_node
    distance = [INF]*v
    distance[0] = 0.0
    while q:
        dist, now = heapq.heappop(q)
        if now == v-1: # 도착지 도달하면 종료
            break
        if dist > distance[now]:
            continue
        # 모든 조합 다돌아봐야 최소 비용 알 수 있다. (n<=2000이니까 가능)
        for nxt in range(v):
            if nxt == now:
                continue
            dx, dy = xs[now]-xs[nxt], ys[now]-ys[nxt]
            d = math.hypot(dx, dy)-(rs[now]+rs[nxt]) # math.hypot: float반환
            d = max(0.0, d) # 음수가 나오면 비용은 0이니까
            ndist = dist+d
            if ndist < distance[nxt]:
                distance[nxt] = ndist
                heapq.heappush(q, (ndist, nxt))
    print(f"{distance[-1]:.10f}")
solution()