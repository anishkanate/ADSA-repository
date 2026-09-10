def prim(graph):
    n = len(graph)
    selected = [False] * n
    selected[0] = True

    total_cost = 0

    for _ in range(n - 1):
        min_weight = float('inf')
        x = y = -1

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < min_weight:
                            min_weight = graph[i][j]
                            x = i
                            y = j

        print(f"{x} -- {y} = {min_weight}")
        total_cost += min_weight
        selected[y] = True

    print("Total cost:", total_cost)


graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 1],
    [6, 8, 1, 0]
]

prim(graph)
