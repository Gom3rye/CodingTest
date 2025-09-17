import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)  # 백트래킹 깊이를 위해

def is_good(seq):
    length = len(seq)
    for i in range(1, length // 2 + 1):
        if seq[-i:] == seq[-2*i:-i]:
            return False
    return True

def dfs(seq, n):
    if len(seq) == n:
        print(seq)
        sys.exit(0)  # 가장 처음 찾은 수열이 가장 작으므로 바로 종료

    for num in '123':  # 사전순으로 1, 2, 3
        new_seq = seq + num
        if is_good(new_seq):
            dfs(new_seq, n)

def solution():
    n = int(input())
    dfs('', n)

solution()