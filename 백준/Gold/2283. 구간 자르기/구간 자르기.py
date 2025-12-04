import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split()) # 구간 <=1000, 남는 길이의 총합 <=10^9
    # 딱 k가 되도록 만드는 a, b 출력 & if not, 0 0 출력
    # 중요한 점: 양 끝점의 위치는 0 이상 1,000,000 이하의 정수이다.
    MAX = 1000002
    vertical = [0]*MAX
    diff = [0]*MAX
    for _ in range(n):
        start, end = map(int, input().split())
        diff[start] += 1
        diff[end] -= 1
    # print(diff[:20])
    # print()
    vertical[0] = diff[0]
    # 양 끝점이 최대 1,000,000 니까 누적합으로
    for i in range(1, MAX):
        vertical[i] = vertical[i-1]+diff[i]
    # print(vertical[:20])

    # 범위가 10^9니까 O(n)으로 해야 함 -> 투 포인터
    start, length = 0, 0
    for end in range(MAX):
        length += vertical[end]
        while length > k:
            length -= vertical[start]
            start += 1
        if length == k:
            print(start, end+1) # [a,b) 상황이니까 end+1로 출력해서 [a,b]로 만들기
            return
    print("0 0")
solution()