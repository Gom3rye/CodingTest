import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    answer = []
    for second in range(1, n+1): # 가능한 모든 두 번째 수 시도(조건이 양의 정수이므로 두 번째 수는 첫 번째 수보다 작거나 같아야 한다.)
        seq = [n, second]
        while True:
            third = seq[-2] - seq[-1]
            if third >= 0:
                seq.append(third)
            else:
                break
        if len(answer) < len(seq):
            answer = seq
    print(len(answer))
    print(*answer)  
solution()