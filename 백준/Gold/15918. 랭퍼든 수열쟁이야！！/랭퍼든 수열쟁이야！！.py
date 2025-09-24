import sys
input = sys.stdin.readline
def solution():
    n, x, y = map(int, input().split())
    x, y = x-1, y-1 # 0based index로 바꿔주기
    result = [-1]*2*n # 방문 처리도 함께 (ex, -1이면 미방문)
    used = [False]*(n+1) # (1~n까지의 숫자 중)쓸 수 있는 숫자인지 판별
    count = 0
    # result[x]==result[y]라는 조건이 있으므로 result[x]=result[y]=y-x-1 이어야 한다.
    # 모든 순열을 다 구한 후 조건 탐색해보는 것은 비효율적
    # 미리 조건을 최대한 맞춰놓고 시작하자.
    result[x] = result[y] = y-x-1
    used[y-x-1] = True
    def backtracking(idx):
        nonlocal count
        if idx == 2*n:
            count += 1
            return
        
        # 해당 칸에 이미 숫자가 배정되어 있는 경우
        if result[idx] != -1:
            backtracking(idx+1)
            return
        
        # 아직 숫자가 배정되지 않은 칸인 경우
        for num in range(1, n+1):
            now, pair = idx, idx+num+1
            if not used[num] and pair < 2*n and result[pair] == -1:
                used[num] = True
                result[now] = result[pair] = num
                backtracking(idx+1)
                used[num] = False
                result[now] = result[pair] = -1

    backtracking(0)
    print(count)
solution()