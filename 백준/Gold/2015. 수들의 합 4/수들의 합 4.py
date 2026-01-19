import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split()) # #수 <=200,000, 부분합 |k| <=2,000,000,000
    arr = list(map(int, input().split()))
    # 음수가 있기때문에 단조성이 깨져 투포인터는 사용하면 안됨!
    prefix_sum = {0:1} # 합이 딱 k인 경우를 위해 누적합0인 경우도 1개 있다고 초기화
    # 구간 합의 차 =k 를 이용해서 해시맵으로 풀자!
    cnt = 0
    now_sum = 0
    for i in range(n):
        now_sum += arr[i]
        target = now_sum-k
        if target in prefix_sum:
            cnt += prefix_sum[target]
        if now_sum in prefix_sum:
            prefix_sum[now_sum] += 1
        else:
            prefix_sum[now_sum] = 1
    print(cnt)
solution()