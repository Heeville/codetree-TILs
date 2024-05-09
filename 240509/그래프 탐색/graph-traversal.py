from collections import defaultdict

def count_reachable_vertices(N, edges):
    graph = defaultdict(list)
    visited = set()

    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(1)
    return len(visited) - 1 


N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]


result = count_reachable_vertices(N, edges)
print(result)