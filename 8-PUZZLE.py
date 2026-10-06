import heapq

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def manhattan(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            current_row = i // 3
            current_col = i % 3

            goal_index = goal.index(tile)
            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


def successors(state):
    children = []

    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    # UP
    if row > 0:
        new_state = state.copy()
        new_state[blank], new_state[blank - 3] = new_state[blank - 3], new_state[blank]
        children.append(new_state)

    # DOWN
    if row < 2:
        new_state = state.copy()
        new_state[blank], new_state[blank + 3] = \
            new_state[blank + 3], new_state[blank]
        children.append(new_state)

    # LEFT
    if col > 0:
        new_state = state.copy()
        new_state[blank], new_state[blank - 1] = \
            new_state[blank - 1], new_state[blank]
        children.append(new_state)

    # RIGHT
    if col < 2:
        new_state = state.copy()
        new_state[blank], new_state[blank + 1] = \
            new_state[blank + 1], new_state[blank]
        children.append(new_state)

    return children


def a_star(start):
    pq = []

    g = 0
    f = g + manhattan(start)

    heapq.heappush(pq, (f, g, start, []))

    explored = []

    while pq:

        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path + [state]

        if state in explored:
            continue

        explored.append(state)

        for child in successors(state):

            if child not in explored:
                new_g = g + 1
                new_f = new_g + manhattan(child)

                heapq.heappush(
                    pq,
                    (new_f, new_g, child, path + [state])
                )

    return None


start = [1 ,2 ,3,
        5, 0, 6,
        4, 7, 8]
if start == goal:
    print("solution found")
    solution=goal
else:
    solution = a_star(start)
    

print("Solution:")

for state in solution:
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()
