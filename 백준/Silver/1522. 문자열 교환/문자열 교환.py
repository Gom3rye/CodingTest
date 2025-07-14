import sys
input = sys.stdin.readline
def solution():
    s = input().strip()
    n = len(s)
    k = s.count('a') # a의 개수만큼 윈도우(k)가 잡힌다.
    # window 안의 b의 개수가 최소가 되어야 한다.
    min_b = int(1e9)
    w = s[:k]
    b = w.count('b')
    min_b = min(min_b, b) # 초기화

    for start in range(1, n):
        if s[start-1] == 'b':
            b -= 1

        if s[(start+k-1)%n] == 'b':
            b += 1

        min_b = min(min_b, b)
    print(min_b)
solution()
