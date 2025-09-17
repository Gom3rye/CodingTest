import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    result = []
    # 수열의 끝부분을 기준으로 같은 길이의 인접 부분 수열이 있는지 체크
    def is_good(string):
        length = len(string)
        # 인접한 두 수열을 비교해야 하므로 가능한 최대 길이는 전체 길이의 절반이다.
        for i in range(1, length//2+1): # 비교할 부분 수열의 길이
            # 앞에서부터 비교하면 문제 없던 부분도 처음부터 다시 계속 비교해야 하니까
            # 보통 문제가 생기는 부분은 수열의 끝부분이니까 순서를 뒷부분부터 검사 (추가할 때마다 is_good 검사하니까)
            if string[-i:] == string[-2*i:-i]:
                return False
        return True
    def backtracking(idx):
        if idx == n:
            print("".join(map(str, result)))
            sys.exit()
        for num in [1, 2, 3]:
            result.append(num)
            if is_good(result):
                backtracking(idx+1)
            # 재귀가 끝난 후에는 무조건 pop으로 상태 복원 (백트레킹은 모든 경로를 탐색하기 때문에 )
            result.pop()
    backtracking(0)
solution()