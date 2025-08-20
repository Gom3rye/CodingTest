def solution(n, k, cmd):
    # 각 행이 자신의 이전/다음 행 인덱스를 가리키는 이중 연결 리스트
    # table[i] = [prev_idx, next_idx]
    # None은 끝을 의미함
    table = {i: [i - 1, i + 1] for i in range(n)}
    table[0][0] = None
    table[n - 1][1] = None
    
    # 현재 선택된 행의 인덱스
    current_k = k
    
    # 삭제된 행을 저장할 스택
    # (삭제된 행 인덱스, 이전 행 인덱스, 다음 행 인덱스)
    deleted_stack = []
    
    for command in cmd:
        parts = command.split()
        op = parts[0]
        
        if op == 'U':
            x = int(parts[1])
            for _ in range(x):
                current_k = table[current_k][0]
        
        elif op == 'D':
            x = int(parts[1])
            for _ in range(x):
                current_k = table[current_k][1]
        
        elif op == 'C':
            # 1. 현재 노드의 이전/다음 노드 인덱스를 가져옴
            prev_idx, next_idx = table[current_k]
            
            # 2. 삭제 정보 스택에 저장
            deleted_stack.append((current_k, prev_idx, next_idx))
            
            # 3. 연결 리스트에서 현재 노드 제거
            if prev_idx is not None:
                table[prev_idx][1] = next_idx
            if next_idx is not None:
                table[next_idx][0] = prev_idx
            
            # 4. 현재 선택 위치(k) 변경
            if next_idx is not None:
                current_k = next_idx
            else: # 마지막 행을 삭제한 경우
                current_k = prev_idx

        elif op == 'Z':
            # 1. 가장 최근에 삭제된 정보 복구
            restored_idx, prev_idx, next_idx = deleted_stack.pop()
            
            # 2. 끊어졌던 연결을 다시 복구
            if prev_idx is not None:
                table[prev_idx][1] = restored_idx
            if next_idx is not None:
                table[next_idx][0] = restored_idx

    # 최종 결과 생성
    answer = ['O'] * n
    for idx, _, _ in deleted_stack:
        answer[idx] = 'X'
        
    return "".join(answer)