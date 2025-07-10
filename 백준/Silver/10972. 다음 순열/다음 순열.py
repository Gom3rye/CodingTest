import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n-1, 0, -1): # n-1 ~ 1까지
        if arr[i] > arr[i-1]: # 오른쪽에서부터 보면서 처음으로 자기 왼쪽 수가 자기보다 작아진 부분 찾기
            # arr[i-1]보다 큰 값 중 가장 작은 값을 찾는다. (arr[i:]는 내림차순이므로 끝부분에서 부터 확인하면 된다.)
            for j in range(n-1, 0, -1):
                if arr[i-1] < arr[j]:
                    # arr[j]가 해당하는 값이므로
                    arr[i-1], arr[j] = arr[j], arr[i-1]
                    # arr[i:].sort() -> 복사된 새 리스트라서 영향 x
                    arr[i:] = reversed(arr[i:]) # 가장 작은 값이 맨 뒤에 있고 다른 것들은 다 내림차순으로 되어 있는 상태니까 reverse 하면 오름차순으로 정렬된다.
                    # 또는 arr[i:] = sorted(arr[i:])
                    print(*arr)
                    sys.exit()
    print(-1)
solution()
