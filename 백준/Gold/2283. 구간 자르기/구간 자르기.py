# import sys
# input = sys.stdin.readline
# def solution():
#     n, k = map(int, input().split()) # 구간 <=1000, 남는 길이의 총합 <=10^9
#     # 딱 k가 되도록 만드는 a, b 출력 & if not, 0 0 출력
#     # 중요한 점: 양 끝점의 위치는 0 이상 1,000,000 이하의 정수이다.
#     # 변수가 2개 필요 -> a, b
#     distance = []
#     max_right = 0
#     for _ in range(n):
#         left, right = map(int, input().split())
#         distance.append([left, right])
#         max_right = max(max_right, right)
#     start, end = 0, max_right
#     mid = (start+end)//2 # mid: a<->b 사이의 중간값
#     start_mid = (start+mid)//2 # a
#     end_mid = (mid+end)//2 # b
#     while start_mid <= end_mid:
#         total = 0
#         for s, e in distance:
#             start_dist = max(s, start_mid)
#             end_dist = min(e, end_mid)
#             total += end_dist-start_dist
#         if total == k:
#             print(start_mid, end_mid)
#         elif total < k: # 더 많이 짜른 것
#             end = mid+1
#         else:
#             start = mid-1

# solution()


import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    vertical = [0]*1000001
    for _ in range(n):
        start, end = map(int, input().split())
        for i in range(start, end):
            vertical[i] += 1

    left, right, val = 0, 0, 0
    while 0<=left<=right and right <1000001:
        if val == k:
            print(left, right, sep=' ')
            return
        elif val < k:
            val += vertical[right]
            right += 1
        else:
            val -= vertical[left]
            left += 1
    print('0 0')
solution()
