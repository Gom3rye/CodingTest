import sys; input = sys.stdin.readline
document = input().rstrip()
search = input().rstrip()
cnt = 0
idx = 0
for i in range(len(document) - len(search)+1):
    for j in range(len(search)):
        if document[i+j] != search[j] or i<idx:
            break
    else:
        cnt += 1
        idx = i+len(search)
print(cnt)