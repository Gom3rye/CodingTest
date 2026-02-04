import sys
input = sys.stdin.readline
def solution():
    dna = input().strip() # len <=500
    # 부분 서열을 골라 길이가 최대가 되는 KOI 유전자 길이 출력 (구간 DP(Interval Dynamic Programming))
    n = len(dna)
    dp = [[0]*n for _ in range(n)] # dp[i][j]: i ~ j구간에서의 최대 KOI 유전자 길이
    for length in range(1, n): # i ~ i+length을 기준으로 탐색
        for i in range(n-length): # n-length번 반복
            j = i+length
            # 방법1: aXt, gXc 처럼 끝에 a~t, g~c인 경우
            if (dna[i]=='a' and dna[j]=='t') or (dna[i]=='g' and dna[j]=='c'):
                dp[i][j] = dp[i+1][j-1]+2
            # 방법2: x,y가 유전자라면 xy도 유전자, k: 왼쪽 구간의 끝 인덱스
            for k in range(i, j): # (i,i)/(i,j) ~ (i,j/(j,j) 까지 모든 가능한 분할 지점 다 확인해봐야 한다.
                dp[i][j] = max(dp[i][j], dp[i][k]+dp[k+1][j])
    print(dp[0][-1])
solution()