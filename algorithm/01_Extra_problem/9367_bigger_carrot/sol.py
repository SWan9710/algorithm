import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):
    N = int(input())
    carrot_list = list(map(int, input().split()))

    result = 1
    count = 1
    for i in range(1,len(carrot_list)):
        if carrot_list[i-1] < carrot_list[i]:
            count += 1
            if count > result:
                result = count
        else:
            count = 1
    print(f'#{tc} {result}')
