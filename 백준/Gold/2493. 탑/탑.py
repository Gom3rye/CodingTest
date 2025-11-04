import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    heights = list(map(int, input().split()))
    answer = [0]*n
    stack = [] # stack[i] = (높이, idx)
    # 핵심: 나보다 왼쪽에 있으면서 나보다 낮은 애들은 버려도 된다. (앞으로 레이저 수신 절대 못하니까)
    # 가장 최근에 추가한 놈(가장 가까운 놈)을 가장 먼저 검사해야 하기 때문에 stack 쓰자!!
    # 한 방향으로 탐색하며 나보다 크면서/작으면서 가장 가까운 원소를 찾아야 할 때 -> stack
    for i in range(n):
        height = heights[i]
        # 스택이 비어있지 않고, top이 나보다 낮으면 "쓸모 없으므로" pop
        while stack and stack[-1][0] < height:
            stack.pop()
        # while이 끝났을 때 스택에 누군가 있으면 그게 나보다 크면서 가장 가까운 타워
        if stack:
            answer[i] = stack[-1][1]
        # else: result[i] = 0 (초기값)
        stack.append((height, i+1)) # (높이와 1based 인덱스)
    print(*answer)
solution()