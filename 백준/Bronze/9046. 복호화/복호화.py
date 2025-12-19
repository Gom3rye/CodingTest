import sys
from collections import Counter
input = sys.stdin.readline
def solution():
    t = int(input()) # test case <=20
    for _ in range(t):
        strings = list(input().split())
        strings = "".join(strings) # len <=255
        counter = Counter(strings).most_common()
        # 한 문자로만 이루어졌으면 그 알파벳 출력하면 됨
        if len(counter) == 1:
            print(counter[0][0])
            continue
        answer = counter[0][0]
        max_cnt = counter[0][1]
        for char, cnt in counter[1:]:
            if cnt == max_cnt:
                print("?")
                break
            else:
                print(answer)
                break
        
solution()