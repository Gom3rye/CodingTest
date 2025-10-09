import sys
from collections import defaultdict
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # dna 수, 문자열의 길이
    dnas = [input().strip() for _ in range(n)]
    answer = []
    hamming_distance = 0
    for j in range(m):
        count = defaultdict(int) # 기본으로 0값
        for i in range(n):
            count[dnas[i][j]] += 1
        max_char = max(count, key=lambda x: (count[x], -ord(x))) # ord: 문자->숫자 (사전 순으로 정렬하기 위해서 -붙여주기)
        hamming_distance += (n - count[max_char])
        # 또는 hamming_distance += sum(count[x] for x in count if x != max_char)
        answer.append(max_char)
    print("".join(answer))
    print(hamming_distance)
solution()