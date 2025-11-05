import sys
from collections import Counter
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 나무수 <=백만, 나무길이 <=2억
    arr = list(map(int, input().split()))
    counter = Counter(arr)
    start, end = 0, max(arr)
    answer = 0
    while start <= end:
        total = 0 # 총 나무 길이
        mid = (start+end)//2
        for height, cnt in counter.items():
            if height > mid:
                total += (height-mid)*cnt
        
        if total >= m: # 필요한 나무 미터보다 큰 경우
            answer = mid # 일단 mid 결과로 저장
            start = mid+1 # 더 큰 것도 가능한지 보기
        elif total < m:
            end = mid-1
    print(answer)
solution()