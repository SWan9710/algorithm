import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1,test_case+1):
    N, K = map(int, input().split()) # 배열의 수, 단어의 길이

    # 가로
    row_arr =[]
    for i in range(N):
        row_arr.append(list(map(int, input().split())))
    # print(row_arr)

    # 세로
    column_arr = [[0] * N for _ in range(N)]
    for i in range(N):
         for j in range(N):
            column_arr[i][j] = row_arr[j][i]
    # print(column_arr)

    row_result = 0
    col_result = 0

    for i in range(N):
        count = 0
        for j in range(1, N):
            # 연속된 숫자가 1일때
            if row_arr[i][j-1] == row_arr[i][j] == 1:
                count += 1
                # 연속된 숫자가 1이므로 마지막 자리도 1
                # 마지막 비교하는데 1의 갯수가 K-1이면 결과값을 1더해줌
                if j == (N-1) and count == (K-1):
                    row_result += 1

            # 연속된 숫자가 다를때 >> 1 0
            else:
                # 현재 들고온 수가 1인지를 확인
                # if문 통과조건이 이전수와 지금수를 비교하는데 둘다 1일경우이므로
                # 이전까지 if문을 통과했다면 count == K - 1 이어야 함
                if count == K - 1:
                    row_result += 1
                    # 비교수가 0 이므로 count 초기화
                    count = 0
                # 들고오는 수가 0 0 이거나 0 1 인 경우
                else:
                    count = 0

    for i in range(N):
        count = 0
        for j in range(1, N):
            # 연속된 숫자가 1일때
            if column_arr[i][j - 1] == column_arr[i][j] == 1:
                count += 1
                # 연속된 숫자가 1이므로 마지막 자리도 1
                # 마지막 비교하는데 1의 갯수가 K-1이면 결과값을 1더해줌
                if j == (N - 1) and count == (K - 1):
                    col_result += 1

            # 연속된 숫자가 다를때 >> 1 0
            else:
                # 현재 들고온 수가 1인지를 확인
                # if문 통과조건이 이전수와 지금수를 비교하는데 둘다 1일경우이므로
                # 이전까지 if문을 통과했다면 count == K - 1 이어야 함
                if count == K - 1:
                    col_result += 1
                    # 비교수가 0 이므로 count 초기화
                    count = 0
                # 들고오는 수가 0 0 이거나 0 1 인 경우
                else:
                    count = 0
    print(f'#{tc} {row_result + col_result}')