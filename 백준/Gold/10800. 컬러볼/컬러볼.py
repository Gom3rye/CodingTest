import sys
input = sys.stdin.readline
INF = float('inf')
def solution():
    n = int(input()) # #공 <=200,000
    # n이 큼 -> 정렬+누적합 의심!!
    balls = []
    for i in range(n):
        color, size = map(int, input().split())
        balls.append((size, color, i))
    balls.sort()
    # 답
    answer = [0]*n
    colors = [0]*(n+1) # 같은 컬러는 먹을 수 없으니까 컬러별로 누적합 만들어주기 위해 1based index
    # n이 크기 때문에 투포인터를 써서 단방향으로만 계산할 수 있도록!
    left = 0
    total_sum = 0 # 지금까지의 합
    for right in range(n):
        size, color, idx = balls[right]
        while balls[left][0] < size:
            s, c, _ = balls[left]
            total_sum += s
            # color별로 누적합 관리 (c색의 누적합: colors[c] += s)
            colors[c] += s
            left += 1

        answer[idx] = total_sum - colors[color]

    print('\n'.join(map(str, answer)))
solution()