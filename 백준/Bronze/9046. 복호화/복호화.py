import sys
from collections import Counter
input = sys.stdin.readline
def solution():
    t = int(input()) # test case <=20
    for _ in range(t):
        strings = input().strip().replace(" ", "") # len <=255
        counter = Counter(strings).most_common()
        max_cnt, answer, question = 0, '', False
        for char, cnt in counter:
            if cnt > max_cnt:
                answer = char
                max_cnt = cnt
            elif cnt == max_cnt:
                answer = '?'
                break
            else:
                break
        print(answer)
solution()