import sys
input = sys.stdin.readline
from collections import deque
def solution():
    classes = [input().strip() for _ in range(5)]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    def backtracking(count, ppl):
        if count >= 4: # Y가 4명 이상이면 안됨
            return

        if tuple(sorted(ppl)) in visited: # 이미 결성했던 조합이면
            return
        
        if len(ppl) == 7:
            # set에 list는 못 넣으니까 불변 객체인 tuple로 만들어서 넣기 & 중복 제거를 위해 sorted로 정렬해서 한 가지 조합만 저장될 수 있도록
            crew.add(tuple(sorted(ppl)))
            return
        
        for x, y in ppl:
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0<=nx<5 and 0<=ny<5:
                    # 한 번 고려한 사람은 또 고려하면 안되니까
                    if (nx, ny) not in ppl:
                        if classes[nx][ny] == 'S':
                            ppl.append((nx, ny))
                            backtracking(count, ppl)
                            ppl.pop()
                        else:
                            ppl.append((nx, ny))
                            backtracking(count+1, ppl)
                            ppl.pop()
        visited.add(tuple(sorted(ppl)))
    
    crew = set() # 완성된 7공주 조합
    visited = set() # 중복 조합 가지치기 하기 위해서
    for i in range(5):
        for j in range(5):
            if classes[i][j] == 'S':
                backtracking(0, [(i,j)])
    print(len(crew))
solution()