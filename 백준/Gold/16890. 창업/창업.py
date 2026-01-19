import sys
from collections import deque
input = sys.stdin.readline
def solution():
    # a의 가장 작은것과 b의 가장 큰것을 매 회차 비교해야 한다.
    a_temp = list(input().strip())
    n = len(a_temp)
    # 각자 사용할 문자 남기기
    a = deque(sorted(ch for ch in a_temp)[:(n+1)//2]) # 최대 맨 앞 (n+1)//2개만 필요하다.
    b = deque(sorted([ch for ch in input().strip()], reverse=True)[:n//2]) # 맨 앞 n//2개만 필요
    # 맨앞, 맨뒤를 표시하기 위한 포인터 생성
    left, right = 0, n-1
    answer = ['']*n
    for i in range(n):
        if i%2==0: # a차례일때
            # a의 가장 작은 수가 b의 가장 큰 수보다 작은 경우
            if b and a[0] < b[0]:
                answer[left] = a.popleft()
                left += 1
            # a의 가장 작은 수가 b의 가장 큰 수보다 크거나 같은 경우
            else:
                # a의 가장 큰수를 맨 뒤에 배치 (어차피 모든 a의 수가 b보다 작을 일은 없으므로)
                answer[right] = a.pop()
                right -= 1
        else:
            # b의 가장 큰 수가 a의 가장 작은 수보다 큰 경우
            if a and b[0] > a[0]:
                answer[left] = b.popleft()
                left += 1
            # b의 가장 큰 수가 a의 가장 작은 수보다 작거나 같은 경우
            else:
                answer[right] = b.pop() # b의 가장 작은 수를 맨 끝에 놓기
                right -=1
    print(''.join(answer))
solution()