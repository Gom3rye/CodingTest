import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline
def solution():
    n = int(input())
    svc = list(map(int, input().split()))
    # 가장 큰 체력에 -9를 하는 게 최소 횟수가 아닐 수도 있음 -> Greedy 아님
    # 공격해야 하는 횟수의 "최솟값"을 구하기 -> bfs
    # 상태 정의: 남아 있는 scv들의 체력
    while len(svc) < 3:
        svc.append(0) # 1~3까지 가능하니까 일단 3쌍으로 만들기

    q = deque([(svc[0], svc[1], svc[2], 0)]) # 3쌍의 남은 체려과 공격 횟수
    # (1,3,9)와 (3,9,1) 은 같은 경우로 봐야 하므로 sort를 해서 visited 체크해야 한다.
    # (-8,10,10)과 (0,10,10)은 같은 상태로 봐야 하므로 hp의 최솟값은 0으로 setting 해놓자. (안 그럼 불필요한 상태가 set에 저장되어 불필요한 탐색을 하게 되니까)
    visited = {tuple(sorted([svc[0], svc[1], svc[2]]))} # set((a, b, c)) -> {a, b, c} ok, not {(a, b, c)} <- 이렇게 해주려면 []로 한 번 더 감싸얗 한다. ex, set([(a, b, c)])
    damage = list(permutations([1,3,9])) # 3마리 SCV에 대한 9, 3, 1 데미지 조합 (총 3! = 6가지)
    while q:
        a, b, c, count = q.popleft()
        # damage 조합으로 체력 깍기
        for d1, d2, d3 in damage:
            na = max(0, a-d1)
            nb = max(0, b-d2)
            nc = max(0, c-d3)
            if na==0 and nb==0 and nc==0:
                print(count+1)
                return
            nxt_state = tuple(sorted([na, nb, nc]))
            if nxt_state not in visited:
                visited.add(nxt_state)
                q.append((na, nb, nc, count+1))
solution()