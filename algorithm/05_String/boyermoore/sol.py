import sys
sys.stdin = open('input.txt', encoding='utf-8')

def search(pattern, char):
    # 어디까지 동일한 값을 가지고 있는지 확인할 거
    # 맨뒤는 조사 안할거
    for i in range(len(pattern)-2,-1,-1):
        # 동일한 값이 있다면
        if pattern[i] == char:
            # 그 위치까지 이동하도록 index 번호 넘겨주기
            return  len(pattern)- i - 1

        # 동일한 값이 없다면





def boyer_moore(pattern, target):
    count = 0
    t_idx = 0

    # 조사 범위가 조금 다르다.
    # 조사 대상 idx가 전체 길이 - 패턴길이를 넘기 전까지
    # 보이어 무어는 뒤에서 부터 조사함
    # 전체길이에서 패턴길이 만큼 뺀거만큼 조사할거
    while t_idx <= len(target) - len(pattern):
        # 뒤에서 부터 조사 할거니까 패턴 인덱스의 길이는 패턴의 길이만큼
        p_idx = len(pattern) - 1

        # p_idx가 0이 되기 전까지 반복
        while p_idx >= 0:
            # 두 조사 대상이 같지 않을때
            if pattern[p_idx] != target[t_idx + p_idx]:
                # 다음 조사 위치로 이동하기 위한 값을 만들어야 한다.
                next = search(pattern, target[t_idx + len(pattern) - 1])
                break
            p_idx -= 1
        # 패턴의 끝까지 조사 했다면
        if p_idx == -1:
            count += 1
            t_idx += 1

        # 패턴의 끝까지 조사를 못했다면
        else:
            t_idx += next
    return count



for N in range(10):
    tc = int(input())
    pattern_word = input()
    target_word = input()