import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1
    print(start, end=' ')

    # 다음 조사 가능 위치 찾기
    for next in range(1, V+1):
        # 인접해있고, => 1번 노드와 붙어 있는 노드중 하나
        # 그 노드 정보는 G에 들어가 잇음
        # G[start][next] => True일때 즉 G 배열의 start와 next 번째에 값이 있는 경우에
        # 그리고 visited[next] 가 값이 없을때때
       if G[start][next] and not visited[next]:
           # 조사를 한다? 는 행위
            DFS(next)


# V = 노드 개수, E = 간선 개수
V, E = map(int, input().split())
# 간선 정보
data = list(map(int, input().split()))
# 방문 표시용 배열 생성
visited = [0] * (V+1)

# 이동 가능 정보를 담기 위한 리스트
# 0번 노드는 쓰지 않고, V번 노드도 필요하므로 V + 1

G = [[0] * (V+1) for _ in range(V+1)]

# 인접 행렬 그리기
for i in range(E):
    # 두개의 노드가 이어져 있는 정보
    n1, n2 = data[i*2], data[i*2+1]
    G[n1][n2] = 1
    G[n2][n1] = 1

# # 위에거를 다른방식으로 표현한거
# for i in range(0, len(data), 2):
#     print(i, i+1)

for mat in G:
    print(mat)
DFS(1)