import sys
sys.stdin = open('input.txt')

test_case = 10
for tc in range(1, test_case+1):

    N = int(input())
    ladder_arr = [list(map(int, input().split())) for _ in range(100)]
    min_v = 100000


    for i in range(100):
        if ladder_arr[0][i] == 0:
            continue
        x = 0
        y = i
        count = 0
        while True:
            # 오른쪽 검사
            if y < 100 and ladder_arr[x][y + 1] == 1:
                while y < 100 and ladder_arr[x][y+1] == 1:
                    y += 1
                # 오른쪽에 0이 왔을때
                else:
                    count += 1
                    x += 1  # 아래로 한칸 내려가기

            # 왼쪽 검사
            elif y > 0 and ladder_arr[x][y - 1] == 1:
                while y > 0 and ladder_arr[x][y-1] == 1:
                    y -= 1
                else:
                    count += 1
                    x += 1

            # 아래로 내려가기
            else:
                x += 1
            if x == 100:
                break
        if min_v >= count:
            min_v = count

        print(min_v)