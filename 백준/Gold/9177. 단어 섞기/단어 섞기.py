import sys
input = sys.stdin.readline
def solution():
    t = int(input()) # 데이터 집합의 개수 <=1000
    for tc in range(1, t+1):
        a, b, c = input().split() # 단어 길이 <=200
        # a에서 i개, b에서 j개를 써서 c의 (i+j)번째 문자를 만들 수 있는가?
        n1 = len(a) # 0~i-1
        n2 = len(b) # 0~j-1
        dp = [[False]*(n2+1) for _ in range(n1+1)]
        dp[0][0] = True # 아무것도 안 사용해서 아무것도 안 만드는 건 항상 True로 시작 (초기화)
        for i in range(n1+1):
            for j in range(n2+1):
                if i > 0 and dp[i-1][j] and a[i-1] == c[i+j-1]: # 0based index
                    dp[i][j] = True
                if j > 0 and dp[i][j-1] and b[j-1] == c[i+j-1]:
                    dp[i][j] = True
        
        answer = 'yes' if dp[n1][n2] else 'no'
        print(f"Data set {tc}: {answer}")
solution()