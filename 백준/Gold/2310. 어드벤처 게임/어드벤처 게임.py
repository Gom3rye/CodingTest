import sys
from collections import deque
input = sys.stdin.readline
def solution():
    while True:
        n = int(input()) # #방 <=1000
        if n == 0:
            break
        # 필요한 변수: 방이름, 요구하는 금액, 이동 가능 방번호
        # 이음새=> 인덱스! 몇 번째 방이고 그 방에 대한 정보를 인덱스로 관리할 수 있다!
        rooms = ['']*n
        money = [0]*n
        adj = [] # 0based index로
        for i in range(n):
            data = list(input().split()[:-1])
            rooms[i] = data[0]
            money[i] = int(data[1])
            adj.append([int(r)-1 for r in data[2:]]) # 0based index
        start_coin = 0
        if rooms[0] == 'L':
            start_coin = money[0]
        elif rooms[0] == 'T' and money[0] > 0:
            print("No")
            continue
        # 재방문 막기 위한 중복처리 관리: 방 번호별이 아니라 금액별! 금액이 작아도 다른 방 한 번더 가서 금액 충전해올 수 있기 때문
        q = deque([(0, start_coin)]) # 0번째 방에서 0원을 가지고 n-1방에 갈 수 있는지 없는지 탐색
        max_money = [-1]*n # 현재 coin이 max_money[방번호]보다 많을 때만 전진
        max_money[0] = start_coin
        while q:
            now, coin = q.popleft()
            if now == n-1:
                print("Yes")
                break
            for nxt in adj[now]:
                # L인 경우-> money[nxt]로 채우거나 패쓰
                if rooms[nxt] == 'L':
                    ncoin = max(coin, money[nxt])
                # T인 경우-> 빼기
                elif rooms[nxt] == 'T':
                    if coin >= money[nxt]:
                        ncoin = coin-money[nxt]
                    else:
                        continue # 이동 불가능이므로 cut
                # E인 경우-> 값 그대로
                else:
                    ncoin = coin
                # max_money 갱신
                if ncoin > max_money[nxt]:
                    max_money[nxt] = ncoin
                    q.append((nxt, ncoin))
        else:
            print("No")

solution()