import sys
from itertools import permutations
input = sys.stdin.readline
def solution():
    n = int(input()) # #사람 <=10
    # cnt의 idx: idx+1번째 사람의 왼쪽에 자신보다 큰 사람이 있는 횟수
    cnt = list(map(int, input().split()))
    if sum(cnt) == 0:
        print(*range(1, n+1))
        return
    for ppl in permutations(range(1, n+1), n):
        for idx, person in enumerate(ppl):
            bigger = 0
            # idx-1번째 사람까지 자신과 비교하면서 더 큰사람의 수가 cnt[person-1]과 같은지 확인
            for i in range(idx):
                if ppl[i] > person:
                    bigger += 1
            if bigger != cnt[person-1]:
                break
        else:
            print(*ppl)
solution()