import sys
input = sys.stdin.readline
def solution():
    n, s = map(int, input().split()) # #커넥티드 카 <=1,000,000, # 첫 차 <=n
    x = list(map(int, input().split())) # 초기 위치 0based index
    h = list(map(int, input().split())) # 연료량 0based index
    # 연결될 가능성이 있는 커넥티드 카 전부 구해보기-> 일반 bfs나 시뮬로 하면 n이 백만이어서 시간초과, 연속된 구간을 투포인터로 탐색해야 한다.
    s -= 1 # 0based index로
    left = right = s # 시작은 [s,s]를 가리키고 있는 포인터
    # 갈 수 있는 최대, 최소의 x범위 기록
    min_x, max_x = x[s]-h[s], x[s]+h[s]
    while True:
        moved = False
        # 왼쪽 포인터 이동할 수 있는지 확인(누적 갱신))
        while left > 0 and x[left-1] >= min_x: # 먼저 left-1이 가능한지 체크하고
            left -= 1 # 가능하면 while문 안으로 들어와서 -1 해주기
            min_x = min(min_x, x[left]-h[left])
            max_x = max(max_x, x[left]+h[left])
            moved = True
        # 오른쪽 포인터 이동할 수 있는지 확인
        while right < n-1 and x[right+1] <= max_x:
            right += 1
            min_x = min(min_x, x[right]-h[right])
            max_x = max(max_x, x[right]+h[right])
            moved = True
        if not moved:
            break
    print(*range(left+1, right+2))
solution()