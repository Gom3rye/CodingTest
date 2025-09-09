import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    h = list(map(int, input().split()))
    min_diff = float('inf')
    # n^4는 시간 초과
    h.sort() # 왼쪽 포인터를 늘리면 값이 커지고 오른쪽 포인터를 줄이면 값이 작아진다는 단조성을 주기 위해 정렬
    for start in range(n-3):
        for end in range(start+3, n):
            anna = h[start]+h[end] # 안나가 만든 눈사람의 키
            s, e = start+1, end-1
            while s < e:
                elsa = h[s]+h[e]
                min_diff = min(min_diff, abs(anna-elsa))
                if min_diff == 0: # 0이면 종료
                    print(0)
                    return
                # anna가 elsa보다 더 크다면 elsa의 눈사람 크기 키우기
                if anna > elsa:
                    s += 1
                elif anna < elsa: # elsa의 눈사람 크기 줄이기
                    e -= 1

    print(min_diff)
solution()