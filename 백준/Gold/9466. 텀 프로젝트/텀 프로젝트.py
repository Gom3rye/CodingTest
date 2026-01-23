import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    t = int(input())
    def dfs(now):
        nonlocal cnt
        visited[now] = 1
        nxt = students[now]
        if visited[nxt] == -1:
            dfs(nxt)
        elif visited[nxt] == 1: # 사이클 생성
            count = 1
            while nxt != now: # 기존 루트까지 찾아서
                nxt = students[nxt]
                count += 1
            cnt += count

        visited[now] = 2 # 완료 처리
        

    for _ in range(t):
        n = int(input()) # #힉셍 <=100,000
        temp = list(map(int, input().split()))
        students = []
        for i in range(n):
            students.append(temp[i]-1) # 0based index
        
        # 사이클 생성 탐지
        cnt = 0
        visited = [-1]*n
        for i in range(n):
            if visited[i] == -1:
                dfs(i)
        print(n-cnt)
solution()