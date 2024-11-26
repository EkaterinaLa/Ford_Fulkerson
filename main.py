'''https://it.kgsu.ru/Algorithms/alg063.html'''


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = [s] 
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

                    if ind == t:
                        return True

        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')

            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow


g = Graph(6)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 10)
g.add_edge(1, 3, 4)
g.add_edge(1, 4, 8)
g.add_edge(2, 4, 9)
g.add_edge(1, 2, 2)
g.add_edge(4, 3, 6)
g.add_edge(4, 5, 10)
g.add_edge(3, 5, 10)


source = 0
sink = 5

print(g.ford_fulkerson(source, sink))
