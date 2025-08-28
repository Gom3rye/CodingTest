import sys
# Python의 재귀 깊이는 보통 1000이므로, N이 900이라 필수는 아닐 수 있지만
# 안전을 위해 늘려주는 것이 좋습니다.
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution():
    K, N, F = map(int, input().split())
    
    # 친구 관계를 빠르게 확인하기 위해 인접 행렬 사용
    # friends[i][j] = True 이면 i와 j는 친구
    friends = [[False] * (N + 1) for _ in range(N + 1)]
    for _ in range(F):
        a, b = map(int, input().split())
        friends[a][b] = True
        friends[b][a] = True

    # 현재까지 선발된 학생 명단
    picnic_members = []

    # 백트래킹(DFS) 함수
    # start_node: 중복된 조합을 피하기 위해, 이전에 확인한 학생보다 번호가 큰 학생만 후보로 봄
    def find_group(start_node):
        # 1. 종료 조건: K명의 학생을 모두 선발했다면 성공
        if len(picnic_members) == K:
            # 성공한 명단을 출력하고 프로그램 종료
            for member in picnic_members:
                print(member)
            sys.exit(0)

        # 2. 다음 멤버 탐색
        for next_member in range(start_node, N + 1):
            is_friend_with_all = True
            # 현재 명단에 있는 모든 학생과 친구인지 확인
            for current_member in picnic_members:
                if not friends[current_member][next_member]:
                    is_friend_with_all = False
                    break
            
            # 모든 멤버와 친구라면, 명단에 추가하고 다음 멤버를 찾으러 감
            if is_friend_with_all:
                # --- Choose (선택) ---
                picnic_members.append(next_member)
                # --- Recur (탐색) ---
                find_group(next_member + 1)
                # --- Unchoose (선택 취소, 백트래킹) ---
                # 위 재귀 호출이 끝났다는 것은, 이 경로가 실패했거나
                # 이미 답을 찾고 종료했다는 의미.
                # 다른 경로를 탐색하기 위해 마지막 멤버를 명단에서 제외.
                picnic_members.pop()

    find_group(1)
    
    # for 루프가 끝날 때까지 sys.exit(0)가 호출되지 않았다면, 답이 없는 것
    print(-1)

solution()