import sys
sys.stdin=open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):

    N = int(input()) # 수열의 길이
    squence_list = list(map(int, input()))

    count = 0
    result = 0

    for i in squence_list:
        if i == 0:
            count = 0
        else:
            count += 1
            if count >= result:
                result = count

    print(f'#{tc} {result}')
