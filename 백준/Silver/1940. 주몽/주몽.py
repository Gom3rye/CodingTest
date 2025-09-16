import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 재료의 개수
    m = int(input()) # 값옷을 만드는데 필요한 수
    materials = sorted(map(int, input().split()))
    start, end, cnt = 0, n-1, 0
    while start < end:
        armor = materials[start] + materials[end]
        if armor < m:
            start += 1
        elif armor > m:
            end -= 1
        else: # armor == m
            cnt += 1
            start += 1
    print(cnt)
solution()