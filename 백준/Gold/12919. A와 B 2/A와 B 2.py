import sys
input = sys.stdin.readline
def solution():
    start = input().strip()
    target = input().strip()
    # 이미 완성된 target -> start로 가는게 start -> target으로 가는 것보다 쉬우므로 반대로 계산
    def dfs(t):
        if t == start:
            return True
        if len(t) < len(start): # t길이가 start보다 짧아지면 실패
            return False
        # A로 끝나는 경우
        if t[-1] == 'A':
            if dfs(t[:-1]):
                return True # 'A'추가 -> 'A' 빼고 다시 호출
        # B로 시작하는 경우 (B를 끝에 추가하고 뒤집은 상태니까 B는 처음에 있을 것)
        if t[0] == 'B':
            if dfs(t[::-1][:-1]): # 'B'추가, 뒤집기 -> 뒤집기, B빼기
                return True
        
        return False

    if dfs(target):
        print(1)
    else:
        print(0)
solution()