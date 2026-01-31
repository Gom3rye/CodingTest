import sys
input = sys.stdin.readline
INF = float('inf')
def dist(c1, c2):
    return abs(c1[0]-c2[0])+abs(c1[1]-c2[1])
def solution():
    n = int(input()) # #checkpoint <=100,000
    checkpoints = [list(map(int, input().split())) for _ in range(n)]
    # 체크포인트 1개 건너뛰면서 달릴 수 있고 이때 달려야 하는 최소 거리는?
    not_used = [0]*n # 현재->다음(미래)로 전개: push방식!
    used = [INF]*n # 건너뛰는 기회를 쓴 경우 # 처음은 못 건너뛰니까 used[0] = 0으로 초기화 안해도 됨
    for i in range(1, n):
        d = dist(checkpoints[i-1], checkpoints[i])
        # 갱신(건너뛰기가 1번밖에 안되기 때문에 건너뛰기 사용여부를 체크하기 위해 두 상태 모두 갱신하며 가져가야 한다.)
        not_used[i] = not_used[i-1]+d
        used[i] = used[i-1]+d
        # 건너 뛰고 온 경우
        if i >= 2:
            used[i] = min(used[i], not_used[i-2]+dist(checkpoints[i-2], checkpoints[i]))
    print(used[-1])
solution()