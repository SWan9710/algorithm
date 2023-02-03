import sys
sys.stdin=open('input.txt')

# 첫줄에 테스트케이스 개수 T, 다음 줄부터 테스트케이스별로 첫 줄에
# 수열의 길이 N, 다음 줄에 N개의 0과 1로 구성된 수열이 공백없이 제공
# 1<= T <= 10
# 10 <= N <= 100

# 출력 #과 테스트케이스 번호, 빈칸에 이어 답을 출력

test_case = int(input())
for tc in range(1, test_case+1):
    sequence_range = int(input())
    sequence = list(map(int, input()))

    count = 0
    result = 0
    for i in sequence:
        if i == 1:
            count += 1
            if count >= result:
                result = count
        else:
            count = 0

    print(f'#{tc} {result}')


