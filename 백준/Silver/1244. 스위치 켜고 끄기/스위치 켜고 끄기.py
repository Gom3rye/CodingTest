import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 스위치의 개수
    status = [0]+list(map(int, input().split())) # 1based index
    m = int(input()) # 학생 수
    for _ in range(m):
        gender, num = map(int, input().split())
        if gender == 1: # 남학생이라면
            times, now = 1, num
            while now <= n:
                status[now] ^= 1  # 상태 toggle
                times += 1
                now = num*times
        else: # 여학생이라면
            times = 1
            status[num] ^= 1
            while 1<=num-times and num+times<=n:
                if status[num-times] == status[num+times]:
                    status[num-times] ^= 1
                    status[num+times] ^= 1
                    times += 1
                else:
                    break
    # 한 줄에 20개씩 출력
    if n > 20:
        for i in range(1, n+1):
            print(status[i], end=' ')
            if (i%20) == 0:
                print()
    else:
        print(*status[1:])
solution()