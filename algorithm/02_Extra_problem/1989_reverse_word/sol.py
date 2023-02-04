import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):

    words = input()
    result_word = ''
    for i in range(len(words)-1,-1,-1):
        result_word += words[i]

    if words == result_word:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
