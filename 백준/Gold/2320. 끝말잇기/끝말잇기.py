import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #단어 <=16
    words = list(input().strip() for _ in range(n))
    # 단어의 시작과 끝, 길이만 중요!
    start = [w[0] for w in words]
    end = [w[-1] for w in words]
    length = [len(w) for w in words]
    # 길이가 긴것들부터 고른다고 해도 나중에 작은 것들을 더 이어붙일 수 있는게 결과적으로 더 클 수 있으니까 그리디 x
    # 상태가 과거 선택에 의존하기 때문에 상태 관리 dp 사용!
    dp = {} # dp[(지금까지 써온 글자, 시작 글자)] = 최대길이
    def backtracking(used_set, now):
        key = (frozenset(used_set), now)
        # memoization
        if key in dp:
            return dp[key]
        
        best = length[now]
        for nxt in range(n):
            # 이미 쓴 단어는 패쓰
            if nxt in used_set:
                continue
            if end[now] == start[nxt]:
                used_set.add(nxt)
                best = max(best, length[now]+backtracking(used_set, nxt))
                used_set.remove(nxt)
        
        dp[key] = best
        return best
    
    max_score = 0
    for i in range(n):
        max_score = max(max_score, backtracking({i}, i))
    print(max_score)
solution()