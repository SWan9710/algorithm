import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*(N+2) for _ in range(N+2)]
    # index out of range 오류 안뜨게 처음부터 주변을 0으로 감싸준 배열 생성

    # 시작 지점은 1,1 부터 맨 아래줄은 실행 안할거기때문에 N+1 까지
    for i in range(1,N+1):          # N = 4 => 4까지 반복하기 위해 +1
        for j in range(1,N+1):
            if i == 1 and j == 1:
                # 시작지점 값은 1로 시작하니 1로 지정
                arr[i][j] = 1
            # 1,1 이 아닌 경우에는 대각선 왼쪽 위와 바로 위에 값을 더해서 현재 값으로 넣어줌
            arr[i][j] += (arr[i-1][j-1] + arr[i-1][j])

    # 결과값 출력역시 첫줄과 마지막 줄은 건너 뛸거라 범위를 1부터 N+1 까지 지정
    print(f'#{tc}')
    for i in range(1,N+1):
        for j in range(1,N+1):
            # 0인 값은 출력 안할거기 때문에 continue로 건너뛰기
            if arr[i][j] == 0:
                continue
            # 0이 아닌값은 공백 한칸을 두고 옆으로 출력
            print(arr[i][j],end=' ')
        # 이후 줄바꿔 주기
        print()
