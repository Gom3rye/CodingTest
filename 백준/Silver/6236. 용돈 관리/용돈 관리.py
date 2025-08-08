import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    spend = [int(input()) for _ in range(n)]
    # 최소 인출 금액(k) 계산하기
    # k가 작아지면 인출 횟수 늘어나고 k가 커지면 인출 횟수 작아진다. (인출 횟수는 m 이하여야 한다.)
    left, right = max(spend), sum(spend) # 인출 횟수가 적어도 1번은 되야 하니까 k의 최댓값은 sum(spend)
    while left <= right:
        k = (left+right)//2
        count = 1
        current = k
        for cost in spend:
            if current < cost:
                count += 1
                current = k
            current -= cost
        if count <= m:
            answer = k
            right = k-1
        else:
            left = k+1
        
    print(answer)
solution()