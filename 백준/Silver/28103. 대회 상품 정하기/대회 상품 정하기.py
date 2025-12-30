import sys
from bisect import bisect_left
input = sys.stdin.readline
def solution():
    n, m, x = map(int, input().split()) # 참가자수<=10^12, 상품목록<=10^6, 자금정수<=10^18
    prices = list(map(int, input().split()))
    # 필요한 변수 선언
    budget = x
    remaining_ppl = n
    cheapest = prices[-1]
    answer = [0]*m

    # 가능한 비싼 선물의 위치를 찾기 위해 cost 오름차순으로 정렬하고 bisetct_left 사용!
    neg_cost = [-p for p in prices]
    while remaining_ppl > 0:
        # max_price는 지금 사람 제외한 나머지 사람들이 cheapest를 배정받았다고 할 때 남는 예산
        max_price = budget-(remaining_ppl-1)*cheapest
        idx = bisect_left(neg_cost, -max_price) # -넣기 잊지 말기
        # price: 제일 비싼 선물(가격)
        price = prices[idx]

        # 이제 이 price를 몇 개 배정할 수 있는지 이분 탐색으로 찾기
        cnt, start, end = 1, 1, remaining_ppl
        while start <= end:
            mid = (start+end)//2 # 배정할 수 있는 개수
            # 공식: if budget-(젤 비싼거 가능한 개수)*가격 >= (remaining_ppl-(젤 비싼거 가능한 개수))*cheapest: ans = mid
            if budget-mid*price >= (remaining_ppl-mid)*cheapest:
                cnt = mid
                start = mid + 1
            else:
                end = mid -1
        
        budget -= price*cnt
        remaining_ppl -= cnt
        answer[idx] += cnt
    print(*answer)
solution()