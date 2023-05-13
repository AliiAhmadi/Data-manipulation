def find_hamiltonian_path(graph):
    n = len(graph)
    if n < 2:
        return graph
    if n == 2:
        return [0, 1] if graph[0][1] else [1, 0]
    if n == 3:
        if graph[0][1] and graph[1][2] and not graph[0][2]:
            return [0, 1, 2]
        if graph[0][2] and graph[2][1] and not graph[0][1]:
            return [0, 2, 1]
        if graph[1][0] and graph[0][2] and not graph[1][2]:
            return [1, 0, 2]
        if graph[1][2] and graph[2][0] and not graph[1][0]:
            return [1, 2, 0]
        if graph[2][0] and graph[0][1] and not graph[2][1]:
            return [2, 0, 1]
        if graph[2][1] and graph[1][0] and not graph[2][0]:
            return [2, 1, 0]
        return None
    center = n // 2
    left = graph[:center] + [[False] * n]
    right = [[False] * n] + graph[center:]
    path_left = find_hamiltonian_path(left)
    path_right = find_hamiltonian_path(right)
    if path_left is None or path_right is None:
        return None
    left_end = next(i for i in path_left if i < center)
    right_start = next(i for i in path_right if i > center)
    for i in range(left_end, center):
        for j in range(right_start, n):
            if graph[i][j] and all(k not in path_left + path_right for k in range(left_end, i)) and all(k not in path_left + path_right for k in range(j, right_start, -1)):
                return path_left[:path_left.index(left_end)] + list(range(i, center)) + path_right[path_right.index(right_start)+1:] + [j]
    return None
