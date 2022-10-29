
#O(v+e) time and O(v) space2
def cycleInGraph(edges):
    visited = set()

    for node in range(len(edges)):
        visited.add(node)
        constainsCycle = dfs(node, edges, visited)
        if constainsCycle:
            return True
    return False
        
def dfs(node, edges, visited):
    neighbours = edges[node]
    print(neighbours)
    for neighbour in neighbours:
        if neighbour in visited:
            return True
        visited.add(neighbour)
        containsCycle  = dfs(neighbour, edges, visited)
        if containsCycle:
            return True
    visited.remove(node)
    return False

def test_cycle_graph():
    input = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
    actual = cycleInGraph(input)
    expected = True
    assert actual == expected
