import sys

input = sys.stdin.readline

# N, M, L 입력
N, M, L = map(int, input().split())

# 휴게소 위치 입력
locations = [0] + list(map(int, input().split())) + [L]

# 위치 정렬
locations.sort()

# 이진 탐색 구간 정의
start = 1
end = L - 1

# 이진 탐색 구현
while start <= end:
    # 휴게소 없는 구간의 최댓값 정의
    mid = (start + end) // 2

    # 설치한 휴게소 수 초기화
    cnt = 0

    # 휴게소 간 거리 계산해 지정한 최댓값보다 큰 값 확인
    for i in range(len(locations)-1):
        if locations[i+1] - locations[i] > mid:
            # 휴게소 설치
            cnt += (locations[i+1] - locations[i] - 1) // mid

    # M과 설치한 휴게소 수 비교
    if cnt <= M:
        end = mid - 1
    else:
        start = mid + 1

# 결과 출력
print(start)
