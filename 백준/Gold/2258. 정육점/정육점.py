import sys

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    meats = []
    for _ in range(n):
        # 무게, 가격 순으로 입력받음
        w, p = map(int, input().split())
        meats.append((p, w)) # 가격 기준 정렬을 위해 (가격, 무게)로 저장

    # 1. 가격 오름차순, 가격 같다면 무게 내림차순 정렬
    meats.sort(key=lambda x: (x[0], -x[1]))

    total_weight = 0
    current_price = 0
    min_cost = float('inf')
    found = False

    for i in range(n):
        price, weight = meats[i]
        total_weight += weight
        
        # 2. 비용 계산
        # 이전 고기와 가격이 같으면 돈을 더 내야 함
        if i > 0 and meats[i][0] == meats[i-1][0]:
            current_price += price
        else:
            # 가격이 달라지면 현재 고기 가격만 내면 됨 (싼 건 다 덤)
            current_price = price
        
        # 3. 목표 무게 달성 시 최솟값 갱신
        if total_weight >= m:
            min_cost = min(min_cost, current_price)
            found = True

    # 4. 결과 출력
    if not found:
        print(-1)
    else:
        print(min_cost)

solution()