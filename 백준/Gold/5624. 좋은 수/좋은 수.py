import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # <=5000
    a = list(map(int, input().split()))
    # a+b+c = a[d] -> a+b = a[d]-c
    two_sum = set()
    cnt = 0
    for i in range(n):
        # i번째 수가 좋은 수인지 확인
        for j in range(i):
            if a[i]-a[j] in two_sum:
                cnt += 1
                break # 좋은 수 판단 완료
        # two_sum 갱신 (a[i]를 사용해서)
        for k in range(i+1): # 같은 수 여러번 더해도 되니까 i+1까지해서 i*2도 가능하도록!
            two_sum.add(a[i]+a[k])
    print(cnt)
solution()