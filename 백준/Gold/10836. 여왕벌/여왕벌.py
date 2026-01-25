import sys

input = sys.stdin.readline

def solution():
    # M: 격자 크기, N: 날짜 수
    M, N = map(int, input().split())
    
    # 테두리(왼쪽 열 + 위쪽 행)의 누적 성장치를 저장할 배열
    # 길이는 (M-1) + 1 + (M-1) = 2M-1
    # 초기 크기는 모두 1
    total_growth = [0] * (2 * M - 1)

    # N일 동안의 성장을 누적
    for _ in range(N):
        cnt0, cnt1, cnt2 = map(int, input().split())
        # 0은 더할 필요 없음, 1과 2가 시작되는 지점만 마킹 (차분 배열 원리)
        if cnt0 < 2 * M - 1:
            total_growth[cnt0] += 1
            if cnt0 + cnt1 < 2 * M - 1:
                total_growth[cnt0 + cnt1] += 1

    # 누적합을 통해 각 위치의 최종 성장치를 구함
    curr = 0
    for i in range(2 * M - 1):
        curr += total_growth[i]
        total_growth[i] = curr + 1 # 초기 크기 1 더함

    # 출력 최적화
    # 첫 번째 행을 제외한 나머지 행들의 내부 값은 첫 번째 행의 값과 동일함
    top_row = total_growth[M-1:] # (0,0)부터 (0, M-1)까지의 값
    
    for i in range(M):
        if i == 0:
            # 첫 번째 행은 전체 출력
            print(*(top_row))
        else:
            # i번째 행의 첫 번째 열 값은 total_growth[M-1-i]
            # 나머지는 top_row[1:]와 동일함
            print(total_growth[M-1-i], *(top_row[1:]))

solution()