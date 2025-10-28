import sys
input = sys.stdin.readline

def is_similar(a, b):
    map_ab = {}
    map_ba = {}
    for x, y in zip(a, b):
        if x in map_ab and map_ab[x] != y:
            return False
        if y in map_ba and map_ba[y] != x:
            return False
        map_ab[x] = y
        map_ba[y] = x
    return True

def solution():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if is_similar(words[i], words[j]):
                cnt += 1
    print(cnt)

solution()
