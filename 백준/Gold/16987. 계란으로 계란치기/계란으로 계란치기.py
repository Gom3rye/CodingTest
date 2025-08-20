import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution():
    n = int(input())  # 계란 개수
    eggs = [list(map(int, input().split())) for _ in range(n)]  # 각 계란의 [내구도, 무게]
    max_count = 0  # 최대로 깰 수 있는 계란 수

    def dfs(current, count):
        nonlocal max_count

        # 모든 계란을 다 들었다면 종료 조건
        if current == n:
            max_count = max(max_count, count)
            return

        # 현재 계란이 이미 깨졌다면 칠 수 없으므로 다음 계란으로 이동
        if eggs[current][0] <= 0:
            dfs(current+1, count)
            return
            
		#매 재귀 호출마다 초기화되어야 한다.
        can_hit = False  # 칠 수 있는 계란이 있는지 확인용 플래그

        for i in range(n):
            # 자기 자신이거나, 대상 계란이 이미 깨졌다면 패스
            if i == current or eggs[i][0] <= 0:
                continue

            # 계란끼리 치기
            eggs[current][0] -= eggs[i][1]  # 현재 계란 내구도 감소 (상대 계란 무게만큼)
            eggs[i][0] -= eggs[current][1]  # 상대 계란 내구도 감소 (현재 계란 무게만큼)
            can_hit = True  # 실제로 한 번이라도 쳤다는 표시
            
            cracked = 0
            if eggs[current][0] <= 0:
                cracked += 1
            if eggs[i][0] <= 0:
                cracked += 1
            dfs(current+1, count+cracked)  # 다음 계란으로 이동

            # 백트래킹: 상태 복구
            eggs[current][0] += eggs[i][1]
            eggs[i][0] += eggs[current][1]

        # 칠 수 있는 계란이 하나도 없다면 dfs(current+1)로 넘어가야 함(다음 계란)
        if not can_hit:
            dfs(current+1, count)

    dfs(0, 0)
    print(max_count)
solution()