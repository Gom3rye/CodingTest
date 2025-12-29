import sys
input = sys.stdin.readline

def solution():
    n, m, k = map(int, input().split())
    cards = sorted(map(int, input().split()))
    cheolsu = list(map(int, input().split()))

    # parent[i] = i번째 카드가 사용되었을 때 다음 후보 카드 인덱스
    parent = list(range(m + 1))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for num in cheolsu:
        # num보다 큰 카드의 최소 인덱스
        left, right = 0, m
        while left < right:
            mid = (left + right) // 2
            if cards[mid] > num:
                right = mid
            else:
                left = mid + 1

        idx = find(left)
        print(cards[idx])

        # 카드 사용 처리
        parent[idx] = idx + 1

solution()
