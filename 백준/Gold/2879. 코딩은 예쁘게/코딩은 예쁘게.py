import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    now = list(map(int, input().split()))
    target = list(map(int, input().split()))
    # 변화량 차이를 기록하는 배열 만들기
    diff = [0]+[target[i]-now[i] for i in range(n)]+[0]
    # diff 배열을 0으로 만들기 위한 최소 횟수 구하기 -> 인접 값들의 변화량만 관찰하면 된다.
    min_cost = 0
    nd = len(diff)
    for i in range(1, nd):
        change = diff[i]-diff[i-1]
        if change > 0:
            # 변화가 발생했다는 거니까 횟수에 추가해야 한다.
            min_cost += change
    print(min_cost)
solution()