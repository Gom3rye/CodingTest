import sys
input = sys.stdin.readline
def solution():
    # 쌓인 피로도 <=1,000,000, 처리한 양 <=10,000, 쉬었을 때 줄어든 피로도 <=10,000, 넘기면 안되는 최대 피로도 <=1,000,000
    a, b, c, m = map(int, input().split())
    fatigue = 0
    work = 0
    for _ in range(24): # 24번 반복
        # 일을 할 수 있는 경우
        if fatigue + a <= m:
            fatigue += a
            work += b
        else: # 일 못하는 경우(쉬어야 하는 경우)
            fatigue = max(fatigue-c, 0)
    print(work)
solution()