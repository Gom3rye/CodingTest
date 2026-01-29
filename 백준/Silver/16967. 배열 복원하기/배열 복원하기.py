import sys
input = sys.stdin.readline
def solution():
    h, w, x, y = map(int, input().split()) # <=300, 아래로 이동시킨 횟수, 오른쪽으로 이동시킨 횟수 <=h,w
    b = [list(map(int, input().split())) for _ in range(h+x)]
    a = [[0]*w for _ in range(h)]
    # a를 구해야 하니까 a크기만큼 for문 돌리기
    for i in range(h):
        for j in range(w):
            if i >= x and j >= y: # 모두에 포함되는 경우
                a[i][j] = b[i][j]-a[i-x][j-y]
            else:
                a[i][j] = b[i][j]
    for row in a:
        print(*row)
solution()