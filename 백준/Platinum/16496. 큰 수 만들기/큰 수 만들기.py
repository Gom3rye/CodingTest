import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #리스트 원소 <=1000
    arr = list(input().split())
    arr.sort(key=lambda x: x*10, reverse=True)
    answer = ''.join(arr)
    print(answer if answer[0] != '0' else 0)
solution()