import sys
sys.stdin = open('input.txt')

def DFS(start):
    # start => 0부터 시작

    # 0번째 방문기록 배열에 1을 기록
    visited[start] = 1

    # stack에 [0] 을 넣어줌
    stack = [start]

    # stack에 값이 있는동안 반복문을 계속 수행
    while stack:

        # stack의 마지막 값을 start 값으로 지정하며 stack의 마지막 값을 제거해줌
        start = stack.pop()

        # 종료조건 B가 99에 도착하는 경우를 찾는거니
        # start 값이 99가 되는 순간 1을 반환하며 종료
        if start == 99:
            return 1

        # 노드의 최대 갯수는 98 개 이므로 노드의 갯수를 100으로 잡고 V까지 반복
        for next in range(V):

            # 입력받은 간선정보를 토대로 만든 G배열의 [0][0] 값부터 비교 하는데 방문기록이 1이 아니라면
           if G[start][next] and not visited[next]:

                # 방문기록에 1을 추가하고
                visited[start] = 1

                # stack에 next값을 추가해줌
                stack.append(next)
    # 반복문을 다 돌았는데 조건을 만족하지 못했다면 0을 반환
    return 0

T = 10
for tc in range(1, T+1):
    V = 100
    # 배열의 크기가 100 * 100으로 주어지므로 노드의 갯수는 100개가 되고 도착지점은 99
    # 노드의 갯수는 98개를 넘지 않는다가 있으므로 노드가 있어도 간선이 없다면 길이 연결 안되기 때문에
    # 노드의 갯수를 배열의 크기인 100으로 잡아줌

    # N => 테스트 케이스 넘버
    # E => 간선의 갯수
    N, E = map(int, input().split())

    # 입력받은 간선의 정보
    data = list(map(int, input().split()))

    # 방문기록을 표시할 visited 리스트
    visited = [0] * (V)

    # 이동 가능 정보를 담기 위한 리스트 G 생성
    G = [[0] * V for _ in range(V)]

    # 인접행렬 만들기
    for i in range(E):
        # 간선의 정보가 2개씩 들어오므로 n1과 n2에 홀,짝 번 인덱스를 각각 부여해줌
        n1, n2 = data[i*2], data[i*2+1]
        G[n1][n2] = 1

    # 노드의 시작을 0에서부터 시작하니 DFS[start] 에 0부터 시작
    print(f'#{tc}',DFS(0))