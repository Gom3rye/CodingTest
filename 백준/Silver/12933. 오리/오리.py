import sys
input = sys.stdin.readline
def solution():
    # 최대한 적은 '동시에 우는 오리 수' 구하기
    duck = input().strip()
    order = {'q':0, 'u':1, 'a':2, 'c':3, 'k':4}
    count = [0]*5 # count[0]: q를 소리했고 u를 기다리고 있는 오리의 수
    answer = 0 # 오리 수
    for char in duck:
        idx = order[char]
        if idx == 0: # q인 경우
            if count[-1] > 0: # k가 끝나고 온 q인 경우
                count[-1] -= 1
            else: # 새 오리 추가해야 하는 경우
                answer += 1
            count[0] += 1
        else: # u,a,c,k 인 경우
            if count[idx-1] > 0:
                count[idx-1] -= 1
                count[idx] += 1
            else: # 녹음한 소리가 올바르지 않은 경우
                print(-1)
                return
    # count[0], [1], [2], [3] 중 하나라도 1이상이면 어떤 오리는 끝까지 quack를 못 말한 것
    print(-1 if count[0] or count[1] or count[2] or count[3] else answer)
solution()