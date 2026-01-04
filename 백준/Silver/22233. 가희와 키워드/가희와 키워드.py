import sys
input = sys.stdin.readline
def solution():
    # 글에 있는 키워드의 최대 개수는 10
    n, m = map(int, input().split()) # #키워드, #블로그 글 <=200,000
    # 있는지 없는지 여부를 구하는 계산 -> set 사용해서 O(1)로!
    keywords = set(input().strip() for _ in range(n))
    for _ in range(m):
        keyword = set(input().strip().split(','))
        keywords -= keyword
        print(len(keywords))
solution()