import sys
input = sys.stdin.readline
def solution():
    # 줄의 마지막 아이가 타게 될 놀이기구의 번호
    n, m = map(int, input().split()) # #아이들 <=2,000,000,000, #놀이기구 종류 <=10000
    time = list(map(int, input().split())) # 기구의 운영 시간 0based index
    if n <= m:
        print(n)
        return
    max_time = max(time)
    answer, start, end = -1, 1, max_time*n
    while start <= end:
        mid = (start+end)//2
        cnt = m # 0분에 m개의 기구 모두 채울 수 있으니까
        for t in time:
            cnt += mid//t
            if cnt >= n:
                answer = mid # 모든 아이를 태운 최소 시간
                end = mid - 1
                break
        else:
            start = mid + 1
    
    # 마지막 아이가 어느 놀이기구에 탔는지 알아보기 위해 최소 시간-1분까지는 몇 명이 탔는지 확인
    ppl = m
    for t in time:
        ppl += (answer-1)//t
    
    for i in range(m):
        if answer%time[i] == 0: # 딱 떨어지면 answer시간에 한 명을 태울 수 있다는 소리
            ppl += 1
            if ppl == n:
                print(i+1) # 1based index
                break
    
solution()