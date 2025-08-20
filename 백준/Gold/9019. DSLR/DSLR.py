import sys
from collections import deque
input = sys.stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        
        # A에서 B로 가는 정방향 탐색
        q_A = deque([A])
        # visited_A[i]: A에서 i까지 가는 경로
        visited_A = {A: ""} 
        
        # B에서 A로 가는 역방향 탐색
        q_B = deque([B])
        # visited_B[i]: B에서 i까지 가는 경로
        visited_B = {B: ""}

        # 너비를 1씩 늘려가며 탐색
        while q_A and q_B:
            # --- 정방향 탐색 1 레벨 진행 ---
            # 현재 레벨의 모든 노드에 대해 탐색
            for _ in range(len(q_A)):
                now = q_A.popleft()
                
                # 역방향 탐색이 이미 방문한 곳을 만났다면, 경로를 찾은 것!
                if now in visited_B:
                    print(visited_A[now] + "".join(reversed(visited_B[now])))
                    break
                
                # D, S, L, R 명령어 적용
                # D
                nxt = (now * 2) % 10000
                if nxt not in visited_A:
                    visited_A[nxt] = visited_A[now] + "D"
                    q_A.append(nxt)
                # S
                nxt = (now - 1) if now != 0 else 9999
                if nxt not in visited_A:
                    visited_A[nxt] = visited_A[now] + "S"
                    q_A.append(nxt)
                # L
                nxt = (now % 1000) * 10 + (now // 1000)
                if nxt not in visited_A:
                    visited_A[nxt] = visited_A[now] + "L"
                    q_A.append(nxt)
                # R
                nxt = (now % 10) * 1000 + (now // 10)
                if nxt not in visited_A:
                    visited_A[nxt] = visited_A[now] + "R"
                    q_A.append(nxt)
            else: # for문이 break 없이 끝나면 계속 진행
                # --- 역방향 탐색 1 레벨 진행 ---
                for _ in range(len(q_B)):
                    now = q_B.popleft()
                    
                    if now in visited_A:
                        print(visited_A[now] + "".join(reversed(visited_B[now])))
                        break

                    # 역방향 명령어 적용 (D, S, L, R의 역연산)
                    # S의 역연산 (+1)
                    nxt = (now + 1) % 10000
                    if nxt not in visited_B:
                        visited_B[nxt] = visited_B[now] + "S"
                        q_B.append(nxt)
                    # L의 역연산 (R)
                    nxt = (now % 10) * 1000 + (now // 10)
                    if nxt not in visited_B:
                        visited_B[nxt] = visited_B[now] + "L"
                        q_B.append(nxt)
                    # R의 역연산 (L)
                    nxt = (now % 1000) * 10 + (now // 1000)
                    if nxt not in visited_B:
                        visited_B[nxt] = visited_B[now] + "R"
                        q_B.append(nxt)
                    # D의 역연산 (/2) - 두 가지 가능성이 있음
                    if now % 2 == 0:
                        nxt1 = now // 2
                        if nxt1 not in visited_B:
                            visited_B[nxt1] = visited_B[now] + "D"
                            q_B.append(nxt1)
                        nxt2 = (now + 10000) // 2
                        if nxt2 not in visited_B:
                            visited_B[nxt2] = visited_B[now] + "D"
                            q_B.append(nxt2)
                else:
                    continue # 안쪽 for문이 break 없이 끝나면 계속
                break # 안쪽 for문이 break로 끝나면 바깥 while도 종료
            break # 바깥 for문이 break로 끝나면 바깥 while도 종료

solution()