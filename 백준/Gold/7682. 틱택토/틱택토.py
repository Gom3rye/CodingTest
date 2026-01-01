import sys
from collections import Counter
input = sys.stdin.readline
def solution():
    def win(board, person):
        # 나올 수 있는 경우의 수 모두 나열 ---,|||,\,/
        cases = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for first, second, third in cases:
            if board[first] == board[second] == board[third] == person:
                return True
        return False
    while True:
        game = input().strip()
        if game == 'end':
            break
        # invalid한 경우를 모두 나열
        count = Counter(game)
        x_cnt = count['X']
        o_cnt = count['O']
        x_win = win(game, 'X')
        o_win = win(game, 'O')
        if x_cnt < o_cnt:
            print('invalid')
        elif not (x_cnt == o_cnt or x_cnt == o_cnt+1):
            print('invalid')
        # 둘 다 승리한 경우
        elif x_win and o_win:
            print('invalid')
        # x 승리했을 경우 -> x의 개수 == o의 개수+1
        elif x_win and x_cnt == o_cnt+1:
            print('valid')
        # o 승리했을 경우 -> o의 개수 == x의 개수
        elif o_win and x_cnt == o_cnt:
            print('valid')
        # 둘 다 승리하지 못한 경우
        elif not x_win and not o_win and x_cnt+o_cnt==9:
            print('valid')
        else:
            print('invalid')
solution()