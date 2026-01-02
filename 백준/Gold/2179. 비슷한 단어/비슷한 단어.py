import sys
input = sys.stdin.readline
# 두 개의 단어들의 최대 공통 접두사 길이를 구해야 하니까 공통접두사 길이 구하는 함수 작성!
def longest_common_prefix(w1, w2):
    n = min(len(w1), len(w2))
    for i in range(n):
        if w1[i] != w2[i]:
            return i
    return n
def solution():
    n = int(input()) # <=20,000
    words = [input().strip() for _ in range(n)]
    # 인접 단어들만 고려하기 위해 알파벳 순서로 정렬하고 이를 통해 바뀐 인덱스 리스트를 만들기!
    # words[i]의 정렬 후 순서는 idx_list[i]
    idx_list = sorted(range(n), key=lambda x: words[x])
    
    # 최대 lcp를 구하기 위한 리스트!-> 양옆의 lcp길이만 구하기(이게 가능한 이유는 사전순으로 정렬했기 때문)
    adj_lcp = [0]*(n-1) # “사전순 정렬된 i번째와 i+1번째 단어 사이의 LCP”
    # max_lcp 구하기
    max_lcp = 0
    for i in range(n-1):
        length = longest_common_prefix(words[idx_list[i]], words[idx_list[i+1]])
        adj_lcp[i] = length
        if max_lcp < length:
            max_lcp = length
    
    # 사전 순으로 정렬된 것과 실제 입력 순서가 다르므로 실제 입력 순서대로 max_lcp에 도달가능한지 보여주는 배열 만들기
    can_reach_max = [False]*n
    for i in range(n-1):
        if adj_lcp[i] == max_lcp:
            can_reach_max[idx_list[i]] = True
            can_reach_max[idx_list[i+1]] = True

    s_idx = -1
    for i in range(n):
        if can_reach_max[i]:
            s_idx = i
            print(words[i])
            break
    
    # 이제 위에서 구한 s와 함게 쌍이 되어 max_lcp를 이루는 t구하기
    for t in range(s_idx+1, n):
        if longest_common_prefix(words[s_idx], words[t]) == max_lcp:
            print(words[t])
            break
solution()