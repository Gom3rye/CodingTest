def solution(money):
    def max_money(coins):
        n = len(coins)
        if n == 2:
            return max(coins)
        dp = [0]*n
        dp[0] = coins[0]
        dp[1] = max(coins[0], coins[1])
        # 연달아서만 안 선택하면 되니까
        for i in range(2, n):
            dp[i] = max(dp[i-2]+coins[i], dp[i-1])
        return dp[-1]
        
    startfrom0 = max_money(money[:-1]) # 첫 번째 선택했으면 마지막은 선택하면 안됨
    startfrom1 = max_money(money[1:]) # 첫 번째 선택 안 했으니 두 번째 부터
    
    return max(startfrom0, startfrom1)