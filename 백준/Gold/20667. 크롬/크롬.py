import sys
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split()) # 총 크롬 탭 수, 목표 cpu 사용량, 목표 메모리 할당량
    # dp[cpu][mem] = pri 로 하면 m이 최대 십만, c가 천 -> 10^8로 메모리 초과 및 시간 초과
    # -> 차원을 뒤집어서 m을 상태에서 빼고 값으로 관리하자. dp[pri][cpu] = max mem
    # O(N*P*M) DP 떠올리기, => 최소 pri를 구하는 문제 -> 중요도 합 pri가 주어졌을 때 cpu m이상, mem k이상을 만족할 수 있는가로 뒤집기
    tabs = []
    total_pri = 0
    for _ in range(n):
        cpu, mem, pri = map(int, input().split())
        total_pri += pri
        tabs.append((cpu, mem, pri))
    # 도달 불가능한 상태(-1)로 초기화 dp[pri][cpu] = max mem
    dp = [[-1]*(m+1) for _ in range(total_pri+1)]
    # 초기화
    dp[0][0] = 0
    for cpu, mem, pri in tabs:
        for p in range(total_pri, pri-1, -1):
            # 이전 상태를 순회하는 c는 0~m까지의 모든 상태를 확인해야 한다.
            for c in range(m, -1, -1):
                if dp[p-pri][c] != -1: # 도달 가능 상태라면
                    # c+cpu가 m을 넘어가면 모두 m번 인덱스에 저장
                    new_c = min(m, c+cpu)
                    # max(현재값, 이전 상태에서 탭을 추가한 값)
                    dp[p][new_c] = max(dp[p][new_c], dp[p-pri][c]+mem)

    ans = float('inf')
    for p in range(total_pri+1):
        if dp[p][m] >= k:
            ans = p
            break # 최소 p를 찾았으므로 즉시 종료

    print(ans if ans != float('inf') else -1)           
solution()