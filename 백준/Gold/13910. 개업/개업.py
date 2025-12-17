import sys
from collections import deque
input = sys.stdin.readline
def solution():
    # 최소 횟수로 요리해서 모든 주문 처리하기
    n, m = map(int, input().split()) # #짜장면 <=10,000, #웍 <=100
    woks = list(map(int, input().split())) # 웍의 크기
    possible = set() # 한 번에 만들 수 있는 그릇 수
    for wok in woks:
        possible.add(wok)
    for i in range(m): # 양손을 써서 한 번에 만들 수 있는 그릇 수
        for j in range(i+1, m):
            possible.add(woks[i]+woks[j])
    q = deque([0]) # 만든 그릇 수
    count = [-1]*(n+1) # 요리한 횟수
    count[0] = 0 # 0그릇을 만들기 위해 0번 요리
    while q:
        dish = q.popleft()
        if dish == n:
            print(count[dish])
            return
        
        for dishes in possible:
            ndishes = dish+dishes
            if ndishes <= n and count[ndishes] == -1:
                count[ndishes] = count[dish]+1
                q.append(ndishes)
        
    print(-1) # 모든 주문 처리할 수 없는 경우
solution()