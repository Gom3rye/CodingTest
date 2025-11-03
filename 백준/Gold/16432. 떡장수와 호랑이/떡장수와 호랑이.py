# DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N = int(input())

lst = list()
check_dict_lst = [[False]*10 for _ in range(N)]

for i in range(N):
    temp_lst = list(map(int ,input().split()))
    lst.append(temp_lst[1:])

def dfs(day, ricecake_lst):
    global lst
    global check_dict_lst

    if day == N:
        for ricecake in range(1, len(ricecake_lst)):
            print(ricecake_lst[ricecake])
        exit(0)
        return

    for i in range(len(lst[day])):
        if ricecake_lst[-1] == lst[day][i]:
            continue
        if check_dict_lst[day][lst[day][i]]:
            continue
        check_dict_lst[day][lst[day][i]] = True
        ricecake_lst.append(lst[day][i])
        dfs(day+1, ricecake_lst)
        ricecake_lst.pop()
    return
dfs(0, [-1])
print(-1)