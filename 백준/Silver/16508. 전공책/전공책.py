import sys
from collections import Counter
input = sys.stdin.readline
def solution():
    word = input().strip()
    n = int(input())
    books = []
    min_price = float('inf')
    for _ in range(n):
        price, name = input().split()
        books.append((int(price), Counter(name)))
    needed = Counter(word)
    def backtracking(idx, price, current_counter):
        nonlocal min_price
    
        if price >= min_price: # 가지치기
            return
        
        if all(current_counter[alphabet] >= cnt for alphabet, cnt in needed.items()):
            min_price = min(min_price, price)
            return
        
        if idx == n: # 없는 경우 가지치기
            return
        # 현재 책을 고른 경우
        cost, name = books[idx]
        backtracking(idx+1, price+cost, current_counter+name)
            
        # 현재 책을 고르지 않은 경우
        backtracking(idx+1, price, current_counter)
    backtracking(0, 0, Counter()) # idx, price, current_counter
    print(min_price if min_price != float('inf') else -1)
solution()