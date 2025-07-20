import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    weights = list(map(int, input().split()))
    max_energy = [0]  # 리스트로 감싸서 참조로 업데이트 가능하게 함

    def dfs(current, energy):
        if len(current) == 2:  # 앞뒤만 남았을 때 종료
            max_energy[0] = max(max_energy[0], energy)
            return
        
        for i in range(1, len(current) - 1):
            gain = current[i - 1] * current[i + 1]
            removed = current.pop(i)
            dfs(current, energy + gain)
            current.insert(i, removed)  # 원상복구 (백트래킹)

    dfs(weights, 0)
    print(max_energy[0])

solution()
