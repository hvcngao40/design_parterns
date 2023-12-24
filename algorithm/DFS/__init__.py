# 1. Sum of Path Numbers: Tính tổng tất cả các số được tạo ra từ 1 cây nhị phân (Tính giá trị đường đi từ 1 điểm đến 1 điểm)

# Định nghĩa lớp Node để biểu diễn một nút của cây nhị phân
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val  # Giá trị của nút
        self.left = left  # Con trái của nút
        self.right = right  # Con phải của nút


# Hàm để tính tổng các số được tạo ra từ các đường đi từ gốc đến lá của cây nhị phân
def sum_of_path_numbers(root):
    if not root:
        return 0

    total_sum = 0

    def dfs(node, current_sum):
        nonlocal total_sum

        current_sum = current_sum * 10 + node.val

        if not node.left and not node.right:
            total_sum += current_sum
            return

        if node.left:
            dfs(node.left, current_sum)

        if node.right:
            dfs(node.right, current_sum)

    dfs(root, 0)

    return total_sum


# 2. All Paths for a Sum: Tìm tat cả các đường đi có cùng chi phí

def all_paths_for_sum(root, target_sum):
    all_paths = []

    def dfs(node, current_path, current_sum):
        if not node:
            return

        current_path.append(node.val)
        current_sum += node.val

        if current_sum == target_sum and not node.left and not node.right:
            all_paths.append(current_path[:])

        dfs(node.left, current_path, current_sum)
        dfs(node.right, current_path, current_sum)

        current_path.pop()

    dfs(root, [], 0)

    return all_paths


if __name__ == '__main__':
    # Tạo cây nhị phân
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Gọi hàm tính tổng các số từ đường đi gốc đến lá
    result = sum_of_path_numbers(root)
    print("Sum of path numbers:", result)
    #################################################
    # Tạo cây nhị phân
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)

    # Gọi hàm tìm tất cả các đường đi có tổng bằng 12
    result = all_paths_for_sum(root, 12)
    print("All paths for sum 12:")
    for path in result:
        print(path)
