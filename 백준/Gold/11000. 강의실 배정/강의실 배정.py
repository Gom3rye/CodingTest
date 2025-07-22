import sys, heapq
input = sys.stdin.readline
def solution():
    n = int(input())
    classes = [list(map(int, input().split())) for _ in range(n)]
    q = []
    classes.sort() # 시작 시간 기준 정렬해야 수업 순서가 꼬이지 않는다.
    # 끝나는 시간을 우선순위 큐에 넣으면서 관리
    for start, end in classes:
        # 한 강의실로 곂칠 수 있으면 빼기
        if q and q[0] <= start: 
            heapq.heappop(q)
        # 일단 다 넣으면서
        heapq.heappush(q, end)
    print(len(q))
solution()