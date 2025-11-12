n = int(input())
requests = list(map(int, input().split()))
m = int(input())

left = 0
right = max(requests)
answer = 0

while left <= right:
    mid = (left + right) // 2
    total = sum(min(r, mid) for r in requests)

    if total <= m:  # 예산 총합이 M 이하면 가능
        answer = mid      # 현재 상한액 저장
        left = mid + 1    # 더 큰 상한액을 탐색
    else:
        right = mid - 1   # 예산 초과 → 상한액 줄이기

print(answer)
