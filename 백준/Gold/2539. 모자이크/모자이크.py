import sys
input = sys.stdin.readline

# 1. 입력 처리
R, C = map(int, input().split()) # 행, 열 (사용하지 않음)
K = int(input()) # 색종이 장수
N = int(input()) # 잘못 칠해진 칸의 개수

max_r = 0 # 가장 높은 행
mistake_cols = set() # 잘못 칠해진 칸의 "열" 좌표 (중복 제거)

for _ in range(N):
    r, c = map(int, input().split())
    max_r = max(max_r, r)
    mistake_cols.add(c)

# 2. 그리디 탐색을 위해 열 좌표 정렬
sorted_cols = sorted(list(mistake_cols))
num_unique_cols = len(sorted_cols)

# 3. 이분 탐색의 Check 함수 (그리디)
# "크기 S의 색종이 K장으로 덮을 수 있는가?"
def can_cover(S, K):
    if S < max_r: # S가 가장 높은 칸보다 작으면 절대 불가
        return False
        
    papers_used = 1
    # 첫 색종이는 가장 왼쪽 칸에 맞춤
    paper_end = sorted_cols[0] + S - 1 
    
    for i in range(1, num_unique_cols):
        col = sorted_cols[i]
        
        # 현재 칸이 이전 색종이의 범위를 벗어나면
        if col > paper_end:
            papers_used += 1 # 새 색종이 사용
            paper_end = col + S - 1 # 새 색종이 깔기
            
    # 사용한 색종이 수가 K장 이하인가?
    return papers_used <= K

# 4. 이분 탐색(Binary Search) 실행
low = max_r # 최소 크기
high = 1000001 # 최대 크기 (넉넉하게)
answer = high

while low <= high:
    mid_S = (low + high) // 2
    
    if can_cover(mid_S, K):
        # 덮을 수 있음 -> 더 작은 크기(S)를 시도
        answer = mid_S
        high = mid_S - 1
    else:
        # 덮을 수 없음 -> 더 큰 크기(S)가 필요
        low = mid_S + 1

print(answer)