import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    ptr = 0
    
    while ptr < len(input_data):
        n = int(input_data[ptr])
        ptr += 1
        if n == 0: break
        
        rooms = []
        for i in range(n):
            type_char = input_data[ptr]
            amount = int(input_data[ptr+1])
            ptr += 2
            
            edges = []
            while True:
                e = int(input_data[ptr])
                ptr += 1
                if e == 0: break
                edges.append(e)
            rooms.append((type_char, amount, edges))
            
        # dist[i]는 i번 방에 도달했을 때의 최대 소지금
        dist = [-1] * (n + 1)
        
        # 1번 방 초기화
        type1, amt1, _ = rooms[0]
        start_money = 0
        if type1 == 'L':
            start_money = amt1
        elif type1 == 'T':
            if amt1 > 0: # 시작부터 트롤에게 낼 돈이 없으면 불가능
                print("No")
                continue
        
        dist[1] = start_money
        queue = deque([1])
        
        possible = False
        while queue:
            curr = queue.popleft()
            curr_money = dist[curr]
            
            if curr == n:
                possible = True
                break
                
            for next_room in rooms[curr-1][2]:
                ntype, namt, _ = rooms[next_room-1]
                nmoney = curr_money
                
                if ntype == 'L':
                    nmoney = max(curr_money, namt)
                elif ntype == 'T':
                    if curr_money >= namt:
                        nmoney = curr_money - namt
                    else:
                        continue # 돈 부족으로 못 감
                
                # 기존에 이 방에 왔을 때보다 돈을 더 많이 들고 올 수 있다면 갱신
                if nmoney > dist[next_room]:
                    dist[next_room] = nmoney
                    queue.append(next_room)
                    
        print("Yes" if possible else "No")

if __name__ == "__main__":
    solve()