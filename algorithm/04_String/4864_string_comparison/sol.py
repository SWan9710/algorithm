import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):
    first_word = input()
    second_word = input()

    if first_word in second_word:
        print(f'#{tc}',1)
    else:
        print(f'#{tc}',0)

        # in연산자 쓰지 않고 풀어보기