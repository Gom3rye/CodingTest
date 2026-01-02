import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #건물 <=100,000
    height = list(map(int, input().split())) # 0based index
    # 왼쪽이나 오른쪽에서 “내보다 높고, 중간에 나보다 낮거나 같은 건물로 가려지지 않은 건물들” -> 높이가 감소하지 않는 단소스택구조
    stack = [] # 단, 건물의 높이뿐만 아니라 위치도 중요하므로 (높이, 위치)로 초기화하자.
    # 한 건물을 기준으로 왼쪽 오른쪽을 보면 O(n^2)이니까 왼쪽, 오른쪽의 수 배열과 가장 가까운 번호를 저장해놓는 배열을 만들어서 O(n)으로 끝내야 한다.
    left_cnt, right_cnt = [0]*n, [0]*n
    left_nearest, right_nearest = [-1]*n, [-1]*n
    # 왼쪽 방면
    for i in range(n):
        # stack에는 본인보다 큰 건물의 높이와 위치를 저장
        while stack and stack[-1][0] <= height[i]:
            stack.pop()

        if stack:
            left_cnt[i] = len(stack)
            left_nearest[i] = stack[-1][1]
        
        stack.append((height[i], i))
    # 오른쪽 방면
    stack = []
    for i in range(n-1, -1, -1):
        while stack and stack[-1][0] <= height[i]:
            stack.pop()

        if stack:
            right_cnt[i] = len(stack)
            right_nearest[i] = stack[-1][1]
        
        stack.append((height[i], i))
    # 이제 각 배열을 기준으로 결과 출력
    # 가장 가까운 건물 중, 작은 번호를 출력
    for i in range(n):
        total = left_cnt[i]+right_cnt[i]
        if total == 0:
            print(total)
            continue
        candidates = []
        if left_nearest[i] != -1:
            candidates.append(left_nearest[i])
        if right_nearest[i] != -1:
            candidates.append(right_nearest[i])
        nearest = min(candidates, key=lambda x: (abs(i-x), x)) # 여기서 i는 closure 개념!
        print(total, nearest+1)
solution()