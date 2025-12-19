import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # <=1000
    cards = list(map(int, input().split()))
    original = list(range(1, n+1))
    # 2**k < n 즉, k는 최대 9 -> 브루트포스
    def shuffle(deck, k):
        # 1번째 단계
        length = 2**k
        deck = deck[-length:]+deck[:-length]
        # 2~ 번째 단계
        for i in range(2, k+2):
            t = 2**(k-i+1)
            block = deck[:length]
            rest = deck[length:]
            block = block[-t:]+block[:-t]
            deck = block+rest
            length = t # 이전 단계에서 새로 올린 카드들만 다시 대상으로 삼아야 함
        return deck
    
    for k1 in range(1, 10):
        if 2**k1 >= n:
            continue
        first = shuffle(original, k1)
        for k2 in range(1, 10):
            if 2**k2 >= n:
                continue
            second = shuffle(first, k2)
            if second == cards:
                print(k1, k2)
                return
solution()