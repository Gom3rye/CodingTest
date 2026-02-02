import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split()) # <=1,000,000, 100,000
    arr = list(map(int, input().split()))
    # 연속한 부분 수열 -> 투 포인터 사용!
    start, cnt, max_length = 0, 0, 0
    # 한 칸씩 전진하며 탐색해야 하기 때문에 for문 사용
    for end in range(n):
        # 홀수인 경우 개수 +1
        if arr[end]%2 != 0:
            cnt += 1
        # cnt가 k보다 크다면 작거나 같을 때까지 start 이동
        while cnt > k:
            if arr[start]%2 == 1: # 홀수인 경우
                cnt -= 1
            start += 1
        max_length = max(max_length, end-start+1-cnt)
    print(max_length)
solution()