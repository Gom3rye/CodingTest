import sys
input = sys.stdin.readline
def solution():
    k = int(input()) # 추의 개수
    gs = list(map(int, input().split()))
    total = sum(gs) # <=13*20만(260만)
    dp = set([0])
    for g in gs:
        temp = set()
        for dp_v in dp:
            temp.add(dp_v+g)
            temp.add(abs(dp_v-g))
        dp.update(temp)
    print(total-len(dp)+1)
solution()