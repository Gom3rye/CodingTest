import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 식재료의 개수
    # 단, 지, 탄, 비타민
    mp, mf, ms, mv = map(int, input().split())
    nutrients = [[]]+[tuple(map(int, input().split())) for _ in range(n)] # 1based index로 맞춰주기
    min_cost = float('inf')
    result = []
    materials = []
    def backtracking(idx, cost, tp, tf, ts, tv):
        nonlocal min_cost, materials
        if cost > min_cost: # 가지치기
            return
        if idx == n+1:
            # 합이 최소 영양소를 만족하는 경우만 봐야 하므로 이 단계에서 확인해야 한다.
            if tp >= mp and tf >= mf and ts >= ms and tv >= mv:
                if cost < min_cost:
                    min_cost = cost
                    materials = result[:] # pop/append로 리스트 내용 수정은 가능하지만 리스트 전체 재할당은 nonlocal로 선언해야 한다.
                    # 함수 안에서 변수에 = 할당을 하면 그 변수는 자동으로 지역 변수로 취급되기 때문에.
                elif cost == min_cost:
                    if result < materials:
                        materials = result[:]
            return
        
        p, f, s, v, c = nutrients[idx]
        # idx의 식재료를 고르는 경우
        result.append(idx)
        backtracking(idx+1, cost+c, tp+p, tf+f, ts+s, tv+v)
        result.pop()
        # idx의 식재료를 고르지 않는 경우
        backtracking(idx+1, cost, tp, tf, ts, tv)

    backtracking(1, 0, 0, 0, 0, 0) # 1번 재료부터 확인
    if min_cost != float('inf'):
        print(min_cost)
        print(*materials)
    else:
        print(-1)
solution()