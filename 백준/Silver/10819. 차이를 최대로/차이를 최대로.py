import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    
    # 각 인덱스의 사용 여부를 기록할 배열
    visited = [False] * n
    max_result = 0

    def backtracking(perm):
        nonlocal max_result
        
        # 순열이 완성되면 값을 계산
        if len(perm) == n:
            result = 0
            for i in range(n - 1):
                result += abs(perm[i] - perm[i+1])
            max_result = max(max_result, result)
            return

        # 0번부터 n-1번 인덱스를 순회
        for i in range(n):
            # 만약 i번 인덱스를 아직 사용하지 않았다면
            if not visited[i]:
                # 사용했다고 표시
                visited[i] = True
                perm.append(a[i])
                
                # 재귀 호출
                backtracking(perm)
                
                # 탐색이 끝나면 다음 순열을 위해 원래대로 되돌림
                visited[i] = False
                perm.pop()
                
    backtracking([])
    print(max_result)

solution()