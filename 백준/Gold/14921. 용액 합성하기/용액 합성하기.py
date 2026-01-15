import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # <=100,000
    sol = list(map(int, input().split())) # 오름차순으로 주어진다.
    # 가장 0에 가까운 용액 만들기
    start, end = 0, n-1
    candidates = []
    while start < end:
        a, b = sol[start], sol[end]
        answer = a+b
        candidates.append(answer)
        if answer < 0:
            start += 1
        elif answer > 0:
            end -= 1
        else: # answer == 0:
            print(0)
            return
    # candidates 중에서 0이랑 제일 가까운 원소 출력하기
    candidates.sort()
    temp = [abs(val) for val in candidates]
    ans_idx = temp.index(min(temp))
    print(candidates[ans_idx])
solution()