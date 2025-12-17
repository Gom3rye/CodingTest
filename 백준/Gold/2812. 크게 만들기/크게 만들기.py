import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    s = input().strip() # 수를 문자열로 받기
    stack = []
    for num in s:
        while stack and stack[-1]<num and k>0:
            stack.pop()
            k -= 1
        stack.append(num)
    # 끝까지 갔는데 k가 남은 경우
    if k > 0:
        stack = stack[:-k] # 뒤에서 k개만큼 제거
    print("".join(stack))
solution()