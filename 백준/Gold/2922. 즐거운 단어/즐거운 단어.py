import sys
sys.setrecursionlimit(10000)

word = input().strip()
vowels = {'A', 'E', 'I', 'O', 'U'}

# 수동 캐시
dp = {}

def dfs(idx, v_count, c_count, has_L):
    if v_count >= 3 or c_count >= 3:
        return 0
    if idx == len(word):
        return 1 if has_L else 0

    key = (idx, v_count, c_count, has_L)
    if key in dp:
        return dp[key]

    total = 0
    ch = word[idx]

    if ch == '_':
        # 모음 5개
        total += dfs(idx+1, v_count+1, 0, has_L) * 5
        # 자음 20개 (L 제외)
        total += dfs(idx+1, 0, c_count+1, has_L) * 20
        # 자음 'L' (따로 처리해서 has_L = True)
        total += dfs(idx+1, 0, c_count+1, True) * 1
    else:
        if ch in vowels:
            total += dfs(idx+1, v_count+1, 0, has_L)
        else:
            total += dfs(idx+1, 0, c_count+1, has_L or ch == 'L')

    dp[key] = total
    return total

print(dfs(0, 0, 0, False))
