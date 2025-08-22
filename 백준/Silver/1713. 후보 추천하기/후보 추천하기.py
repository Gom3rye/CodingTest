import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    rec = int(input())
    students = list(map(int, input().split()))
    result = dict() # result[ppl] = count
    # 추천수가 똑같다면 먼저 들어온 순으로 빼야 하니까 순서도 중요
    for i in range(rec):
        if len(result) < n:
            if students[i] in result:
                result[students[i]] += 1
            else:
                result[students[i]] = 1
        else:
            # 이미 result에 있는 사람이라면 count값만 올려주기
            if students[i] in result:
                result[students[i]] += 1
            else:
                min_count = float('inf')
                for ppl in result:
                    min_count = min(min_count, result[ppl])
                for ppl in result:
                    if result[ppl] == min_count:
                        del result[ppl]
                        result[students[i]] = 1
                        break
    print(*sorted(result))
solution()