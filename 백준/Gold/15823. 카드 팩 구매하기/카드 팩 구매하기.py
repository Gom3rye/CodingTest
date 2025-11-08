import sys
input = sys.stdin.readline
from collections import defaultdict

def solution():
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))

    # --- 2. is_possible(S) 함수 (O(N)) ---
    # "크기 S로 M개의 팩을 만들 수 있는가?"
    def is_possible(S):
        
        # 2-A. 전처리: is_valid[i] (i에서 끝나는 S짜리 팩이 유효한가?)
        # O(N) 슬라이딩 윈도우
        is_valid = [False] * n
        window_counts = defaultdict(int) # 윈도우 내 카드 카운트
        duplicates = 0 # 윈도우 내 중복 카드 종류 수
        start = 0
        
        for end in range(n):
            # 1. 윈도우에 'end' 카드 추가
            card_end = cards[end]
            window_counts[card_end] += 1
            if window_counts[card_end] == 2:
                duplicates += 1
                
            # 2. 윈도우 크기가 S보다 크면 'start' 카드 제거
            if end - start + 1 > S:
                card_start = cards[start]
                window_counts[card_start] -= 1
                if window_counts[card_start] == 1:
                    duplicates -= 1
                start += 1
            
            # 3. 윈도우 크기가 S이고 중복이 없으면 유효
            if end - start + 1 == S and duplicates == 0:
                is_valid[end] = True

        # 2-B. DP: dp[i] (i번째 카드까지 만들 수 있는 최대 팩 수)
        dp = [0] * (n + 1) # 1-based index
        
        for i in range(1, n + 1):
            # 1. i번째 카드를 포함 안 함
            dp[i] = dp[i - 1]
            
            # 2. i번째 카드를 팩의 끝으로 포함
            # (i-1번째 인덱스가 유효한지 확인)
            if i >= S and is_valid[i - 1]:
                dp[i] = max(dp[i], dp[i - S] + 1)
                
            # (최적화) M개를 만들 수 있으면 즉시 True 반환
            if dp[i] >= m:
                return True
                
        # N개까지 다 봤는데 M개를 못 만들었음
        return False

    # --- 1. 이분 탐색 (Binary Search) ---
    low = 1
    high = n // m # S의 최대 가능 크기
    answer = 0
    
    while low <= high:
        mid_S = (low + high) // 2
        
        if mid_S == 0: # S=0은 불가능
            break
            
        if is_possible(mid_S):
            # mid_S가 가능하다면 -> 더 큰 S를 시도
            answer = mid_S
            low = mid_S + 1
        else:
            # mid_S가 불가능 -> 더 작은 S를 시도
            high = mid_S - 1
            
    print(answer)

solution()