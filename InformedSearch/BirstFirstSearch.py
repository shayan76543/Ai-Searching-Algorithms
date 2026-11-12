def best_first_search(graph, heuristic, start, goal):
    pq = []
    pq.append((heuristic[start], start))
    visited = set()
    while pq:
        pq.sort()
        h, current = pq.pop(0)
        if current in visited:
            continue
        print("Visiting:", current)
        if current == goal:
            return True
        visited.add(current)
        for neighbour in graph[current]:

            if neighbour not in visited:
                pq.append((heuristic[neighbour], neighbour))
    return False
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'F': 1,
    'G': 0
}
result = best_first_search(graph, heuristic, 'A', 'G')
print("Goal Found:", result)
# Time Compexity and Space Complexity Time Com->O(b**m)  Space Com ->O(b**d)
#  here Here, \(m\) is the maximum depth of the search tree.

# For Best First Search, the graph bound assumes a priority queue implemented using a binary heap and appropriate duplicate handling.
