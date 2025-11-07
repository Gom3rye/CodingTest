import sys
from itertools import permutations
from collections import defaultdict

input = sys.stdin.readline

def solution():
    A, B, C = input().split()

    # 1. 고유 문자 추출
    unique_letters = list(set(A + B + C))
    L = len(unique_letters)

    if L > 10:
        print("NO")
        return

    # 2. "가중치(weight)" 계산 (A + B - C = 0)
    # weights['S'] = 1000, weights['E'] = 91 ...
    weights = defaultdict(int)
    
    # A (Plus)
    for i, char in enumerate(reversed(A)):
        weights[char] += (10 ** i)
        
    # B (Plus)
    for i, char in enumerate(reversed(B)):
        weights[char] += (10 ** i)
        
    # C (Minus)
    for i, char in enumerate(reversed(C)):
        weights[char] -= (10 ** i)
        
    # 3. P(10, L) 순열 탐색
    for p in permutations(range(10), L):
        
        # 4. {문자: 숫자} 매핑 생성
        mapping = dict(zip(unique_letters, p))
        
        # 5. O(L) 가중치 합 계산
        total_sum = 0
        for char in unique_letters:
            total_sum += weights[char] * mapping[char]
            
        # 6. 합이 0이면 성공
        if total_sum == 0:
            print("YES")
            return
            
    # 7. 실패
    print("NO")

solution()