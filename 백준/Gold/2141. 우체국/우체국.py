import sys
input = sys.stdin.readline
def solution():
    # 중앙값 찾기: 중앙값을 기준으로 왼쪽, 오른쪽은 절반
    n = int(input()) # <= 100,000
    infos = []
    total_ppl = 0
    for _ in range(n):
        x, a = map(int, input().split())
        total_ppl += a
        infos.append((x, a))
    
    infos.sort(key=lambda x: x[0]) 
    # 마을위치, 사람수 <= 1,000,000,000
    target_ppl = (total_ppl+1)//2
    median = 0
    for x, a in infos:
        median += a
        if median >= target_ppl:
            print(x)
            break
solution()