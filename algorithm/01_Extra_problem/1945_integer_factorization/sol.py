import sys
sys.stdin=open('input.txt')

divs = [2, 3, 5, 7, 11]
test_case = int(input())
for tc in range(1, test_case+1):

    N = int(input())
    count = [0] * 5 # 구해야 하는 값의 갯수는 2, 3, 5, 7, 11로 5개

    for i in range(len(divs)):
        while N % divs[i] == 0:
            count[i] += 1
            N //= divs[i]

    result = ''
    for i in range(len(count)):
        result += str(count[i])
    t_result =' '.join(result)

    print(f'#{tc}',t_result)

