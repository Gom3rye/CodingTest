import sys, heapq
input = sys.stdin.readline
def solution():
    n = int(input()) # 연산의 개수
    # 자연수: 값 추가, 0: min값 출력하고 배열에서 제거
    operations = [int(input()) for _ in range(n)]
    q = []
    for operation in operations:
        if operation == 0:
            if q: # 뭐라도 있으면
                print(heapq.heappop(q))
            else:
                print(0)
        else:
            heapq.heappush(q, operation)
solution()