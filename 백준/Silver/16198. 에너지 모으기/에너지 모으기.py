import sys
input = sys.stdin.readline
n = int(input()) # 구슬의 개수
w = list(map(int, input().split()))
max_energy = 0
def backtracking(arr, energy):
    global max_energy

    # if energy <= max_energy: # energy는 누적값으로 현재 작아도 나중에 커질 수 있으므로
    #     return
    
    if len(arr) == 2:
        max_energy = max(max_energy, energy)
        return
    
    for i in range(1, len(arr)-1):
        marbles = arr[i-1] * arr[i+1]
        removed = arr.pop(i) # i번째 구술 제거
        backtracking(arr, energy+marbles)
        arr.insert(i, removed)

backtracking(w, 0)
print(max_energy)