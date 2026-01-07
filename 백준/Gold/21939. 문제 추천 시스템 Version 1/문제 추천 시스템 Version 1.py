import sys, heapq

input = sys.stdin.readline

def solution():
    n = int(input())
    minq, maxq = [], []
    # in_list[문제번호] = 난이도 로 저장하여 현재 유효한 난이도를 관리
    in_list = {} 
    
    for _ in range(n):
        p, l = map(int, input().split())
        heapq.heappush(minq, (l, p))
        heapq.heappush(maxq, (-l, -p))
        in_list[p] = l
    
    m = int(input())
    for _ in range(m):
        command = input().split()
        
        if command[0] == 'add':
            p, l = int(command[1]), int(command[2])
            # 동일한 문제 번호가 다른 난이도로 들어올 수 있으므로 갱신
            heapq.heappush(minq, (l, p))
            heapq.heappush(maxq, (-l, -p))
            in_list[p] = l
            
        elif command[0] == 'recommend':
            if command[1] == '1':
                # maxq의 top에 있는 문제가 삭제되었거나, 난이도가 변경된 과거 데이터라면 pop
                while maxq and (abs(maxq[0][1]) not in in_list or in_list[abs(maxq[0][1])] != abs(maxq[0][0])):
                    heapq.heappop(maxq)
                print(-maxq[0][1])
            else:
                # minq의 top에 있는 문제가 삭제되었거나, 난이도가 변경된 과거 데이터라면 pop
                while minq and (minq[0][1] not in in_list or in_list[minq[0][1]] != minq[0][0]):
                    heapq.heappop(minq)
                print(minq[0][1])
                
        elif command[0] == 'solved':
            p = int(command[1])
            # dict에서 제거하여 힙의 Lazy Deletion(지연 삭제) 대상으로 만듦
            if p in in_list:
                del in_list[p]

solution()