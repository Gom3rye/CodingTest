import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 기둥의 개수 <=1000
    pillars = [list(map(int, input().split())) for _ in range(n)]
    pillars.sort()
    # 최대 기둥을 기준으로 왼쪽 오른쪽 나누기 + 최대 기둥 1개 만큼의 사이즈 더해주기
    max_height = -1
    max_idx = -1
    for i in range(n):
        if max_height <= pillars[i][1]:
            max_height = pillars[i][1]
            max_idx = i # max_height가 여러 개 있을 때 제일 오른쪽에 있는 max_height의 x좌표를 구하자
    answer = 0
    left_stack = [] # 지붕이 될 (x, y) 저장
    for i in range(max_idx+1): # 0 ~ max_idx까지
        x, y = pillars[i]
        if left_stack and left_stack[-1][1] > y:
            continue
        left_stack.append((x, y))
    # print(left_stack)
    for i in range(len(left_stack)-1):
        width = left_stack[i+1][0]-left_stack[i][0]
        height = left_stack[i][1]
        answer += width*height
    # print(pillars)
    right_stack = []
    for i in range(n-1, max_idx-1, -1): # max_idx ~ n-1까지
        x, y = pillars[i]
        if right_stack and right_stack[-1][1] > y:
            continue
        right_stack.append((x, y))
    # print(right_stack)
    for i in range(len(right_stack)-1):
        width = right_stack[i][0]-right_stack[i+1][0]
        height = right_stack[i][1]
        answer += width*height
    print(answer+max_height) # max_height 한 기둥 뺀 거 더해주기
solution()