def is_path(graph, start, end, checked):
    if start == end:
        return True
    checked.append(start)
    if start in graph:
        for new_start in graph[start]:
            if new_start not in checked and is_path(graph, new_start, end, checked):
                return True
    return False

def main():
    graph = {
        'A': ['B', 'C', 'O'],
        'B': ['D', 'A', 'K', 'C'],
        'C': ['E', 'M', 'N'],
        'D': ['D'],
        'E': ['J', 'K'],
        'F': ['A', 'B'],
        'H': ['O', 'P', 'Q', 'C', 'B'],
        'I': ['P', 'Q'],
        'J': []
    }
    checked = []
    start, end = input("Input path: ").upper().split(" ")

    print(is_path(graph, start, end, checked))

if __name__ == "__main__":
    main()
