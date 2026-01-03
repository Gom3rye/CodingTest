import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #사람 <=10
    # cnt[i]: 키가 i+1인 사람이 기억한 자기보다 큰 사람이 왼쪽에 있는 횟수
    cnt = list(map(int, input().split()))
    # 키가 큰 사람부터 줄을 세우면 이미 서 있는 사람들은 전부 나보다 키가 큰 사람들이다.
    answer = []
    for height in range(n, 0, -1):
        answer.insert(cnt[height-1], height)
    print(*answer)
solution()