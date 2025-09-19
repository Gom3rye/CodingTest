import sys
input = sys.stdin.readline

# 입력 받기
answer = list(map(int, input().split()))
count = 0

def dfs(pos, picked, score):
    global count
    if pos == 10:
        if score >= 5:
            count += 1
        return

    for i in range(1, 6):
        # 연속 3문제 같은 답이면 안 됨
        if pos >= 2 and picked[pos - 1] == picked[pos - 2] == i:
            continue
        picked.append(i)
        if i == answer[pos]:
            dfs(pos + 1, picked, score + 1)
        else:
            dfs(pos + 1, picked, score)
        picked.pop()

dfs(0, [], 0)
print(count)
