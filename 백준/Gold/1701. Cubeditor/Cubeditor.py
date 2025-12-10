import sys
input = sys.stdin.readline
def solution():
    s = input().strip()
    n = len(s) # <=5000 -> n^3이면 시간초과 따라서 O(n^2)인 kmp 쓰기
    answer = 0
    # 모든 접미사에 대해 kmp 배열 생성
    for start in range(n):
        pi = [0]*(n-start)
        j = 0 # 현재까지 연속으로 일치한 접두사 길이
        # 접미사 문자열
        sub = s[start:]
        for i in range(1, len(sub)): # i: 우측 인덱스
            while j > 0 and sub[i] != sub[j]:
                j = pi[j-1] # 이전 최장길이로 돌아가기

            if sub[i] == sub[j]:
                j += 1
                pi[i] = j
                answer = max(answer, j)
    print(answer)
solution()