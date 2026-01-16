import sys
input = sys.stdin.readline
def solution():
    # 트럭 한 대로 배송할 수 있는 최대 박스 수 구하기
    n, c = map(int, input().split()) # #마을 <=2000, 트럭 용량 <=10000
    m = int(input()) # #박스 정보 <=10000
    deliveries = []
    for _ in range(m):
        s, e, cnt = map(int, input().split())
        deliveries.append((e, s, cnt))
    deliveries.sort() # 더 빨리 받는 마을 순으로 정렬
    capacity = [c]*(n+1)
    answer = 0
    for e, s, cnt in deliveries:
        # 남은 용량중 제일 빡빡한 것(여유가 없는 것) (s~e-1구간에서 남은 최소 용량)
        min_capacity = min(capacity[s:e])
        # 부분적으로 가져갈 수도 있으니까
        can_take = min(min_capacity, cnt)
        if can_take > 0:
            for i in range(s, e): # s~e-1까지 차지하고 있으니까
                capacity[i] -= can_take
            answer += can_take
    print(answer)
solution()