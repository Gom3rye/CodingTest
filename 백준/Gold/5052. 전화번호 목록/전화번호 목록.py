import sys
input = sys.stdin.readline
def solution():
    t = int(input()) # <=50
    for _ in range(t):
        n = int(input()) # 전화번호 수 <=10000
        phonebook = [input().strip() for _ in range(n)]
        phonebook.sort() # 문자를 사전 순으로 정렬하면 옆의 글자만 보면 된다.
        for i in range(n-1):
            num = phonebook[i]
            if phonebook[i+1].startswith(num):
                print("NO")
                break
        else:
            print("YES")  
solution()