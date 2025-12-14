import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split()) # 원생 수 <=300,000, 조 개수 <=300,000
    heights = list(map(int, input().split()))
    if k==n:
        print(0)
        return
    # 이미 정렬된 상태니까 차이가 큰 구간들 구해서 그 구간들 먼저 잘라주면 된다.
    diff = []
    for i in range(n-1):
        diff.append(heights[i+1]-heights[i])
    diff.sort()
    # 가장 큰 k-1개의 구간 빼기
    print(sum(diff[:n-k]))
solution()