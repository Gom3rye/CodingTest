import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # #책 <=50, 한번에 들고 갈 수 있는 책 <=50
    books = list(map(int, input().split()))
    neg, pos = [], []
    for book in books:
        if book < 0:
            neg.append(-book) # 절댓값으로 넣기
        else:
            pos.append(book)
    neg.sort(reverse=True)
    pos.sort(reverse=True)
    # 모든 이동은 왕복을 하되, 가장 먼곳은 편도로 가야 한다.
    farthest = 0
    if neg:
        farthest = max(farthest, neg[0])
    if pos:
        farthest = max(farthest, pos[0])
    nn, np = len(neg), len(pos)
    min_cost = 0
    for i in range(0, nn, m):
        min_cost += neg[i]*2
    for i in range(0, np, m):
        min_cost += pos[i]*2
    min_cost -= farthest
    print(min_cost)
solution()