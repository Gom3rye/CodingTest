import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    nums = [0]+[int(input()) for _ in range(n)] # 1based index
    visited = [-1]*(n+1) # -1: 미방문, 1: 방문 중, 2: 방문 완료
    result = set()
    def dfs(x):
        visited[x] = 1
        nxt = nums[x]

        if visited[nxt] == -1:
            dfs(nxt)
        # cycle 발생
        elif visited[nxt] == 1:
            temp = set([nxt])
            while nxt != x:
                nxt = nums[nxt]
                temp.add(nxt)
            result.update(temp)
        
        visited[x] = 2 # 방문 종료
    for i in range(1, n+1):
        if visited[i] == -1:
            dfs(i)
    
    print(len(result))
    for i in sorted(result):
        print(i)
    
solution()