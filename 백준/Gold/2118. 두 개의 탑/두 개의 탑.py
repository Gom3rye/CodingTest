import sys
input = sys.stdin.read

def solve():
    data = input().split()
    N = int(data[0])
    distances = list(map(int, data[1:]))

    # 누적합 계산
    prefix = [0] * (2 * N + 1)  # 두 배로 만들기 위한 누적합 배열
    for i in range(2 * N):
        prefix[i + 1] = prefix[i] + distances[i % N]

    total = prefix[N]  # 전체 거리
    max_dist = 0
    j = 0

    # 투 포인터 사용
    for i in range(N):
        # j는 i보다 오른쪽에 있는 인덱스
        while j < i + N and prefix[j + 1] - prefix[i] <= total // 2:
            j += 1
        # 최대 거리 갱신
        max_dist = max(max_dist, prefix[j] - prefix[i])

    print(max_dist)

solve()
