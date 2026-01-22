import sys
input = sys.stdin.readline
def solution():
    # 세 팀원의 코딩 실력의 합이 0인 팀 몇 개 만들 수 있는지
    n = int(input()) # #학생 <=10000
    a = sorted(map(int, input().split()))
    total = 0
    for i in range(n-2):
        one = a[i]
        two, three = i+1, n-1
        while two < three:
            team = one+a[two]+a[three]
            if team < 0:
                two += 1
            elif team > 0:
                three -= 1
            else: # total == 0:
                if a[two] == a[three]: # -4, 2, 2
                    cnt = three-two+1
                    total += (cnt*(cnt-1)//2) # 조합
                    break
                else: # -4, 1, 3
                    left = a[two]
                    left_cnt = 0
                    while a[two] == left:
                        two += 1
                        left_cnt += 1
                    right = a[three]
                    right_cnt = 0
                    while a[three] == right:
                        three -= 1
                        right_cnt += 1
                    total += left_cnt*right_cnt
    print(total)
solution()