import sys
input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()
bl = len(bomb)

stack = []

for ch in s:
    stack.append(ch)
    
    # 스택의 뒤에서 bomb와 비교
    if len(stack) >= bl:
        if ''.join(stack[-bl:]) == bomb:
            # 폭발
            del stack[-bl:]

# 출력
if stack:
    print(''.join(stack))
else:
    print("FRULA")
