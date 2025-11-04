import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    # a+b = d-c
    candidates = set(arr[i]+arr[j] for i in range(n) for j in range(n))
    # 가장 큰 d를 찾기 위해 arr 정렬
    arr.sort()
    for d in range(n-1, -1, -1):
        d_num = arr[d]
        for c in range(n):
            c_num = arr[c]
            if d_num-c_num in candidates:
                print(d_num)
                return
solution()