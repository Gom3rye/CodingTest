def solution():
    import sys
    input = sys.stdin.readline

    # 알파벳 개수 세기 (A~Z → 0~25)
    def str_to_count_array(s):
        arr = [0] * 26
        for c in s:
            arr[ord(c) - ord('A')] += 1
        return arr

    target = input().strip()
    target_count = str_to_count_array(target)

    n = int(input())
    books = []
    for _ in range(n):
        cost, title = input().split()
        cost = int(cost)
        books.append((cost, str_to_count_array(title)))

    min_cost = float('inf')
    memo = dict()

    def can_make(current):
        for i in range(26):
            if current[i] < target_count[i]:
                return False
        return True

    def backtrack(idx, curr_count, total_cost):
        nonlocal min_cost

        # 조기 종료 1: 이미 최소 비용 넘으면 가지치기
        if total_cost >= min_cost:
            return

        # 조기 종료 2: 단어 만들 수 있다면 최소 비용 갱신
        if can_make(curr_count):
            min_cost = total_cost
            return

        # 끝까지 탐색한 경우
        if idx == n:
            return

        key = (idx, tuple(curr_count))
        if key in memo and memo[key] <= total_cost:
            return
        memo[key] = total_cost

        # ① 현재 책 선택 O
        next_count = [curr_count[i] + books[idx][1][i] for i in range(26)]
        backtrack(idx + 1, next_count, total_cost + books[idx][0])

        # ② 현재 책 선택 X
        backtrack(idx + 1, curr_count, total_cost)

    backtrack(0, [0] * 26, 0)

    print(min_cost if min_cost != float('inf') else -1)
solution()