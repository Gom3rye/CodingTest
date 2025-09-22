from collections import Counter

def solution():
    import sys
    input = sys.stdin.readline

    target = input().strip()
    target_counter = Counter(target)

    n = int(input())
    books = []
    for _ in range(n):
        cost, title = input().split()
        cost = int(cost)
        books.append((cost, Counter(title)))

    min_cost = float('inf')

    def backtrack(index, current_counter, total_cost):
        nonlocal min_cost

        # 목표 단어를 만들 수 있는 경우 → 최소 비용 갱신
        if all(current_counter[c] >= target_counter[c] for c in target_counter):
            min_cost = min(min_cost, total_cost)
            return  # 조기 종료 가능

        if index == n:
            return  # 더 이상 선택할 책 없음

        # ① 현재 책 선택
        cost, counter = books[index]
        backtrack(index + 1, current_counter + counter, total_cost + cost)

        # ② 현재 책 선택 안 함
        backtrack(index + 1, current_counter, total_cost)

    backtrack(0, Counter(), 0)

    print(min_cost if min_cost != float('inf') else -1)
solution()