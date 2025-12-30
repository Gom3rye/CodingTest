import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #볼 <=500,000
    balls = input().strip()
    # 최소 횟수는 min(빨간왼, 빨간오, 파란왼, 파란오)로 정리한 경우들
    # 횟수는 덩어리의 개수로 구할 수 있고 lstrip(), rstrip()을 이용해 쉽게 풀자!
    counts = []
    # 왼쪽에 R이 있는 경우
    counts.append(balls.lstrip('R').count('R'))
    # 오른쪽에 R이 있는 경우
    counts.append(balls.rstrip('R').count('R'))
    # 왼쪽에 B가 있는 경우
    counts.append(balls.lstrip('B').count('B'))
    # 오른쪽에 B가 있는 경우
    counts.append(balls.rstrip('B').count('B'))
    print(min(counts))
solution()