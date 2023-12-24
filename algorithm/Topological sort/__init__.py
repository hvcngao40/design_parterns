# Topological sort (sắp xếp topo) là một thuật toán được sử dụng để sắp xếp các đỉnh trong một đồ thị có hướng sao cho
# tất cả các cạnh đều chỉ đi từ đỉnh được sắp xếp trước đến đỉnh được sắp xếp sau. (chỉ dùng cho đồ thị không có chu trình)
from collections import defaultdict, deque


def topological_sort(graph):
    # Tính số lượng đỉnh tiền đề của mỗi đỉnh (cùng 1 hàng theo chiều rộng của BFS)
    in_degrees = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degrees[neighbor] += 1

    # Tìm tất cả các nguồn (không có đường đi nào đến no)
    sources = deque()
    for node in graph:
        if in_degrees[node] == 0:
            sources.append(node)

    # Sắp xếp topo (thêm nguồn vào list, xóa nguồn, các nút bên dưới thaành nguồn, rồi tiếp tục đến hết đồ thị)
    sorted_list = []
    while sources:
        source = sources.popleft()
        sorted_list.append(source)

        # Giảm số lượng đỉnh tiền đề của các đỉnh con
        for neighbor in graph[source]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                sources.append(neighbor)

    return sorted_list


# ứng dụng: 1. Xác định thứ tự thực hiện công việc hoặc các phụ thuộc giữa các công việc trong lịch trình dự án.
# 2. Xác định thứ tự biên dịch các mã nguồn trong quá trình biên dịch.
# 3. Tìm kiếm một thứ tự thích hợp để giải quyết các phụ thuộc giữa các gói phần mềm hoặc module.


# 1. Task Scheduling: công việc phụ thuộc
def task_scheduling(tasks, prerequisites):
    # Tạo đồ thị và đếm số lượng đỉnh tiền đề của mỗi đỉnh
    graph = defaultdict(list)
    in_degrees = defaultdict(int)
    for task, prerequisite in prerequisites:
        graph[prerequisite].append(task)
        in_degrees[task] += 1

    # Tìm tất cả các công việc không có đỉnh tiền đề
    sources = deque()
    for task in tasks:
        if in_degrees[task] == 0:
            sources.append(task)

    # Sắp xếp topo và kiểm tra tính khả thi
    sorted_order = []
    while sources:
        task = sources.popleft()
        sorted_order.append(task)

        # Giảm số lượng đỉnh tiền đề của các công việc con
        for dependent_task in graph[task]:
            in_degrees[dependent_task] -= 1
            if in_degrees[dependent_task] == 0:
                sources.append(dependent_task)

    # Kiểm tra xem có thể sắp xếp topo cho tất cả công việc hay không
    if len(sorted_order) != len(tasks):
        return []  # Không thể sắp xếp topo

    return sorted_order


# Minimum Height of a Tree: None of topological  tìm cây có chiều cao nhỏ nhất trong một đồ thị không có chu trình.
# dang tim lon nhat thi dung hon

def minimum_height_tree(n, edges):
    if n == 1:
        return [0]
    graph = defaultdict(list)   # mỗi đỉnh có thể nối đến các đỉnh nào khác
    in_degree = [0] * n     # điểm thể hiện số đỉnh có thể nối của mỗi đỉnh
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        in_degree[u] += 1
        in_degree[v] += 1
    leaves = deque([i for i in range(n) if in_degree[i] == 1])  # chỉ là lá (ko dẫn đi đâu)
    while n > 2:
        n -= len(leaves)
        for _ in range(len(leaves)):
            leaf = leaves.popleft()
            for neighbor in graph[leaf]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 1:
                    leaves.append(neighbor)
    return list(leaves)


if __name__ == '__main__':
    # Ví dụ sử dụng
    graph = {
        'A': ['C'],
        'B': ['D'],
        'C': ['E'],
        'D': ['E', 'F'],
        'E': [],
        'F': []
    }
    sorted_order = topological_sort(graph)
    print(sorted_order)

    # 1. Task Scheduling
    tasks = [1, 2, 3, 4]
    prerequisites = [(1, 2), (2, 3), (3, 4)]  # task 1 phụ thuộc vào task 2, 2 vào 3, 3 vào 4.
    result = task_scheduling(tasks, prerequisites)
    print(result)  # [4, 3, 2, 1]
    # Minimum tree
    n = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    result = minimum_height_tree(n, edges)
    print(result)  # 3
