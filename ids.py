def depth_limited_search(node, goal, graph, limit, path):
    if node == goal:
        return path + [node]
    if limit == 0:
        return "cutoff"
    cutoff_occurred = False
    for child in graph.get(node, []):
        if child not in path:  # avoid revisiting states on the current path
            result = depth_limited_search(child, goal, graph, limit - 1, path + [node])
            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return result
    return "cutoff" if cutoff_occurred else "failure"


def iterative_deepening_search(initial, goal, graph, max_depth):
    for depth in range(max_depth + 1):
        result = depth_limited_search(initial, goal, graph, depth, [])
        if result not in ("cutoff", "failure"):
            return result, depth
    return None, None


def main():
    initial = input("Enter initial state: ").strip()
    goal = input("Enter goal state: ").strip()
    max_depth = int(input("Enter maximum depth: "))

    n = int(input("Enter number of nodes in the search tree: "))
    graph = {}
    print("Enter each node and its children separated by spaces (leave children empty if none):")
    for _ in range(n):
        parts = input().split()
        graph[parts[0]] = parts[1:]

    path, depth = iterative_deepening_search(initial, goal, graph, max_depth)

    if path:
        print("Goal found!")
        print("Solution path:", " -> ".join(path))
        print("Depth:", depth)
    else:
        print(f"Goal not found within maximum depth {max_depth}")


if __name__ == "__main__":
    main()