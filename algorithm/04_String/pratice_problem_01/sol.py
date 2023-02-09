import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):
    word = input()
    reverse_word = word[::-1]
    print(f'#{tc}',reverse_word)