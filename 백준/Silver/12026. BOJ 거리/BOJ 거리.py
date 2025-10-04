import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    s = input().strip()
    dp = [float('inf')]*n # dp[i]: i번째 블럭을 갔을 때의 드는 최소 에너지
    dp[0] = 0
    rule = {"B":0, "O":1, "J":2}
    for i in range(1, n): # i칸까지 오는 최소 비용 dp[i] 구하기
        for j in range(i): # 이전에 도달 가능한 칸들 j에서 i로 점프할 수 있는지 확인하고 가능하면 dp[i] 업데이트
            if (rule[s[j]]+1) % 3 != rule[s[i]]:
                continue
            dp[i] = min(dp[i], dp[j]+(i-j)**2)
    print(dp[-1] if dp[-1] != float('inf') else -1)
solution()