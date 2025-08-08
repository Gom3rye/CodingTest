def solution(friends, gifts):
    # 규칙1: a<->b 주고받은 기록이 있다면 더 많이 준 사람의 선물 +1
    # 규칙2: a<->b 주고받은 기록이 없다면 선물 지수 큰 사람의 선물 +1
    # 규칙3: a<->b 주고받은 기록 없고, 선물 지수도 같다면 +0 (pass)
    
    # 계산하기 편하게 이름을 인덱스로 변환
    friends_name = {name: idx for idx, name in enumerate(friends)}
    n = len(friends)
    # gift_matrix[i][j]: i가 j에게 준 선물 수
    gift_matrix = [[0]*n for _ in range(n)]
    
    # gifs 사용할 수 있는 정보로 바꾸기
    # 선물 지수
    gift_indices = [0]*n
    for gift in gifts:
        giver, receiver = gift.split()
        gift_matrix[friends_name[giver]][friends_name[receiver]] += 1
        gift_indices[friends_name[giver]] += 1
        gift_indices[friends_name[receiver]] -= 1
    # 각 사람이 받게 될 선물 수
    next_gift = [0]*n
    for i in range(n):
        for j in range(i+1, n): # i,j가 교차 되니까 중복되지 않도록 j는 i+1부터 시작
            if gift_matrix[i][j] < gift_matrix[j][i]:
                next_gift[j] += 1
            elif gift_matrix[i][j] > gift_matrix[j][i]:
                next_gift[i] += 1
            else: # gift_matrix[i][j] == gift_matrix[j][i]:
                if gift_indices[i] > gift_indices[j]:
                    next_gift[i] += 1
                elif gift_indices[i] < gift_indices[j]:
                    next_gift[j] += 1
                  
    answer = max(next_gift)
            
    return answer