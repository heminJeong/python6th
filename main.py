import sys

def dijkstra(graph, start):
    # 그래프의 정점 개수
    vertices = len(graph)

    # 출발점에서 각 정점까지의 최단 거리를 저장하는 배열
    distances = [sys.maxsize] * vertices

    # 방문한 정점을 표시하는 배열
    visited = [False] * vertices

    # 출발점의 거리는 0으로 설정
    distances[start] = 0

    # 모든 정점을 방문할 때까지 반복
    for _ in range(vertices):
        # 방문하지 않은 정점 중에서 출발점에서 가장 가까운 정점을 선택
        min_distance = sys.maxsize
        min_index = -1
        for v in range(vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_index = v

        # 선택한 정점을 방문한 것으로 표시
        visited[min_index] = True

        # 선택한 정점과 연결된 정점들의 최단 거리를 업데이트
        for v in range(vertices):
            if (
                not visited[v]
                and graph[min_index][v] != 0
                and distances[min_index] + graph[min_index][v] < distances[v]
            ):
                distances[v] = distances[min_index] + graph[min_index][v]

    return distances

# 그래프 예제
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

start_vertex = 0

distances = dijkstra(graph, start_vertex)

print("출발점으로부터의 최단 거리:")
for v in range(len(distances)):
    print(f"{v}: {distances[v]}")
