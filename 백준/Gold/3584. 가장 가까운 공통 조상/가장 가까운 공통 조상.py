import sys
from math import log2
input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t):
        n = int(input()) # #노드 <=10000
        parents = [0]*(n+1)
        for _ in range(n-1):
            a, b = map(int, input().split())
            parents[b] = a # b의 조상은 a
        v1, v2 = map(int, input().split()) # 공통조상을 찾아야 하는 두 노드
        # v1으로 부모 set만들고 이를 이용해서 v2로 거슬러 올라가면서 그 set에 있는지 없는지 확인
        parents_set = {v1}
        while parents[v1] != 0:
            v1 = parents[v1]
            parents_set.add(v1)
        while v2 != 0:
            if v2 in parents_set:
                print(v2)
                break # v2->거꾸로 올라가는 거니까 이때 바로 출력하는게 제일 가까운 공통 조상!
            v2 = parents[v2]
solution()