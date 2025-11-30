import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 플레이어 수 <= 100,000
    cards = list(map(int, input().split()))
    MAX = 1000001
    scores = [0]*(MAX+1)
    visited = [False]*(MAX+1)
    for num in cards:
        visited[num] = True
    
    for num in cards:
        for temp in range(2*num, MAX+1, num):
            if visited[temp]:
                scores[temp] -= 1
                scores[num] += 1
    print(' '.join([str(scores[num]) for num in cards]))
solution()