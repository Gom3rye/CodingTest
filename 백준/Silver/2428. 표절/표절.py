import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #솔루션 <=100,000
    sizes = sorted(map(int, input().split()))
    left, answer = 0, 0 # 한 칸씩 전진하며 탐색-> for문 사용 가능
    for right in range(n):
        # right원소*0.9보다 큰 원소가 될 때까지 left옮기기
        while sizes[left] < sizes[right]*0.9:
            left += 1
        answer += (right-left)
    print(answer)
solution()