import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    total_word, pattern_word = input().rstrip().split()

    count = 0
    P_idx = 0
    T_idx = 0
    while T_idx < len(total_word): # 0 ~ 6 까지 반복할때

        # asaksusa 의 a값과 sa의 s 값이 다르면
        if total_word[T_idx] != pattern_word[P_idx]:

            # 토탈워드의 값을 초기화 하고 다음패턴 검색
            T_idx = T_idx - P_idx

            # 패턴워드의 인덱스는 처음부터 검사 할것이기
            # 때문에 0값으로 만들어 주기 위해 -1지정
            P_idx = -1

        # 다음 문자열인 s 와 s 를 비교하기 위해 1씩 증가
        P_idx += 1
        T_idx += 1

        # 모든 패턴에 대해서 조사를 마쳤다면
        if P_idx == len(pattern_word):

            # 전체 문자열에서 패턴이 들어가는 횟수 1증가하고
            count += 1
            # 다시 다음값을 조사하기 위해 패턴의 자리 초기화
            P_idx = 0
    # print(f'#{tc}',count)

    word_length = len(total_word) - (count * len(pattern_word))
    print(f'#{tc}',word_length + count)

