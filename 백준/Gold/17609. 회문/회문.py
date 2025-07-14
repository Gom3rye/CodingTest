import sys
input = sys.stdin.readline
def solution():
    t = int(input())
    words = [input().strip() for _ in range(t)]
    result = []
    def check(word, start, end):
        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        return True

    for i in range(t):
        word = words[i]
        n = len(word)
        chance = 0
        start, end = 0, n-1
        ispalindrome = True
        while start < end:
            if word[start] != word[end]:
                ispalindrome = False
                # start를 빼거나 end를 빼야 한다.
                if check(word, start+1, end) or check(word, start, end-1):
                    result.append("1")
                else:
                    result.append("2")
                break

            start += 1
            end -= 1

        if ispalindrome:
            result.append("0")

    print("\n".join(result))

solution()