import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 가능한 모든 비밀번호의 개수를 구하는 것이니까 백트레킹
    pwd = []
    cnt = 0
    def backtracking(idx):
        nonlocal cnt
        if idx == n: # 자리수만큼 조합했을 경우
            for num in numbers:
                if num not in pwd:
                    break
            else:
                cnt += 1
            return
        for num in range(10):
            pwd.append(num)
            backtracking(idx+1)
            pwd.remove(num)
            
    backtracking(0)
    print(cnt)
solution()