import sys, heapq
input = sys.stdin.readline
def solution():
    n = int(input()) # #사람 <=100,000
    infos = [list(map(int, input().split())) for _ in range(n)]
    d = int(input()) # 철로의 길이 <=200,000,000
    # 답으로 가능한 선분들만 포함
    possible = []
    for h, o in infos:
        start = min(h, o)
        end = max(h, o)
        if end-start <= d:
            possible.append((start, end))
    possible.sort(key=lambda x: x[1]) # end 기준으로 정렬 (그래야 왼->오 일직선으로만 가며 검사할 수 있으니까)
    if not possible:
        print(0)
        return
    q = [] # 포함 가능한 사람들의 start
    answer = 0
    for s, e in possible:
        while q and q[0] < e-d: # heap에 있는 젤 왼쪽 부분이 d안에 포함되지 않는 경우
            heapq.heappop(q)
        heapq.heappush(q, s)
        answer = max(answer, len(q))
    print(answer)
solution()