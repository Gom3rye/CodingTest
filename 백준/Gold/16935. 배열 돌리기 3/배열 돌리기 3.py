import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m, r = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    ops = list(map(int, input().split()))
    def op1(arr):
        # 상하 반전
        return arr[::-1]
    def op2(arr):
        # 좌우 반전
        return [row[::-1] for row in arr]
    def op3(arr):
        # 오른쪽으로 90도 회전 # n<->m
        return [list(row) for row in zip(*arr[::-1])]
    def op4(arr):
        # 왼쪽으로 90도 회전 # n<->m
        return [list(row) for row in zip(*arr)][::-1]
    def op5(arr):
        # 4분할 후 시계방향 회전 1->2->3->4->1
        narr = [[0]*m for _ in range(n)]
        nn, nm = n//2, m//2
        # 1->2
        for i in range(nn):
            for j in range(nm):
                narr[i][j+nm] = arr[i][j]
        # 2->3
        for i in range(nn):
            for j in range(nm):
                narr[i+nn][j+nm] = arr[i][j+nm]
        # 3->4
        for i in range(nn):
            for j in range(nm):
                narr[i+nn][j] = arr[i+nn][j+nm]
        # 4->1
        for i in range(nn):
            for j in range(nm):
                narr[i][j] = arr[i+nn][j]
        return narr
    
    def op6(arr):
        # 4분할 후 반시계방향 회전 1->4->3->2->1
        narr = [[0]*m for _ in range(n)]
        nn, nm = n//2, m//2
        # 1->4
        for i in range(nn):
            for j in range(nm):
                narr[i+nn][j] = arr[i][j]
        # 4->3
        for i in range(nn):
            for j in range(nm):
                narr[i+nn][j+nm] = arr[i+nn][j]
        # 3->2
        for i in range(nn):
            for j in range(nm):
                narr[i][j+nm] = arr[i+nn][j+nm]
        # 2->1
        for i in range(nn):
            for j in range(nm):
                narr[i][j] = arr[i][j+nm]
        return narr
    
    for op in ops:
        if op == 1:
            board = op1(board)
        elif op == 2:
            board = op2(board)
        elif op == 3:
            n, m = m, n
            board = op3(board)
        elif op == 4:
            n, m = m, n
            board = op4(board)
        elif op == 5:
            board = op5(board)
        else:
            board = op6(board)

    for row in board:
        print(*row)
solution()