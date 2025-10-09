A = int(input())    # 게임을 진행하는 사람 수
T = int(input())    # T번째 
S = int(input())    # 뻔이면 0, 데기면 1

bcount = 0      # 뻔 개수
gcount = 0      # 데기 개수

cnt = 0         # 회차

N = []          

while True:

    cnt += 1

    for _ in range(2):
        bcount += 1
        N.append((bcount, 0))
        gcount += 1
        N.append((gcount, 1))
    for _ in range(cnt + 1):
        bcount += 1
        N.append((bcount, 0))
    for _ in range(cnt + 1):
        gcount += 1
        N.append((gcount, 1))

    if bcount >= T:
        print(N.index((T, S)) % A)
        break