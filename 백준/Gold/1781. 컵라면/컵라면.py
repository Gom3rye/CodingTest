import sys, heapq
input = sys.stdin.readline
def solution():
    n = int(input())
    info = [list(map(int, input().split())) for _ in range(n)]
    # 데드라인 안에서 받을 수 있는 최대 컵라면 수를 구하기
    # 데드라인 순으로 정렬 한 후 하나씩 q에 넣으면서 q 길이가 데드라인보다 길어지면 제일 작은거(q의 맨 앞에 저장되어 있음) pop하기
    info.sort()
    q = []
    for deadline, ramen in info:
        heapq.heappush(q, ramen)
        if len(q) > deadline:
            heapq.heappop(q)
    print(sum(q))
solution()