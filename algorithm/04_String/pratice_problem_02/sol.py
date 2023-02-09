import sys
sys.stdin = open('input.txt')

<<<<<<< HEAD
for tc in range(1, 7):
    num = input()
    print(f'#{tc} {num} {type(num)}')
=======
def itoa(tc):
    # 입력받은 tc값이 음수일때 minus 변수에 저장
    minus = tc < 0

    # 값을 저장해둘 빈 문자열 temp 생성
    temp = ''

    # 입력받은 tc값이 음수일때 -1을 곱해서 양수로 바꿔줌
    if tc < 0:
        tc = tc * -1

    # tc 값이 양수이고, 나눈 몫이 0 이상일때 계속 반복하며 1의 자리를 계속 찾아줌
    while tc > 0:
        # 입력받은 숫자값의 1의자리를 구한뒤 아스키코드 chr(48) == 0 에 값을 더해주는 형식
        # 거기에 다시 문자열 temp를 뒤에 더해줘서 tc의 10의 자리가 들어갈 공간을 만들어줌
        temp = chr(48 + (tc % 10)) + temp
        tc = tc // 10

    # 입력받은 tc값이 음수인지 양수인지 판별하고 음수일 경우 temp 문자열 앞에 - 부호를 추가해서 출력
    if minus == True:
        temp = '-' + (temp)

    return temp

test_case = int(input())
for t in range(1,test_case+1):
    tc = int(input())
    print(f'#{t}',itoa(tc), type(itoa(tc)))




>>>>>>> f4416a4feb89ca6720a098a41efb00c92baf3c80
