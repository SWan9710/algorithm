import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    _ = int(input())
    # 100 * 100 배열의 양 끝에 0을 추가해주기
    arr = [[0]+list(map(int, input().split())) + [0] for _ in range(100)]

    # 최솟값 설정
    min_v = 100*100

    # 양 끝에 0값이 있으므로 시작지점은 1부터 100까지
    for y in range(1, 101):
        # x 값을 0으로 초기화
        x = 0
        # [1] 시작지점 찾기
        if arr[x][y] != 1:      # arr[0][1] ~ arr[0][100] 중에 0값이 올때는 건너뛰기
            continue

        count, dj = 0, 0    # 좌표값 count
        dx, dy = x, y
        while dx < 99:      # >> x값이 내려가는 값이므로 끝까지 내려갈때 까지 반복
            count += 1      # >> 사다리의 이동횟수 += 1
            if dj == 0:

                if arr[dx][dy-1] == 1:      # 왼쪽검사 왼쪽에 1이있으면
                    dj -= 1                 # dj 값을 한칸씩 왼쪽으로 당김
                    dy -= 1                 # 왼쪽으로 1칸이동

                # 오른쪽 검사
                elif arr[dx][dy+1] == 1:    # 오른쪽에 1이 있으면
                    dj += 1                 # 오른쪽으로 1칸 이동
                    dy += 1                 # 오른쪽으로 1칸 이동

                # 양쪽모두 0인 경우
                else:
                    dx += 1                 # 아래로 한칸 내리기

            # dj값이 0이 아닌경우
            else:
                if arr[dx][dy+dj] == 0:     # 왼쪽이나 오른쪽으로 한칸 이동
                                            # 후 그 옆에 칸이 막힌경우
                    dj = 0                  # dj 값 초기화
                    dx += 1                 # 아래로 한칸 내리기

            dy += dj                        # dy값에 dj값을 더해줌
        if min_v >= count:
            min_v, ans = count, y-1         # 현재의 이동횟수를 min_v에 넣고
                                            # 좌표값에서 -1한값이 진짜 좌표이므로 ans에 넣어줌
    print(f'#{tc} {ans}')