import sys
input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 1. 정렬 (O(N log N))
#   - 1순위: 종료 시간(end) 오름차순 (x[1])
#   - 2순위: 시작 시간(start) 오름차순 (x[0])
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

# 2. 그리디 순회 (O(N))
for start, end in meetings:
    
    # 3. 겹치지 않는지 확인
    if start >= last_end_time:
        # 4. 회의 선택
        count += 1
        last_end_time = end

print(count)