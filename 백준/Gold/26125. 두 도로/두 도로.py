import sys
input = sys.stdin.readline
INF = float('inf')
def solution():
    n, m, s, t = map(int, input().split()) # #교차로 <=300, #도로 <=3000, 집 교차로 번호, 회사 교차로 번호 <=n
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        # 동일한 경로에 더 짧은 도로가 들어올 수 있으므로 min처리 필수!
        graph[a][b] = min(graph[a][b], c)
    q = int(input()) # <=100,000
    for i in range(1, n+1):
        graph[i][i] = 0
    def floyd():
        for k in range(1, n+1):
            for a in range(1, n+1):
                for b in range(1, n+1):
                    graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
    floyd()
    # 간선이 2개만 추가되는 상황이므로 추가된 간선에 따라 최단 경로가 될 수 있는 경우의 수를 모두 체크하자.
    # 전체 floyd 다 돌리면 q가 최대 100,000으로 시간초과
    answer = []
    for _ in range(q):
        a1, b1, c1, a2, b2, c2 = map(int, input().split())
        # 출발과 도착이 같은 경우도 있다고 했으니 이때 거리가 0으로 잘 들어가게 해야 한다.
        if a1==b1:
            c1 = 0
        elif a2==b2:
            c2 = 0
        # 나올 수 있는 최단 거리 경우의 수
        # 1. 새 도로 없이 기존으로 가는 경우
        origin = graph[s][t]
        # 2. 1도로만 쓰는 경우
        one = graph[s][a1]+c1+graph[b1][t]
        # 3. 2도로만 쓰는 경우
        two = graph[s][a2]+c2+graph[b2][t]
        # 4. 1,2도로 다 쓰되, 1->2순서인 경우
        one_two = graph[s][a1]+c1+graph[b1][a2]+c2+graph[b2][t]
        # 5. 1,2도로 다 쓰되, 2->1순서인 경우
        two_one = graph[s][a2]+c2+graph[b2][a1]+c1+graph[b1][t]
        ans = min(origin,one,two,one_two,two_one)
        answer.append(ans if ans < INF else -1) # for문 안에서 출력해버리면 q가 최대 십만이기 때문에 시간 많이 느려질 수 있다.
    print('\n'.join(map(str, answer)))
solution()