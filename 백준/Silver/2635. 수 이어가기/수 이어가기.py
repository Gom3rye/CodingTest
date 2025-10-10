N = int(input())
result = []
for i in range(1, N+1):          # 양의 정수 1부터 N을 포함하는 정수 들 (!!N포함 중요 안할 시 틀림)
    tmp = [N, i]
    while True:
        val = tmp[-2] - tmp[-1]  # 다음 값은 인덱스 -2에서 -1을 뺀 값
        if val >= 0:             # 이 값이 정수라면 넣어주고
            tmp.append(val)
        else:                    # 아니면 break
            break
    if len(tmp) > len(result):   # tmp의 길이가 result보다 클 시
        result = tmp
print(len(result))
for i in result:
    print(i, end=' ')