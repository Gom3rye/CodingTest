import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
light = list(map(int, input().split()))
d = deque() # 인덱스를 저장할 덱
# 윈도우 사이즈 : light[i-m+1 : i+m-1], 윈도우 길이: 2m-1
result = []
for i in range(n):
    while d and light[d[-1]] < light[i]:
        d.pop()
    d.append(i) # d는 내림차순 정리
    # 왼쪽 인덱스가 윈도우 범위에 맞는지 확인
    if d[0] < i-(2*m-2):
        d.popleft()
    # 첫 윈도우 범위만큼 i가 다 도달했을 때부터 결과에 저장
    if 2*m-2 <= i: # d[0]: 현재 윈도우에서 최댓값의 인덱스를 가지고 있다.
        result.append(light[d[0]])
print(*result)