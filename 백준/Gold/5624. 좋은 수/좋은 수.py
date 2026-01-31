import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # <=5000
    a = list(map(int, input().split()))
    # a+b+c = a[d] -> a+b = a[d]-c
    two_sum = set()
    pre_set = set() # 앞에 있는 수들
    cnt = 0
    for num in a:
        for pre in pre_set:
            if num-pre in two_sum:
                cnt += 1
                break
        if num not in pre_set:
            pre_set.add(num)
            for pre in pre_set:
                two_sum.add(num+pre)
    print(cnt)
solution()