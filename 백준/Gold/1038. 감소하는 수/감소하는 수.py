import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n = int(input())
    # 감소하는 수의 총 개수: 2**10-1 = 1023
    if n > 1022:
        print(-1)
        return
    if 0<=n<10:
        print(n)
        return
    count = -1
    q = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    while q:
        num = q.popleft()
        count += 1
        if count == n:
            print(num)
            return
        last_digit = num%10 # 1의 자리 수
        for next_digit in range(last_digit):
            q.append(num*10 + next_digit)
solution()