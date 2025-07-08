import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split()) # n: 멀티탭 구멍의 개수, k: 총 사용횟수
    u = list(map(int, input().split())) # 사용 순서
    extcord = u[:1] # 초반에 한 개 꽂고 시작.
    unplug = 0
    for i in range(1, k):
        # 이미 꽂혀있다면 건너뜀
        if u[i] in extcord:
            continue
        # 플러그 비어있다면 꽂기
        if len(extcord) < n:
            extcord.append(u[i])
            continue
        # 다 꽂혀있다면 가장 나중에 사용할 기기나 안 쓸 기기를 빼기
        priority = []
        # i번째는 extcord에 넣어야 하니까 i+1번째 기기들 중에 우선순위 구하기
        for a in extcord:
            if a in u[i+1:]:
                priority.append(u[i+1:].index(a))
            else: # 앞으로 안 쓸 기기라면 우선순위 왕 크게
                priority.append(101) # k의 최대범위가 100까지니까
        readytounplug = extcord[priority.index(max(priority))]
        extcord.remove(readytounplug)
        extcord.append(u[i])
        unplug += 1
    print(unplug)
solution()