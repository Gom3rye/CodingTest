import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 카드의 개수 <=300,000
    a = list(map(int, input().split()))
    # 얻을 수 있는 최댓값은 연달아 있는 그룹들의 합 중에서 나올 수 있다.
    groups = []
    cnt = 1 # 연속된 횟수
    for i in range(n-1):
        if a[i] == a[i+1]:
            cnt += 1
        else: # 서로 다르다면 그룹에 지금까지 모았던 연속 길이 추가 & 길이 리셋
            groups.append(cnt)
            cnt = 1
    groups.append(cnt) # 마지막 원소 추가
    answer = groups[0]
    for i in range(len(groups)-1):
        answer = max(answer, groups[i]+groups[i+1])
    print(answer)
solution()