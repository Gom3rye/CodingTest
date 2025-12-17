import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 선 그은 횟수 <=1,000,000
    lines = [tuple(map(int, input().split())) for _ in range(n)]
    lines.sort() # 시작점을 기준으로 정렬!
    
    total = 0
    cur_start, cur_end = lines[0]
    for start, end in lines[1:]:
        # 겹치는 경우
        if start <= cur_end:
            cur_end = max(cur_end, end)
        else: # 안 겹치니까 길이 더하고 cur_start, cur_end 갱신
            total += cur_end-cur_start
            cur_start, cur_end = start, end
    
    # 마지막 길이도 더해주기
    total += cur_end-cur_start
    print(total)
solution()