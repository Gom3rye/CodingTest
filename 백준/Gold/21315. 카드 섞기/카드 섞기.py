import sys

# (2, K) 섞기를 수행하는 재귀 함수
def shuffle(deck, k):
    """
    주어진 deck에 대해 (2, k) 섞기를 수행하고 결과 리스트를 반환합니다.
    - deck: 카드 리스트
    - k: 섞기 파라미터 K
    """
    # k=0일 때가 재귀의 기반(base case)이 될 수 있지만,
    # 문제의 정의는 k+1 단계로 이루어져 있으므로, k=1부터 시작하는 재귀로 생각하는 것이 더 자연스럽다.
    # 하지만 2^(k-i+1) 형태를 보면 k에서 1씩 줄어드는 구조이므로 재귀가 가장 깔끔하다.
    
    # 떼어낼 카드 수
    num_to_take = 2**k

    # 2^k가 현재 덱 길이보다 크면 연산 불가 (문제 제약상 이런 경우는 없지만 방어 코드)
    if len(deck) < num_to_take:
        return deck

    # 밑에서 2^k장을 떼어낸 뭉치
    bottom_part = deck[-num_to_take:]
    # 나머지 윗 부분
    top_part = deck[:-num_to_take]

    # k=1부터 시작하므로, k-1 > 0일 때만 재귀 호출
    if k > 0:
        # 떼어낸 뭉치에 대해 (2, k-1) 섞기를 수행
        shuffled_bottom = shuffle(bottom_part, k - 1)
        # 결과적으로 섞인 뭉치를 나머지 위에 얹음
        return shuffled_bottom + top_part
    else:
        # k=0 이면, 2^0=1장만 밑에서 위로 올림. 이것이 재귀의 가장 마지막 단계.
        return bottom_part + top_part


def solution():
    input = sys.stdin.readline
    N = int(input())
    final_deck = list(map(int, input().split()))

    # 초기 상태의 덱
    initial_deck = list(range(1, N + 1))

    # K가 될 수 있는 값들의 범위 찾기
    possible_k = []
    k = 1
    while True:
        if 2**k >= N:
            break
        possible_k.append(k)
        k += 1

    # 2. 모든 (K1, K2) 조합에 대한 완전 탐색
    for k1 in possible_k:
        for k2 in possible_k:
            # 첫 번째 섞기
            deck_after_k1 = shuffle(initial_deck, k1)
            # 두 번째 섞기
            deck_after_k2 = shuffle(deck_after_k1, k2)

            # 최종 결과가 입력과 일치하는지 확인
            if deck_after_k2 == final_deck:
                print(k1, k2)
                return

solution()