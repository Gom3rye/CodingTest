def solution():
    import sys
    input = sys.stdin.readline

    N = int(input())
    x = list(map(int, input().split()))

    left = 0
    right = N - 1
    max_team = 0

    while left < right:
        # 사이에 있는 개발자 수 = right - left - 1
        team_power = (right - left - 1) * min(x[left], x[right])
        max_team = max(max_team, team_power)

        # 능력치가 작은 쪽 포인터를 움직여야 min()이 커질 가능성이 있음
        if x[left] < x[right]:
            left += 1
        else:
            right -= 1

    print(max_team)
solution()