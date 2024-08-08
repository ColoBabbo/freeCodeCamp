my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target = ''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    while unvisited:
        current = min(unvisited, key=distances.get)
        print(f'\nWHILE {unvisited = }\n  {current = }\n  {distances = }\n  {paths = }')
        for node, distance in graph[current]:
            print(f"\n  FOR node, distance in graph[{current}]\n    {node = }\n    {distance = }\n    graph[current='{current}'] = {graph[current]} ")   
            print(f"      Before paths[node='{node}'] = {paths[node]  }\n         distances[node='{node}'] = {distances[node]  }")
            print(f"      IF  distance + distances[current] < distances[node]\n            ({distance })    +    ({distances[current]})    <    {distance + distances[node]}")
            if distance + distances[current] < distances[node]:
                print('        True')
                distances[node] = distance + distances[current]
                print(f'        THEN distances[node] = {distance + distances[current]}')
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
            print(f'      After  {paths[node] = }\n         {distances[node] = }')
            # print(f'    {paths[node] = }')
        unvisited.remove(current)
        # print(f'\n{paths[current] = }')
        # print(f'Current: {current}\nUnvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        # print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths
    
shortest_path(my_graph, 'A', '')