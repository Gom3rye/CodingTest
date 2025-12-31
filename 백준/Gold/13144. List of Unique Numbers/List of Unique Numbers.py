import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # <=100,000
    arr = list(map(int, input().split()))
   
    # end를 끝으로 하는 부분 수열 개수 구하기! -> [start, end]에서 end를 끝으로 하는 연속 부분 수열의 개수는 end-start+1
    start, answer = 0, 0
    visited = [False]*(n+1)
    for end in range(n):
        num = arr[end]
        if not visited[num]:
            visited[num] = True
            answer += (end-start+1)
        else:
            while True:
                target = arr[start]
                if target == arr[end]:
                    start += 1
                    answer += (end-start+1)
                    break
                visited[target] = False
                start += 1 # 하나씩 빼기
    print(answer)
solution()