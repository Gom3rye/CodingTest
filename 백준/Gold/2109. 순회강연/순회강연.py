import sys, heapq
input = sys.stdin.readline
def solution():
    n = int(input()) # #대학 <=10000
    infos = [list(map(int, input().split())) for _ in range(n)]
    # 강연이 몇일에 걸쳐있는게 아니라 그날그날의 선택 문제이므로 그리디
    # 2일차에 2개의 일이 주어졌다면 1일차에 하나를 하고 2일차에 마지막 하나를 하는 등 기한보다 더 빨리 일을 끝낼 수 있다는 걸 주의하기!
    infos.sort(key=lambda x: x[1])
    q = []
    for pay, deadline in infos:
        if len(q) >= deadline:
            heapq.heappush(q, pay)
            heapq.heappop(q) # 가장 작은 거 하나 빼기
        else:
            heapq.heappush(q, pay)
    print(sum(q))
solution()