MAX = 100
queue = []
visited = [0] * MAX

def enqueue(vertex):
    queue.append(vertex)

def dequeue():
    if len(queue) == 0:
        return -1
    return queue.pop(0)

def BFS(graph, startVertex, vertices):
    visited = [0] * vertices

    enqueue(startVertex)
    visited[startVertex] = 1

    print("BFS Traversal:", end=" ")

    while len(queue) != 0:
        currentVertex = dequeue()
        print(currentVertex, end=" ")

        for i in range(vertices):
            if graph[currentVertex][i] == 1 and visited[i] == 0:
                enqueue(i)
                visited[i] = 1

vertices = int(input("Enter number of vertices: "))

graph = []
print("Enter adjacency matrix:")

for i in range(vertices):
    row = list(map(int, input().split()))
    graph.append(row)

startVertex = int(input("Enter starting vertex: "))

BFS(graph, startVertex, vertices)
