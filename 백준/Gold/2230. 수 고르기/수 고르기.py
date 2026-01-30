import sys
input = sys.stdin.readline

def solution(A, N, M):
    left, right = 0, 0
    answer = 2000000000
    while right < N:
        diff = A[right] - A[left]
        if diff < M:
            right += 1
        elif diff > M:
            answer = min(diff, answer)
            left += 1
        else:
            return M
    return answer    

N, M = map(int, input().split())

A = [int(input()) for _ in range(N)]

# 오름차순 정렬
A.sort()

# 답변 구하기
answer = solution(A, N, M)

print(answer)