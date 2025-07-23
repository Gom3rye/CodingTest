import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    bags = [tuple(map(int, input().split())) for _ in range(n)]
    # dp[v] = 최소 무게 w ("가치 → 최소 무게" 기록 dict)
    dp = {0: 0} # 0가치를 무게 0으로 만들 수 있다.
    for w, v in bags:
        temp = {}
        for dp_v, dp_w in dp.items():
            nv = dp_v + v
            nw = dp_w + w
            
            if nw > k: # k까지의 무게만 담을 수 있으니까
                continue
            
            # nv에 대해 지금 계산한 무게 nw가 더 작다면 갱신하겠다. (최솟값을 비교하는 로직이니까 float('inf')로 초기화하는 것)
            if dp.get(nv, float('inf')) > nw: # nv가 존재-> nw 반환, 존재x-> 무한대 반환
                temp[nv] = nw
        dp.update(temp) # dp 딕셔너리에 temp 넣어서 갱신
    print(max(dp.keys()))
solution()