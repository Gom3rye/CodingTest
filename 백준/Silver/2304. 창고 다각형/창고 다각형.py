import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 기둥의 개수 <=1000
    pillars = [list(map(int, input().split())) for _ in range(n)]
    pillars.sort()
    # 최대 기둥을 기준으로 왼쪽 오른쪽 나누기 + 최대 기둥 1개 만큼의 사이즈 더해주기
    max_height = -1
    max_idx = -1
    for i in range(n):
        if max_height <= pillars[i][1]:
            max_height = pillars[i][1]
            max_idx = i # max_height가 여러 개 있을 때 제일 오른쪽에 있는 max_height의 x좌표를 구하자
    answer = 0
    # 구현 ver.
    # 왼쪽 면적 구하기
    now_h = 0
    for i in range(max_idx+1):
        if i > 0:
            answer += (pillars[i][0]-pillars[i-1][0])*now_h
        now_h = max(now_h, pillars[i][1])
    # 오른쪽 면적 구하기
    now_h = 0
    for i in range(n-1, max_idx-1, -1):
        if i < n-1:
            answer += (pillars[i+1][0]-pillars[i][0])*now_h
        now_h = max(now_h, pillars[i][1])
    print(answer+max_height) # max_height 한 기둥 뺀 거 더해주기
solution()