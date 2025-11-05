import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 나무수 <=백만, 나무길이 <=2억
    arr = list(map(int, input().split()))
    start, end = 0, max(arr)
    answer = 0
    while start <= end:
        total = 0 # 총 나무 길이
        mid = (start+end)//2
        for height in arr:
            if height > mid:
                total += (height-mid)
        
        if total >= m: # 필요한 나무 미터보다 큰 경우
            answer = mid
            start = mid+1
        elif total < m:
            end = mid-1
    print(answer)
solution()