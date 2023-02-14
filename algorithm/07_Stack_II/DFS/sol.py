import sys
sys.stdin = open('input.txt')

# 문제는 1번 노드에서 출발
def DFS(start):
    stack = [start] # 시작지점
    visited = [0] * (V+1)    # 이전에 방문한 곳은 다시 가지 않도록 체크용 리스트
    # 언제까지 조사 하나?
    while stack:    #스택에 값이 있는동안 조사
        start = stack.pop() # 다음조사 대상을 꺼내서 start로 지정
        # 방문표시할건데
        # 이전번에 방문한적 없다면
        if visited[start] == 0:
            visited[start] = 1
            print(start, end=' ')
            # 현재 위치 start를 기준으로,
            # 0부터 V+1번 노드까지 모두 조사 가능한지 탐색
            for next in range(1, V+1):
                # start에서 next로 이동 가능하고, next를 방문한 적이 없다면
                if G[start][next] == 1 and visited[next] == 0:
                    # 다음 조사 대상에 next를 집어 넣는다
                    stack.append(next)

# V = Voltex 노드 7개
# E = Edge 간선   8개
V, E = map(int, input().split())
# 간선 정보
data = list(map(int, input().split()))

# 이동 가능 정보 2차원 리스트
G = [[0]*(V+1) for _ in range(V+1)]

# 모든 간선의 길이만큼 반복을 할거
for i in range(E):
    '''
    G[1][2] = 1
    G[2][1] = 1
    이동 가능 정보를 담은 G의 인덱스는 각 노드 번호를 의미한다.
    간선 정보 data의 0번째는 => 첫번째 출발 노드
    간선 정보 data의 1번째는 => 첫번째 도착 노드를 의미
    
    G[data[0]][data[1]] = 1
    G[data[1]][data[0]] = 1
    i * 2, 1 * 2+1
    i == 0
    i == 1
    '''
    G[data[i*2]][data[i*2+1]] = 1
    G[data[i*2+1]][data[i*2]] = 1
print()

for i in range(V+1):
    print(G[i])

DFS(1)