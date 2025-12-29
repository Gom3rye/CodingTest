import sys
from collections import defaultdict
from collections import Counter
input = sys.stdin.readline
def solution():
    t = int(input()) # <=100
    for _ in range(t):
        w = input().strip() # len(w) <=10,000
        counter = Counter(w)
        k = int(input()) # 특정 문자가 나와야 하는 횟수
        if not any(cnt>=k for cnt in counter.values()):
            print(-1)
            continue
        n = len(w)
        # 문자열 하나를 통째로 보지 말고 문자의 출연 '지점'을 보자!
        char_dict = defaultdict(list)
        for i in range(n):
            char = w[i]
            char_dict[char].append(i)
        # len(char_dict[char]) >= k: 인 경우만 보기
        min_length = float('inf') # 3번 문제
        max_length = 0 # 4번 문제
        for char in char_dict: # <=26
            size = len(char_dict[char])
            if size >= k:
                spots = char_dict[char]
                start = 0
                end = start+k-1
                while end < size: # 2<5
                    length = spots[end]-spots[start]+1
                    min_length = min(min_length, length)
                    max_length = max(max_length, length)
                    start += 1
                    end += 1
        print(min_length, max_length)
solution()
