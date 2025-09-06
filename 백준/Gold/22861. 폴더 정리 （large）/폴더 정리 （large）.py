import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

def solution():
    # ------------------ Helper Functions (솔루션 함수 내부에 정의) ------------------

    # 경로를 이용해 폴더 딕셔너리를 찾는 함수
    def get_folder_by_path(root, path_list):
        curr = root
        for folder_name in path_list:
            if folder_name == 'main':
                continue
            # 클래스의 .subfolders 대신 ['subfolders'] 키로 접근
            curr = curr['subfolders'][folder_name]
        return curr

    # 쿼리 기능을 위한 재귀 카운트 함수
    def count_files(folder_dict):
        # 클래스의 .files 대신 ['files'] 키로 접근
        unique_files = set(folder_dict['files'])
        total_count = len(folder_dict['files'])
        
        # 클래스의 .subfolders 대신 ['subfolders'] 키로 접근
        for subfolder in folder_dict['subfolders'].values():
            sub_uniques, sub_total = count_files(subfolder)
            unique_files.update(sub_uniques)
            total_count += sub_total
            
        return unique_files, total_count

    # 폴더 이동(병합)을 위한 재귀 함수
    def merge_folders(source_dict, dest_dict):
        # 파일 병합
        dest_dict['files'].update(source_dict['files'])
        
        # 하위 폴더 병합
        for name, sub_source_dict in source_dict['subfolders'].items():
            if name in dest_dict['subfolders']:
                merge_folders(sub_source_dict, dest_dict['subfolders'][name])
            else:
                dest_dict['subfolders'][name] = sub_source_dict

    # ------------------ Main Logic (솔루션 함수 본문) ------------------

    N, M = map(int, input().split())

    # 'main' 폴더를 딕셔너리로 생성
    root = {'subfolders': {}, 'files': set()}
    all_folders = {'main': root}
    
    relations = []
    for _ in range(N + M):
        P, F, C = input().split()
        relations.append((P, F, C))
        if C == '1': # 폴더일 경우 미리 빈 딕셔너리 생성
            all_folders[F] = {'subfolders': {}, 'files': set()}
    
    for P, F, C in relations:
        parent_folder = all_folders[P]
        if C == '1':
            parent_folder['subfolders'][F] = all_folders[F]
        else:
            parent_folder['files'].add(F)
            
    K = int(input())
    for _ in range(K):
        path_a_str, path_b_str = input().split()
        path_a = path_a_str.split('/')
        path_b = path_b_str.split('/')
        
        folder_a = get_folder_by_path(root, path_a)
        folder_b = get_folder_by_path(root, path_b)
        
        parent_a_path = path_a[:-1]
        parent_a = get_folder_by_path(root, parent_a_path)
        
        merge_folders(folder_a, folder_b)
        
        del parent_a['subfolders'][path_a[-1]]

    Q = int(input())
    for _ in range(Q):
        query_path_str = input().strip()
        query_path = query_path_str.split('/')
        target_folder = get_folder_by_path(root, query_path)
        
        unique_set, total_num = count_files(target_folder)
        print(len(unique_set), total_num)

# 함수 호출
solution()