import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #정류소 <=1,000,000,000
    m = int(input()) # #노선 <=500,000
    # 버스 노선은 1based index
    # 동그란 노선을 linearize 해야 한다.
    intervals = [] # -> n이 너무 크니까 배열이 아닌 리스트로 관리!
    # 포함관계 판단 알고리즘 -> 정렬 + 스위핑
    # a < b: 어느 위치에 있는 큰 노선에라도 잡아먹힐 준비를 하기 위해 2군데 배치
    # a > b: 이미 두바퀴에 걸친 노선 -> 한번만 배치하면 됨
    # -> 2번 배치하는 경우도 있기 때문에 중복처리를 관리하기 위해 인덱스별 포함 여부를 저장하는 배열 활용!
    for idx in range(1, m+1):
        a, b = map(int, input().split())
        if a < b:
            intervals.append((a, b, idx))
            intervals.append((a+n, b+n, idx))
        else: # a > b:
            intervals.append((a, b+n, idx))
    # 일찍 시작해서 늦게 끝난 순으로 정렬 (그래야 단방향으로 가면서 모든 포함관계를 판별할 수 있다.)
    intervals.sort(key=lambda x: (x[0], -x[1]))
    max_end = -1
    included = [False]*(m+1) # 몇 번 버스 노선이 포함되었는지 저장
    for _, e, idx in intervals: # s,e,idx
        if e > max_end:
            max_end = e
        else: # 현재 max_end 값보다 작거나 같다 -> 즉, 포함되었다!
            included[idx] = True
    
    # included가 False 인 노선들만 출력
    print(*[i for i in range(1, m+1) if not included[i]])
solution()