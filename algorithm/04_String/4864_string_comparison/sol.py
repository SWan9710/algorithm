import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):
    first_word = input()
    second_word = input()

    # in연산자 쓰지 않고 풀어보기
    new_arr = []
    for i in range(len(second_word)-len(first_word)+1):
        if second_word[i:i+len(first_word)] == first_word:
            new_arr.append(1)
        else:
            new_arr.append(0)

    if sum(new_arr) != 0:
        print(f'#{tc}',1)
    else:
        print(f'#{tc}',0)

    #in 연산자를 사용할 경우

    # if first_word in second_word:
    #     print(f'#{tc}',1)
    # else:
    #     print(f'#{tc}',0)