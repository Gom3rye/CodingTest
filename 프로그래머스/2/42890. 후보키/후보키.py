from itertools import combinations

def solution(relation):
    """
    주어진 릴레이션에서 후보 키의 개수를 찾는 함수

    Args:
        relation: 릴레이션을 나타내는 2차원 문자열 배열

    Returns:
        후보 키의 개수 (정수)
    """
    row_count = len(relation)
    col_count = len(relation[0])
    
    # 1. 가능한 모든 속성(컬럼) 조합 생성
    # 1개부터 col_count개까지의 모든 조합을 구함
    possible_keys = []
    for i in range(1, col_count + 1):
        possible_keys.extend(combinations(range(col_count), i))
        
    # 최종 후보 키를 저장할 리스트
    candidate_keys = []
    
    # 2. 각 조합을 순회하며 유일성과 최소성 검사
    for p_key in possible_keys:
        # 3. 유일성(Uniqueness) 검사
        # p_key에 해당하는 컬럼 값들로 튜플을 만들어 set에 저장
        temp_set = set()
        for row in relation:
            temp_tuple = tuple(row[col_idx] for col_idx in p_key)
            temp_set.add(temp_tuple)
        
        # set의 크기가 전체 행의 수와 같다면, 이 조합은 유일성을 만족함
        if len(temp_set) == row_count:
            is_minimal = True
            
            # 4. 최소성(Minimality) 검사
            # 현재 유일성을 만족하는 p_key가 이전에 찾은 후보 키를 포함하는지 확인
            # 만약 포함한다면, 현재 키는 최소성을 만족하지 못함
            for c_key in candidate_keys:
                if set(c_key).issubset(set(p_key)):
                    is_minimal = False
                    break
            
            # 유일성과 최소성을 모두 만족하면 후보 키로 추가
            if is_minimal:
                candidate_keys.append(p_key)

    return len(candidate_keys)