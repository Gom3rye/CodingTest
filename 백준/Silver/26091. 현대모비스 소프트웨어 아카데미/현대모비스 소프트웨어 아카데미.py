import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 학회원 수<=100,000, 최소 능력치<=10^9
    powers = sorted(map(int, input().split()))
    # 견학 보낼 수 있는 최대 팀 수 출력 (팀원은 두 명, 팀의 능력치가 m이상)
    # greedy + two pointer (최대 팀을 만드려면 제일 작은 거+큰거로 해야 하고 n이 크니까 two pointer)
    # 3 3 5 5 6 7
    start, end = 0, n-1
    cnt = 0
    while start < end:
        if powers[start] + powers[end] >= m:
            cnt += 1
            start += 1
            end -= 1
        else: # powers[start] + powers[end] < m:
            start += 1
    print(cnt)
solution()