def solution(stones, k):
    answer = 0
    # 연달아서 0이 k번 나오면 실패
    # 구해야 하는 것: 디딤돌을 건널 수 있는 최대 인원 수 -> mid로 두기 mid명이 건널 수 있을까? Y/N 질문
    def can_cross(ppl):
        count = 0
        for stone in stones:
            if stone-ppl < 0:
                count += 1
            else:
                count = 0 # 연속성 끊김
            if count >= k:
                return False
        return True
        
    left, right = 1, max(stones)
    while left <= right:
        mid = (left+right)//2
        # print(f"mid: {mid}, left:{left}, right:{right}")
        if can_cross(mid):
            answer = mid
            left = mid+1
        else:
            right = mid-1
    return answer