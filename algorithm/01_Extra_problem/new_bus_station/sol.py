import sys
sys.stdin=open('input.txt')

# 모든 버스는 A번에서 출발해 B번까지 운행하므로, A와 B 정류장에서 반드시 정차한다.
# 일반버스는 A번부터 B번 사이의 모든 정류장에 정차한다.

# 급행버스는 A가 짝수인 경우 A와 B 사이의 모든 4의 배수 번호 정류장에,
# A가 홀수인 경우 A와 B 사이의 모든 홀수 번호 정류장에 정차한다.

# 광역 급행 버스는 A가 짝수인 경우 A와 B의 4의 배수 번호 정류장에
# A가 홀수인 경우 A 와 B 사이의 3의 배수 이면서 10의 배수가 아닌 번호 정류장에 정차한다.

# 첫째줄 테스트 케이스
# 둘째줄 노선의 수
# N개의 줄마다 각각 다른 번호의 버스 타입
# 1 일반, 2 급행, 3 광역 급행
# 버스 번호 후 A 정류장 B 정류장 공백띄고 주어짐

test_case = int(input())
for tc in range(test_case):
    N = int(input())


    for n in range(N):
        bus_information, A, B = map(int, (input().split()))

        # 일반버스 일때
        if bus_information == 1:
            for i in range(A, B+1):
                print(i)

        # 급행버스 일때
        if bus_information == 2:
            for i in range(A, B + 1):
                if A % 2 == 0:
                    if i % 2 == 0:
                        print(i)

                elif A % 2 == 1:
                    if i % 2 == 1:
                        print(i)

        # 광역급행버스 일때
        if bus_information == 3:
            for i in range(A, B + 1):
                if A % 2 == 0:
                    if i % 4 == 0:
                        print(i)

                elif A % 2 == 1:
                    if i % 3 == 0 and i % 10 != 0:
                        print(i)

