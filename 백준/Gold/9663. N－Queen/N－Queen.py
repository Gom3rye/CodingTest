import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    count = 0
    col = [0]*n
    left_diagonal = [0]*(2*n-1)
    right_diagonal = [0]*(2*n-1)
    def queen(i):
        nonlocal count
        if i == n:
            count += 1
            return
        for j in range(n):
            if not col[j] and not left_diagonal[i+j] and not right_diagonal[i-j+n-1]:
                col[j] = left_diagonal[i+j] = right_diagonal[i-j+n-1] = 1
                queen(i+1) # i행에 퀸 한개 놓았으니까 다음 i+1(행)으로 이동
                col[j] = left_diagonal[i+j] = right_diagonal[i-j+n-1] = 0 #다시 원위치

    # queen(0)-> queen 1개, queen(1)-> queen 2개, .. , queen(3)-> queen 4개
    queen(0)
    print(count)
solution()