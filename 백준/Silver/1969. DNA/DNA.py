import sys
from collections import defaultdict
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # dna 수, 문자열의 길이
    dnas = [input().strip() for _ in range(n)]
    answer = []
    for j in range(m):
        count = defaultdict(int) # 기본으로 0값
        for i in range(n):
            count[dnas[i][j]] += 1
        # 가장 많이 나온 알파벳 채택(동점이면 사전순으로 가장 앞서는 것)
        max_cnt = -1
        result_alpha = 'Z'
        for alpha, cnt in count.items():
            if cnt > max_cnt:
                max_cnt = cnt
                result_alpha = alpha
            elif cnt == max_cnt and result_alpha > alpha:
                result_alpha = alpha # 사전 순 정렬
        answer.append(result_alpha)
    
    hamming_distance = 0
    for j in range(m):
        d = 0
        for i in range(n):
            if dnas[i][j] != answer[j]:
                d += 1
        hamming_distance += d
    print(''.join(answer))
    print(hamming_distance)
solution()