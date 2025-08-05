import sys
input = sys.stdin.readline
def solution():
    n, c = map(int, input().split()) # n개의 물건, 가방에 최대 c만큼의 무게를 넣을 수 있다.
    weights = list(map(int, input().split()))
    
    # 2**30번의 연산은 시간 초과이지만 2**25번의 연산은 가능 -> 2개의 작은 문제로 나누기 (Meet in the middle)
    group_a = weights[:n//2]
    group_b = weights[n//2:]
    sum_a = []
    sum_b = []

    # 각 그룹의 모든 부분집합의 합을 재귀로 구하기
    def dfs(group, idx, current_sum, sum_list):
        if idx == len(group): # 끝까지 탐색했다면 현재 합을 리스트에 추가
            sum_list.append(current_sum)
            return
        # 현재 물건을 포함하지 않는 경우
        dfs(group, idx+1, current_sum, sum_list)
        # 현재 물건을 포함하는 경우
        # (단, 무게가 c를 초과하지 않을 때만 탐색을 이어간다. -> 가지치기)
        if current_sum + group[idx] <= c:
            dfs(group, idx+1, current_sum+group[idx], sum_list)
   
    # 각 그룹에 대해 함수 호출
    dfs(group_a, 0, 0, sum_a)
    dfs(group_b, 0, 0, sum_b)

    # 두 그룹의 결과를 조합하기 위해 한쪽 리스트를 정렬
    sum_b.sort()

    def binary_search(arr, target):
        # arr에서 target의 위치 찾기(인덱스니까 +1 해서 return해주면 그 인덱스까지의 원소 개수가 됨)
        left, right = 0, len(arr)-1
        # target 보다 작거나 같은 값의 마지막 인덱스를 저장할 변수 (조건 만족하는 원소가 하나도 없을 때 +1 해서 0이 되어야 하니까 -1로 초기화)
        answer = -1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] <= target:
                answer = mid
                left = mid+1
            else:
                right = mid-1
        return answer+1
    
    count = 0
    # A그룹의 각 합에 대해 B그룹에서 가능한 조합의 수를 찾기
    for sa in sum_a:
        # sa와 더했을 때 c를 넘지 않는 b그룹의 원소 수를 찾아야 한다.
        # => 값이 c-sa 이하인 원소 개수 찾기
        target = c-sa
        # 이분 탐색으로 target보다 작거나 같은 원소의 개수 빠르게 찾기
        count += binary_search(sum_b, target)
    print(count)

solution()