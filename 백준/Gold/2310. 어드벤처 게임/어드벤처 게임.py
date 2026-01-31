import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    while True:
        n = int(input()) # #방 <=1000
        if n == 0:
            break
        # 필요한 변수: 방이름, 요구하는 금액, 이동 가능 방번호
        # 이음새=> 인덱스! 몇 번째 방이고 그 방에 대한 정보를 인덱스로 관리할 수 있다!
        rooms = []
        for i in range(n):
            data = list(input().split()[:-1])
            room = data[0]
            money = int(data[1])
            adj = [int(r)-1 for r in data[2:]] # 0based index
            rooms.append((room, money, adj))

        visited = [False]*n
        visited[0] = True
        def dfs(idx, coin):
            room, money, adj = rooms[idx]
            
            if room == 'L':
                ncoin = max(money, coin)
            elif room == 'T':
                if coin < money:
                    return False # 이 방에서 출발하면 안됨
                ncoin = coin-money
            else:
                ncoin = coin # E방이면 코인 변화 없음
            
            # n-1번방에 도착하면 성공
            if idx == n-1:
                return True
            
            for nxt in adj:
                if not visited[nxt]:
                    visited[nxt] = True
                    if dfs(nxt, ncoin):
                        return True
                    visited[nxt] = False

            return False

        # 0번방에 들어가기 전에 0원을 가지고 있다.  
        if dfs(0, 0): # dfs는 ‘방에 들어가기 직전 상태’를 인자로 받기 때문에 시작을 항상 (1, 0)으로 해도 첫 방의 효과가 자동으로 반영된다.
            print("Yes")
        else:
            print("No")
solution()