import sys
input = sys.stdin.readline
def solution():
    n, window = map(int, input().split())
    arr = list(map(int, input().split()))
    max_ppl = sum(arr[:window])
    ppl = max_ppl
    interval = 1
    start, end = 0, window-1
    while end < n-1:
        start += 1
        end += 1
        ppl = ppl-arr[start-1]+arr[end]
        if ppl > max_ppl:
            max_ppl = ppl
            interval = 1 # 새 max_ppl이 갱신되면 interval 초기화
        elif ppl == max_ppl:
            interval += 1

    print(max_ppl if max_ppl != 0 else "SAD")
    if max_ppl != 0:
        print(interval)
solution()