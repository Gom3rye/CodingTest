from collections import deque

def solution():
    N, K = map(int, input().split())
    A = deque(map(int, input().split()))  # 내구도 배열 (벨트)
    robots = deque([False] * N)           # 로봇이 있는지 여부 (위쪽 벨트만)

    step = 0

    while True:
        step += 1

        # 1. 벨트 회전 (A도, 로봇도 함께 회전)
        A.rotate(1)
        robots.rotate(1)
        robots[-1] = False  # 내리는 위치에 로봇이 있으면 즉시 내려감

        # 2. 로봇 이동
        for i in range(N - 2, -1, -1):  # 먼저 올라간 로봇부터
            if robots[i] and not robots[i + 1] and A[i + 1] >= 1:
                robots[i] = False
                robots[i + 1] = True
                A[i + 1] -= 1
        robots[-1] = False  # 내리는 위치에 로봇 제거

        # 3. 로봇 올리기
        if A[0] > 0:
            robots[0] = True
            A[0] -= 1

        # 4. 내구도 0인 칸 개수 세기
        if A.count(0) >= K:
            print(step)
            return

solution()
