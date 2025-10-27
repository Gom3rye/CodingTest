import sys
input = sys.stdin.readline
def solution():
    k = int(input()) # 추의 개수
    gs = list(map(int, input().split()))
    total = sum(gs) # <=13*20만(260만)
    cant = 0 # 측정할 수 없는 경우의 수
    dp = set([0])
    for g in gs:
        temp = set()
        for dp_v in dp:
            temp.add(dp_v+g)
            if abs(dp_v-g) > 0:
                temp.add(abs(dp_v-g))
        dp.update(temp)
    for i in range(1, total+1):
        if i not in dp:
            cant += 1
    print(cant)
solution()