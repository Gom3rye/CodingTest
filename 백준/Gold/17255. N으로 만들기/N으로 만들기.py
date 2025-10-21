import sys
input = sys.stdin.readline
def solution():
    n = input().strip()
    l = len(n)
    answer = []

    def dfs(s, left, right, process): # string, left, right index, process
        if left == 0 and right == l-1:
            if process not in answer:
                answer.append(process)
            return
        
        if left > 0: # 왼쪽으로 갈 수 있음
            dfs(n[left-1]+s, left-1, right, process+n[left-1]+s)
        if right < l-1: # 오른쪽으로 갈 수 있음
            dfs(s+n[right+1], left, right+1, process+s+n[right+1])

    for i in range(l):
        dfs(n[i], i, i, n[i]) # 초반에는 left, right 인덱스를 같이 주기
    print(len(answer))
solution()