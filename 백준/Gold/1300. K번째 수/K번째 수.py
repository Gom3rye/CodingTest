import sys

def solve():
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())

    low = 1
    high = K # K번째 수는 K보다 클 수 없음
    answer = 0

    while low <= high:
        mid = (low + high) // 2 # 우리가 검사할 숫자 x
        
        # mid보다 작거나 같은 숫자의 개수 카운트
        count = 0
        for i in range(1, N + 1):
            # i번째 행에서 mid보다 작거나 같은 숫자의 개수
            count += min(N, mid // i)
        
        if count >= K:
            # mid보다 작거나 같은 숫자가 K개 이상이면, 
            # 일단 mid를 후보로 저장하고 더 작은 숫자가 있는지 확인
            answer = mid
            high = mid - 1
        else:
            # K개 미만이면 숫자를 더 키워야 함
            low = mid + 1

    print(answer)

solve()