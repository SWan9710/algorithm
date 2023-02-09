import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):
    word = input()
<<<<<<< HEAD
    reverse_word = word[::-1]
    print(f'#{tc}',reverse_word)
=======

    # 빈 문자열을 만들어 소스의 뒤에서 부터 읽는 방법
    # reverse_word = word[::-1]
    # print(f'#{tc}',reverse_word)

    # Reverse 함수
    # new_word = []
    # for i in range(len(word)):
    #     new_word.append(word[i])
    # new_word.reverse()
    # print(f'#{tc} ',*new_word,sep='')


    # 반복문을 이용해 뒤집는 방법
    reverse_word = ''
    for i in word:
        reverse_word = i + reverse_word
    print(reverse_word)
>>>>>>> f4416a4feb89ca6720a098a41efb00c92baf3c80
