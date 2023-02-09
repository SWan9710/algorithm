import sys
sys.stdin = open('input.txt', encoding='utf-8')

for N in range(10):
    tc = int(input())
    pattern_word = input()
    target_word = input()

    # 조사 하려고 하는 두 대상의 조사 대상을 내가 직접 컨트롤 하는
    # 이덱스로 조절하면서 비교하겠다.
    P_idx = 0
    T_idx = 0

    #최종결과값
    count = 0

    # 순회 횟수
    while T_idx < len(target_word):
        # 두 값이 같으면 idx를 늘리기
        # if target_word[T_idx] == pattern_word[P_idx]:
        #     P_idx += 1
        #     T_idx += 1

        if target_word[T_idx] != pattern_word[P_idx]:
            T_idx = T_idx - P_idx
            P_idx = -1
        P_idx += 1
        T_idx += 1

        # 모든 패턴에 대해서 조사를 마쳤다면
        if P_idx == len(pattern_word):
            count += 1
            P_idx = 0
    print(f'#{tc}',count)