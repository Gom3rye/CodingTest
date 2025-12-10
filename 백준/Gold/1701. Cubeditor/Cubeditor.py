import sys
input = sys.stdin.readline
def solution():
    s = input().strip()
    n = len(s)
    start, end, answer = 1, n-1, 0 # 가능한 최소 길이, 최대 길이, 정답
    while start <= end:
        mid = (start+end)//2 # 패턴 길이
        possible = set()
        # mid 길이만큼의 패턴들을 모두 저장 한 후 곂치는 게 있는지 확인
        for start_idx in range(n-mid+1):
            pattern = s[start_idx:start_idx+mid]
            if pattern in possible:
                answer = max(answer, mid)
                break # mid길이만큼의 패턴 찾았으니까 다른 mid로 넘어가기
            possible.add(pattern)
        else:
            # 맞는 패턴이 없는 거니까 길이 줄이기
            end = mid -1
            continue
        # 중복이 있었을 때) start를 오른쪽으로 밀면서 더 긴 패턴 있나 탐색
        start = mid + 1
    print(answer)
solution()