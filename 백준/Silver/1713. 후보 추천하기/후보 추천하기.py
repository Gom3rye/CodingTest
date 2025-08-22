import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    rec = int(input())
    students = list(map(int, input().split()))
    result = dict() # result[stu] = [count, idx]
    for idx, stu in enumerate(students):
        if stu in result:
            result[stu][0] += 1
        else:
            if len(result) < n:
                result[stu] = [1, idx]
            else:
                # count가 젤 적고 time이 idx가 젤 작은 사람 out
                ready_to_out_stu = sorted(result.items(), key=lambda x: (x[1][0], x[1][1]))[0][0]
                del result[ready_to_out_stu]
                result[stu] = [1, idx]
    print(*sorted(result))
solution()