import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 행,열 <= 1,000,000
    paper = int(input()) # <= 100
    wrong = int(input()) # <= 1000
    max_row = 0
    cols = set()
    for _ in range(wrong):
        r, c = map(int, input().split())
        if r > max_row:
            max_row = r
        cols.add(c)
    cols_list = sorted(cols)

    def is_valid(size):
        if size < max_row: # 최대 행보다 작으면 불가능(밑에서 맞추어 붙이니까)
            return False
        end = cols_list[0]+size-1 # 색종이가 끝나는 열의 번호
        cnt = 1 # 색종이 
        for col in cols_list:
            if col > end:
                cnt += 1
                end = col+size-1 # 다음 색종이가 끝나는 열의 번호
            if cnt > paper:
                return False
        return True
    
    # 백만 중에서 최적의 사이즈를 찾아야 하기 때문에 이분탐색으로 시간복잡도 관리
    # 가장 작은 색종이의 크기 구하기
    start, end = 1, 1000000
    answer = 0
    while start <= end:
        mid = (start+end)//2
        if is_valid(mid):
            answer = mid
            end = mid-1
        else:
            start = mid+1
    print(answer)
solution()