t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    nodes = []

    for i in range(k):
        nodes.append(tuple(map(int, input().split())))

    groups = []
    adjacent = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while len(nodes) > 0:
        a, b = nodes.pop()

        nodes_to_remove = []
        stack = [(a, b)]
        for x1, y1 in stack:
            for x, y in nodes:
                if (x - x1, y - y1) in adjacent:
                    stack.append((x, y))
                    nodes_to_remove.append((x, y))
            nodes = list(set(nodes) - set(nodes_to_remove))
        groups.append(stack)

    print(len(groups))
