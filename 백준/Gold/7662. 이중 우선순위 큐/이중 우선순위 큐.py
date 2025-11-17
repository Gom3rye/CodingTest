import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
def solution():
    # q에 저장된 데이터 중 최댓값과 최솟값 출력
    t = int(input())
    for _ in range(t):
        k = int(input()) # 연산의 개수
        minq, maxq = [], [] # laxy deletion 사용
        counter = defaultdict(int)
        for _ in range(k):
            op, num = input().split()
            num = int(num)
            if op == 'I':
                counter[num] += 1
                heapq.heappush(minq, num)
                heapq.heappush(maxq, -num)
            else: # op == 'D'
                if num == -1: # 최솟값 삭제
                    # max heap에서 삭제된 값은 똑같이 삭제해주기
                    while minq and counter[minq[0]] == 0:
                        heapq.heappop(minq)
                    # 새로운 값 삭제해주기
                    if minq:
                        counter[heapq.heappop(minq)] -= 1
                else: # 최댓값 삭제 maxq에 -붙이는 거 잊지 말기!
                    while maxq and counter[-maxq[0]] == 0:
                        heapq.heappop(maxq)
                    if maxq:
                        counter[-heapq.heappop(maxq)] -= 1
        
        while minq and counter[minq[0]] == 0:
            heapq.heappop(minq)
        while maxq and counter[-maxq[0]] == 0:
            heapq.heappop(maxq)
        if not minq or not maxq:
            print('EMPTY')
        else:
            print(-maxq[0], minq[0])
solution()