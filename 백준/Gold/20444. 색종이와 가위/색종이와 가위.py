import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())

    # 가로 컷 횟수(h_cuts)를 0부터 n/2 까지만 탐색
    left, right = 0, n // 2
    found = False

    while left <= right:
        h_cuts = (left + right) // 2
        v_cuts = n - h_cuts
        
        pieces = (h_cuts + 1) * (v_cuts + 1)
        
        if pieces == k:
            found = True
            break
        elif pieces < k:
            left = h_cuts + 1
        else:
            right = h_cuts - 1
            
    if found:
        print("YES")
    else:
        print("NO")

solution()