import sys
input = sys.stdin.readline
def solution():
    # 뒤로 보내는 어린이 수의 최솟값
    n = int(input()) # #어린이 <=1,000,000
    kids = list(map(int, input().split()))
    # 앞이나 뒤로만 보낼 수 있기 때문에 중간에 끼워넣는 건 불가능
    # => 숫자가 연속적이고 인덱스 순서도 유지하는 연속 "LIS" 찾기
    index = [-1]*n
    for i in range(n):
        index[kids[i]-1] = i # 0based index
    # 연속 LIS
    length = 1
    max_len = 1
    for x in range(1, n): # 0~n-1까지 연속적인지 확인
        if index[x] > index[x-1]:
            length += 1
            max_len = max(max_len, length)
        else:
            length = 1 # 다시 length 초기화
    print(n-max_len)
solution()