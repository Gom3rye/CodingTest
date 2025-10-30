import sys
input = sys.stdin.readline
def solution():
    k = int(input()) # 사람 수
    n = int(input()) # 전체 가로 줄의 수
    end = list(input().strip())
    start = sorted(end) # ex) ABCDEF...
    board = [list(input().strip()) for _ in range(n)] # *: 가로 없음, -: 가로 있음
    # ?를 기준으로 사다리 나누기 (?가 어디에 있는지는 모름)
    for row in range(n):
        if board[row][0] == '?':
            before = board[:row] # 2D list slicing
            after = board[row+1:]
            break
    # start를 before대로 이동하고
    # end를 after[::-1]대로 이동해서 ???를 거친 후 start과 before이 같아야 한다.
    for row in range(len(before)):
        for j in range(k-1):
            if before[row][j] == '-':
                start[j], start[j+1] = start[j+1], start[j] # swap
    after = after[::-1] # reverse
    for row in range(len(after)):
        for j in range(k-1):
            if after[row][j] == '-':
                end[j], end[j+1] = end[j+1], end[j] # swap
    # print(start)
    # print(end)
    answer = []
    for j in range(k-1):
        if start[j] == end[j]:
            answer.append('*')
        else: # 다른 경우
            if start[j] == end[j+1] and start[j+1] == end[j]:
                answer.append('-')
            elif j != 0 and start[j] == end[j-1] and start[j-1] == end[j]:
                answer.append('*')
            else:
                print('x'*(k-1))
                return
    print("".join(answer))
solution()