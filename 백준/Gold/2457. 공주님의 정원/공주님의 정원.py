import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #꽃 <=100,000
    def day_to_num(month, day): # 계산하기 쉬운 숫자로 바꾸기 (어차피 3/31 < 4/1, 3/30 < 4/1이기 때문에 각 월이 몇일까지 있는지는 중요x)
        return month*100+day
    # 301 ~ 1130까지 매일 꽃이 한 가지 이상 피어있어야 한다.
    flowers = []
    for _ in range(n):
        sm, sd, em, ed = map(int, input().split())
        flowers.append((day_to_num(sm, sd), day_to_num(em, ed)))
    flowers.sort() # 시작날 기준으로!
    start = 301
    max_end = 0
    cnt = 0
    idx = 0
    while start <= 1130:
        connected = False
        while idx < n:
            if flowers[idx][0] <= start: # 피어야 할 기간에 피고
                # 가장 늦게 지는 꽃 찾기
                max_end = max(max_end, flowers[idx][1])
                idx += 1
                connected = True
            else:
                break
        if not connected:
            print(0)
            return
        cnt += 1
        start = max_end
    print(cnt)
solution()