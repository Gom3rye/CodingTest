import sys, heapq
input = sys.stdin.readline
def solution():
    # “데드라인 있는 작업 스케줄링” -> 미래 선택 때문에 과거 선택을 버려야 할 수도 있기 때문에 stack 안됨!
    # -> 가장 손해인 것을 버리는 구조 (여기서는 작은 컵라면 수를 버리자)
    n = int(input()) # #숙제 <=200,000
    ramen = [tuple(map(int, input().split())) for _ in range(n)]
    ramen.sort() # 데드라인별로 정렬
    # 받을 수 있는 최대 컵라면 수 출력
    # 최대 수라 dp를 생각했지만 과거에서부터 일직선으로 정보를 갱신하는 게 아니기 때문에 포기
    q = []
    for deadline, cnt in ramen:
        # 계속 추가하다가 조건을 어기면 최악을 버리기
        heapq.heappush(q, cnt)
        if len(q) > deadline:
            heapq.heappop(q)
    print(sum(q))
solution()