import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # <=20
    origin = [list(map(int, input().split())) for _ in range(n)]
    # 최대 5번을 이동시켜서 얻을 수 있는 가장 큰 블록 출력
    # 4**5*20*20 = 1024*400 -> 브루트포스 가능
    def move(arr):
        narr = []
        for i in range(n):
            standard = 0 # 기준값은 0으로 두기
            temp = []
            for num in arr[i]:
                if num == 0: # 패쓰
                    continue
                # 기준값과 같은 경우
                if num == standard:
                    temp.append(num*2)
                    standard = 0 # 한 번 합쳐진 수는 또 합쳐지지 않기 위해 기준 0으로 초기화
                else: # 다른 경우
                    if standard == 0: # 처음 경우
                        standard = num
                    else:
                        temp.append(standard)
                        standard = num
            if standard != 0: # 딱 맞아 떨어지지 않았다는 뜻이니까
                temp.append(standard) # 마지막에 num 넣어주는 거 잊지 말기
            narr.append(temp+[0]*(n-len(temp))) # 남은 공간 채워주기
        return narr
    
    answer = 0
    def backtracking(depth, board):
        nonlocal answer
        if depth == 5:
            answer = max(answer, max(map(max, board)))
            return
        
        # 좌로 이동
        backtracking(depth+1, move(board))
        # 우로 이동
        right = [row[::-1] for row in board]
        backtracking(depth+1, [row[::-1] for row in move(right)]) # 좌우반전
        # 상으로 이동
        # nboard 전치 필요 (행을 열로, 열을 행으로)
        transpose = list(map(list, zip(*board)))
        backtracking(depth+1, list(map(list, zip(*move(transpose)))))
        # 하로 이동
        down = move([row[::-1] for row in transpose])
        backtracking(depth+1, [row for row in zip(*down)][::-1])

    backtracking(0, origin)  
    print(answer)
solution()