# import sys
# input = sys.stdin.readline
# def solution():
#     n, m = map(int, input().split())
#     n -= 1
#     m -= 1 # 0based index
#     board = [list(map(int, input().split())) for _ in range(n)]
#     visited = [[False]*m for _ in range(n)]
#     max_score = 0
#     boomerang = [[(0,0),(0,1),(1,0)], 
#                  [(0,0),(-1,0),(0,-1)], 
#                  [(0,0),(-1,0),(0,1)], 
#                  [(0,0),(0,-1),(1,0)]]
#     def backtracking():

# solution()
import sys

input = sys.stdin.readline

def generate_anagrams(word):
    word = sorted(word)
    used = [False] * len(word)
    result = []
    path = []

    def backtrack():
        if len(path) == len(word):
            result.append(''.join(path))
            return
        for i in range(len(word)):
            if used[i]:
                continue
            # 중복 방지: 이전 문자와 같고 이전 문자를 사용하지 않은 경우 skip
            if i > 0 and word[i] == word[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(word[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return result

n = int(input())
for _ in range(n):
    word = input().strip()
    anagrams = generate_anagrams(word)
    sys.stdout.write('\n'.join(anagrams) + '\n')
