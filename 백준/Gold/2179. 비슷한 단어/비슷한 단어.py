import sys

def get_lcp(s1, s2):
    length = min(len(s1), len(s2))
    for i in range(length):
        if s1[i] != s2[i]:
            return i
    return length

def solution():
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    words = input_data[1:]

    # 1. 인덱스 배열 생성 및 '단어 값' 기준으로 정렬
    # words 리스트를 직접 정렬하지 않고 순서만 담은 idx_list를 정렬함
    idx_list = sorted(range(n), key=lambda i: words[i])

    # 2. 인접한 단어들끼리 LCP를 구하며 전체 최대값(max_val) 찾기
    # 그리고 각 단어가 max_val을 가질 수 있는지 여부를 체크
    max_val = 0
    can_reach_max = [False] * n
    
    # 임시로 LCP 저장 (한 번 더 계산하는 것보다 빠름)
    adj_lcp = [0] * (n - 1)
    for i in range(n - 1):
        lcp = get_lcp(words[idx_list[i]], words[idx_list[i+1]])
        adj_lcp[i] = lcp
        if lcp > max_val:
            max_val = lcp

    # max_val을 가질 수 있는 모든 단어 인덱스 표시
    for i in range(n - 1):
        if adj_lcp[i] == max_val:
            can_reach_max[idx_list[i]] = True
            can_reach_max[idx_list[i+1]] = True

    # 3. 입력 순서대로 S 찾기 (가장 빠른 i)
    # S가 될 수 있는 조건: 이 단어의 인덱스가 can_reach_max에 포함됨
    s_idx = -1
    for i in range(n):
        if can_reach_max[i]:
            s_idx = i
            break
    
    # 4. T 찾기 (s_idx 이후 단어 중 LCP가 max_val인 가장 빠른 j)
    print(words[s_idx])
    for j in range(s_idx + 1, n):
        if get_lcp(words[s_idx], words[j]) == max_val:
            print(words[j])
            break

solution()