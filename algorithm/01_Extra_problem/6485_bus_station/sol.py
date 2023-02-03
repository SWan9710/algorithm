import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):
    N = int(input())

    counts = [0] * 5001                         # 전체 정류장의 수
    for i in range(N):                          # 운행버스의 수
        start, end = map(int, input().split())  # 시작값과 종료값
        for j in range(start, end+1):           # 종료값 자기자신을 포함하기 위해 +1
            counts[j] += 1                      # 시작과 종료 사이의 값에 해당하는
                                                # 정류장 번호에 1을 추가해줌
    P = int(input())                            # P 입력받고
    cj = []                                     # cj번 버스 정류장을 지나는 노선의 수
    for i in range(P):
        p = int(input())                        # c의 1번부터 c의 j번까지
        cj.append(counts[p])                    # 위에서 지나간 버스노선을
                                                # cj배열에 추가해줌
    print(f'#{tc}', *cj)