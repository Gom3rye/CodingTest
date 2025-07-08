import sys
input = sys.stdin.readline
def solution():
    # 가장 긴 연속 부분(행 or 열) 고르기
    n = int(input())
    candies = [list(map(str, input().strip())) for _ in range(n)]
    def count_candies():
        max_candies = 0
        # 행 탐색
        for i in range(n):
            candy = 1
            for j in range(n-1):
                if candies[i][j] == candies[i][j+1]:
                    candy += 1
                else: # 중간에 끊겼으면 다시 초기화
                    candy = 1 
                max_candies = max(max_candies, candy)
        # 열 탐색
        for j in range(n):
            candy = 1
            for i in range(n-1):
                if candies[i][j] == candies[i+1][j]:
                    candy += 1
                else:   
                    candy = 1
                max_candies = max(max_candies, candy)
        
        return max_candies 
    
    max_result = 0
    for i in range(n):
        for j in range(n):
            # 사탕의 오른쪽 탐색
            if j < n-1 and candies[i][j] != candies[i][j+1]: # 서로 다르면 swap
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
                max_result = max(max_result, count_candies())
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j] # 다시 swap 해서 원상복귀
            # 사탕의 왼쪽 탐색
            if i < n-1 and candies[i][j] != candies[i+1][j]:
                candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
                max_result = max(max_result, count_candies())
                candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
    print(max_result)
solution()