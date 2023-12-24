# tìm tất cả tâập con của 1 tập các số, nếu sử dụng đệ quy sẽ chậm
# sử dụng BFS
from collections import deque
from queue import Queue


def subsets(nums):
    subsets = []
    queue = deque()
    queue.append([])  # Thêm tập rỗng vào hàng đợi ban đầu

    while queue:
        curr_subset = queue.popleft()
        subsets.append(curr_subset)

        for num in nums:
            if not curr_subset or num > curr_subset[-1]:
                new_subset = curr_subset + [num]
                queue.append(new_subset)

    return subsets


# 1. Tập con với phần tử trùng nhau Subsets With Duplicates (easy)
def subsetsWithDup(nums):
    subsets = []
    nums.sort()  # Sắp xếp mảng để phát hiện các phần tử trùng nhau

    queue = deque()
    queue.append(([], 0))  # Thêm tập rỗng vào hàng đợi ban đầu

    while queue:
        curr_subset, start = queue.popleft()
        subsets.append(curr_subset)

        for i in range(start, len(nums)):
            # Kiểm tra và loại bỏ các phần tử trùng lặp
            if i > start and nums[i] == nums[i - 1]:
                continue

            new_subset = curr_subset + [nums[i]]
            queue.append((new_subset, i + 1))

    return subsets


# 2. String Permutations by changing case (hoán vị chuỗi bằng cách thay đổi chữ hoa/chữ thường)
def string_permutations_bfs(s: str):
    q = Queue()
    q.put(s)
    seen = set([s])
    res = []
    while not q.empty():
        curr = q.get()
        res.append(curr)
        for i in range(len(curr)):
            if curr[i].isalpha():
                new_str = curr[:i] + curr[i].swapcase() + curr[i+1:]
                if new_str not in seen:
                    q.put(new_str)
                    seen.add(new_str)
    return res


if __name__ == '__main__':
    # Sử dụng ví dụ tập hợp {1, 2, 3}
    nums = [1, 2, 3]
    result = subsets(nums)
    print(result)

    # Test
    nums = [1, 2, 2]
    result = subsetsWithDup(nums)
    print(result)

    # Test
    input_str = "ab12"
    permutations = string_permutations_bfs(input_str)
    print(permutations)
