import sys
input = sys.stdin.readline
def solution():
    g = int(input()) # 찐 킬로그람 <=100,000
    # x: 현재 몸무게, y: 기억하는 몸무게
    y, x = 1, 2
    found = False
    while y < x:
        result = x**2-y**2
        if result == g:
            print(x)
            found = True
            x += 1
        elif result < g: # 차이를 더 키워야 한다.
            x += 1
        else:
            y += 1
    if not found:
        print(-1)
solution()