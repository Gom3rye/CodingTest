import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # <=100,000
    height = [int(input()) for _ in range(n)]+[0] # 끝의 좌표도 계산에 포함하기 위해 0추가
    stack = []
    # 높이와 너비를 알아야 넓이를 구할 수 있고 이를 위해 인덱스를 stack에 저장해야 한다.
    max_size = 0
    for i in range(n+1):
        while stack and height[stack[-1]] > height[i]:
            h = height[stack.pop()]
            if stack:
                w = i-stack[-1]-1 # 현재 i의 길이 막대는 포함하면 안되니까 -1
            else:
                w = i
            max_size = max(max_size, w*h)
        stack.append(i)
    print(max_size)
solution()
