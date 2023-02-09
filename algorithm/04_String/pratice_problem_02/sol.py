import sys
sys.stdin = open('input.txt')

for tc in range(1, 7):
    num = input()
    print(f'#{tc} {num} {type(num)}')