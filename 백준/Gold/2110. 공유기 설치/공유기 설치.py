import sys
input = sys.stdin.readline
n, c = map(int, input().split())
houses = []
for i in range(n):
    houses.append(int(input()))
houses.sort()
# 구해야 하는 것 : 가장 인접한 두 공유기 사이의 거리 -> target
# 계속 움직이면서 target을 구해야 하는 mid -> 현재 공유기 거리
start, end = 1, houses[-1]-houses[0] # start: 공유기 사이 값이 될 수 있는 최소, end: 공유기 사이 값이 될 수 있는 최대
result = 0
while start <= end:
    mid = (start+end)//2 # 현재 공유기 거리
    current = houses[0] # 첫 공유기 세음
    count = 1 # 공유기 한 개 설치했으니까
    
    # mid 값을 이용해서 공유기 설치, 공유기 몇 대 설치할 수 있는지 체크
    for i in range(1, len(houses)): # current로 이미 0번째 집은 공유기 설치했으니까 1번부터 시작
        if houses[i] >= current + mid:
            count += 1
            current = houses[i] # 그 다음 공유기 설치할 기준을 정하기 위해서 current 값 수정
    
    if count < c: # 설치해야 하는 공유기 수보다 적게 세웠으면 거리를 쫍게 해서 다시 설치
        end = mid -1
        
    else: # 설치해야 하는 공유기 수만큼 세웠거나 많이 세웠으면 거리를 멀리 해서 다시 해보기
        result = mid
        start = mid + 1
print(result)
            
