import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # a size, b size <=1,000,000
    a = list(map(int, input().split())) # 이미 정렬 되어 있음
    b = list(map(int, input().split()))
    a_idx, b_idx = 0, 0
    answer = [0]*(n+m)
    for i in range(n+m):
        if a[a_idx] <= b[b_idx]:
            answer[i] = a[a_idx]
            a_idx += 1
            if a_idx == n:
                answer[i+1:] = b[b_idx:]
                break
        else: # a[a_idx] > b[b_idx]:
            answer[i] = b[b_idx]
            b_idx += 1
            if b_idx == m:
                answer[i+1:] = a[a_idx:]
                break
    print(*answer)
solution()