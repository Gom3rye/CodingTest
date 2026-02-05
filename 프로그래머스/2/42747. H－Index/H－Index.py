import sys
from bisect import bisect_right, bisect_left
def solution(citations):
    citations.sort() # len(citations) <=1000
    n = len(citations)
    # parametric search로 h찾기!
    answer, start, end = 0, 0, 10000
    while start <= end:
        mid = (start+end)//2 # h의 최댓값
        less, more = bisect_right(citations, mid), n-bisect_left(citations, mid)
        if more >= mid and less <= mid:
            answer = mid
            start = mid+1
        else:
            end = mid-1
    return answer