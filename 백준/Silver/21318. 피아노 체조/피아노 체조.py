import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 악보 개수
    levels = [0]+list(map(int, input().split())) # 난이도 1based index
    q = int(input()) # 질문
    # n <= 십만으로 크므로 누적합 쓰기!
    mistakes = [0]*(n+1)
    for i in range(1, n+1):
        if levels[i] < levels[i-1]:
            mistakes[i] = 1
    prefix_sum = [0]*(n+1)
    for i in range(1, n+1): # 1based index
        prefix_sum[i] = prefix_sum[i-1]+mistakes[i]
    for _ in range(q):
        x, y = map(int, input().split())
        mistake = prefix_sum[y]-prefix_sum[x]
        print(mistake)
solution()