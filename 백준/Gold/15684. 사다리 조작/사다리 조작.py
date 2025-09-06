import sys
input = sys.stdin.readline
def solution():
    n, m, h = map(int, input().split()) # 세로선, 이미 있는 가로선, 가로선
    ladder = [[False]*(n+1) for _ in range(h+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        ladder[a][b] = True

    def check():
        for i in range(1, n+1): # 세로선
            start = i
            for j in range(1, h+1):
                if ladder[j][start]:
                    start += 1
                elif ladder[j][start-1]:
                    start -= 1
            if start != i:
                return False
        return True
    
    result = 4
    def backtracking(x, y, cnt):
        nonlocal result
        # 제일 작은 횟수가 정답이 되어야 한다.
        if cnt >= result:
            return
        
        if check():
            result = cnt
            return
        
        if cnt == 3: # 3개를 놓았는데 아직 답을 못찾았다는 거니까
            return
        
        for a in range(x, h+1):
            # 행이 바뀌면 열의 시작점을 1로 초기화해주는 로직이 필요
            k = y if a == x else 1
            for b in range(k, n):
                if not ladder[a][b] and not ladder[a][b-1] and not ladder[a][b+1]:
                    ladder[a][b] = True # 사다리 놓을 수 있음
                    backtracking(a, b+2, cnt+1)
                    ladder[a][b] = False

    backtracking(1,1,0)
    print(result if result != 4 else -1)
solution()