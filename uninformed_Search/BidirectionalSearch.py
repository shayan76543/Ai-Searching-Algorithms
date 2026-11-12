from collections import deque
def bidirectional_search(graph, start, goal):
    q1 = deque([start])
    q2 = deque([goal])
    visited1 = {start}
    visited2 = {goal}
    while q1 and q2:
        # Forward search
        current = q1.popleft()
        for neighbor in graph[current]:
            if neighbor in visited2:
                return True
            if neighbor not in visited1:
                visited1.add(neighbor)
                q1.append(neighbor)
        # Backward search
        current = q2.popleft()
        for neighbor in graph[current]:
            if neighbor in visited1:
                return True 
            if neighbor not in visited2:
                visited2.add(neighbor)
                q2.append(neighbor)
    return False
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'G'],
    'F': ['C', 'G'],
    'G': ['D', 'E', 'F']
}
print(bidirectional_search(graph,'A','G'))
# Time Compexity and Space Complexity Time Com->O(b**d/2)  Space Com ->O(b**d/2)