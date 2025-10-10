import sys
input = sys.stdin.readline
def solution():
    s = input().strip()
    n = len(s)
    # 단어를 3개의 단어로 쪼개서 각각 뒤집고 합치기 (단, 사전 순으로 가장 앞서는 단어 출력)
    # S를 S[:i], S[i:j], S[j:] 세 조각으로 나누기
    answer = []
    for first in range(n-2):
        for second in range(first+1, n-1):
            answer.append(s[:first+1][::-1]+s[first+1:second+1][::-1]+s[second+1:][::-1])
    print(sorted(answer)[0])
solution()