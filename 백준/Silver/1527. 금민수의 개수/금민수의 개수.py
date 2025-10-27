import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    a, b = map(int, input().split()) # <= 십억 (최대 10자리)
    # a<= <=b 중에서 4와 7로만 이루어진 수(금민수) 찾기
    # 금민수가 될 수 있는 경우의 수가 적으니까 총 가능한 금민수 수를 먼저 구하기
    # 가능한 금민수 수: 2^n (n:자리수)
    # total = 2^1+2^2+2^3+ ... +2^9 = 2*(2^9-1) = 1022
    golden = []
    def dfs(num):
        if num > b: # 가지치지
            return
        if num >= a: # a이상인 수만 금민수가 될 수 있다.
            golden.append(num)
        dfs(num*10+4)
        dfs(num*10+7)
    dfs(4)
    dfs(7)
    print(len(golden))
solution()