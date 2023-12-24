from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Binary Tree Level Order Traversal: duyệt cây theo chiêu rộng
def level_order(root):
    if not root:
        return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


# Zigzag Traversal: duyệt cây BFS theo chiều rông nhưng zigzag từ trái -> phải, phải-> trái : đảo ngược ở mỗi tầng
def zigzag_traversal(root):
    if not root:
        return []

    result = []
    queue = deque()
    queue.append(root)
    level = 0

    while queue:
        level_size = len(queue)
        current_level = deque()

        for _ in range(level_size):
            node = queue.popleft()

            if level % 2 == 0:
                current_level.append(node.val)
            else:
                current_level.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(current_level))
        level += 1

    return result


# Tìm đường đi ngắn nhất
def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start]

    queue = deque()
    queue.append([start])
    visited = set()
    visited.add(start)

    while queue:
        path = queue.popleft()
        current_node = path[-1]

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)

                if neighbor == end:
                    return new_path

                queue.append(new_path)

    return []


if __name__ == '__main__':
    # Tạo một cây nhị phân để kiểm tra Order Traversal
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(level_order(root))

    # Tạo một cây nhị phân để kiểm tra Zigzag
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(zigzag_traversal(root))

    # Ví dụ đồ thị
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    end_node = 'E'
    shortest_path = bfs_shortest_path(graph, start_node, end_node)

    if shortest_path:
        print(f"Đường đi ngắn nhất từ {start_node} đến {end_node}: ", "->".join(shortest_path))
    else:
        print(f"Không có đường đi từ {start_node} đến {end_node}")
