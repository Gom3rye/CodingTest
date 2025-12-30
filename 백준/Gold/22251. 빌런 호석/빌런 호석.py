import sys
input = sys.stdin.readline
def solution():
    n, k, p, x = map(int, input().split()) # 최대 층, 자리 수 <=6, 반전시킬 수 있는 최대 횟수 <=42, 엘베 실제 위치(층) <10^k
    # 호석이가 반전시킬 led를 고를 수 있는 경우의 수 계산
    # digit에 맞게 1(켜짐), 0(꺼짐) 표시해주기
    digits = [
        '1110111', # 0
        '0010010', # 1
        '1011101', # 2
        '1011011', # 3
        '0111010', # 4
        '1101011', # 5
        '1101111', # 6
        '1010010', # 7
        '1111111', # 8
        '1111011', # 9
    ]
    # 자리수가 6자리니까 브루트포스 가능
    # diff[i][j]: i->j로 가기 위해 몇 digit을 바꾸어야 하는지 미리 구해놓자
    diff = [[0]*10 for _ in range(10)] # 0~9까지
    for i in range(10):
        for j in range(10): # i==j를 기준으로 데칼코마니
            if i == j:
                continue
            for th in range(7): # 0~6까지 digit위치 있다.
                diff[i][j] += 1 if digits[i][th] != digits[j][th] else 0

    answer = 0
    now = str(x).zfill(k) # k자리 수로 zero넣어서 맞추기 (rjust(k, '0')과 같음)
    for floor in range(1, n+1):
        if floor == x: # 현재 위치는 pass
            continue
        comparison = str(floor).zfill(k)
        cnt = 0
        for th in range(k):
            cnt += diff[int(now[th])][int(comparison[th])]
        answer += 1 if cnt <= p else 0
    print(answer)
solution()