import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # a size, b size <=1,000,000
    a = list(map(int, input().split())) # 이미 정렬 되어 있음
    b = list(map(int, input().split()))
    a_idx, b_idx = 0, 0
    answer = []
    while a_idx < n and b_idx < m:
        if a[a_idx] <= b[b_idx]:
            answer.append(a[a_idx])
            a_idx += 1
        else: # a[a_idx] > b[b_idx]:
            answer.append(b[b_idx])
            b_idx += 1
    if a_idx == n:
        answer.extend(b[b_idx:])
    elif b_idx == m:
        answer.extend(a[a_idx:])
    print(*answer)
solution()