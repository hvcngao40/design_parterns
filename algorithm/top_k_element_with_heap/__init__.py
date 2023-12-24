# 1. Tạo một heap có k phần tử.
# 2. Duyệt qua từng phần tử trong mảng và thêm chúng vào heap.
# 3. Nếu số lượng phần tử trong heap vượt quá k, hãy loại bỏ phần tử nhỏ nhất hoặc lớn nhất khỏi heap.
# 4. Kết quả cuối cùng sẽ là các phần tử còn lại trong heap.
import heapq
from collections import Counter


def top_k_elements(nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

    return heap


def top_k_smallest(nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, -num)  # Đảo ngược dấu để tạo heap có thứ tự đảo ngược
        else:
            if -num > heap[0]:
                heapq.heappushpop(heap, -num)

    smallest_nums = [-num for num in heap]  # Đảo ngược dấu trở lại
    smallest_nums.sort()  # Sắp xếp lại danh sách kết quả theo thứ tự tăng dần

    return smallest_nums


def top_k_frequent_numbers(nums, k):
    # Bước tiền xử lý: Đếm số lần xuất hiện của các số
    counter = Counter(nums)

    # Sử dụng heap để tìm K số xuất hiện nhiều nhất
    heap = []
    for num, freq in counter.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        else:
            if freq > heap[0][0]:
                heapq.heappushpop(heap, (freq, num))

    top_k_frequent = [num for freq, num in heap]
    top_k_frequent.sort(reverse=True)  # Sắp xếp lại danh sách kết quả theo thứ tự giảm dần

    return top_k_frequent


if __name__ == '__main__':
    # Ví dụ sử dụng
    nums = [4, 8, 2, 1, 6, 9, 5]
    k = 3

    result = top_k_elements(nums, k)
    print(result)  # Output: [6, 8, 9]
