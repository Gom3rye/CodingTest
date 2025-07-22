import sys
input = sys.stdin.readline
from collections import defaultdict
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    tickets.sort(reverse=True) # pop연산을 통해 알파벳 순서가 앞서도록
    
    for start, end in tickets:
        graph[start].append(end)

    def backtracking(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()
            backtracking(next_airport)
        answer.append(airport)
    backtracking('ICN')    
    return answer[::-1]