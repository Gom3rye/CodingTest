import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    now = list(map(int, input().split()))
    target = list(map(int, input().split()))
    # 변화량 차이를 기록하는 배열 만들기
    diff = [0]+[target[i]-now[i] for i in range(n)]
    # diff 배열을 0으로 만들기 위한 최소 횟수 구하기 -> 인접 값들의 변화량만 관찰하면 된다.
    min_cost = float('inf')
    neg, pos = 0, 0
    for i in range(1, n+1):
        # 이전 줄과의 차이 변화량 관찰
        change = diff[i]-diff[i-1]
        if change < 0:
            neg -= change # 음수니까 빼줘야 +효과
        else:
            pos += change
    # 늘리는 작업과 줄이는 작업은 서로 다른 방향, 두 작업 중 더 많이 필요한 쪽이 전체를 포괄한다.
    min_cost = max(neg, pos)
    print(min_cost)
solution()