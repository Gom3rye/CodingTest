N = int(input())
hills = [int(input()) for _ in range(N)]

INF = float('inf')
answer = INF

# 가능한 최소 높이 L을 전부 시도
for L in range(0, 84):  # L + 17 <= 100
    cost = 0
    low = L
    high = L + 17
    
    for h in hills:
        if h < low:
            cost += (low - h) ** 2
        elif h > high:
            cost += (h - high) ** 2
    
    answer = min(answer, cost)

print(answer)