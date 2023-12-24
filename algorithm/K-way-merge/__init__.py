# trộn K danh sách đã sắp xếp thành 1 danh sách sắp xếp (merge_list)
# 1. Lấy phần từ đầu của mỗi danh sach thêm vào min heap
# 2. Lấy phần tử nhỏ nhất: heap.pop() thêm vào merge_list (danh sách cuối)
# 3. Lấy phần tử tiếp theo của danh sách có phần tử vừa được thêm vào merge list
# 4. Tiếp tục cho đến khi heap rỗng -> được merge list
import heapq


def k_way_merge(lists):
    heap = []  # Heap để lưu trữ các phần tử từ các dãy con
    result = []  # Dãy con kết quả
    # Khởi tạo heap với phần tử đầu tiên từ mỗi dãy con
    for i, lst in enumerate(lists):
        if lst:  # Kiểm tra xem dãy con có phần tử hay không
            heap.append((lst[0], i, 0))  # (giá trị, chỉ số dãy con, chỉ số phần tử)

    heapq.heapify(heap)  # Xây dựng heap

    while heap:  # Lặp cho đến khi heap trống
        val, list_index, elem_index = heapq.heappop(heap)  # Lấy phần tử nhỏ nhất từ heap
        result.append(val)  # Thêm phần tử vào dãy con kết quả

        if elem_index + 1 < len(lists[list_index]):  # Kiểm tra xem dãy con tương ứng còn phần tử hay không
            next_elem = lists[list_index][elem_index + 1]  # Lấy phần tử tiếp theo trong dãy con
            heapq.heappush(heap, (next_elem, list_index, elem_index + 1))  # Thêm phần tử vào heap

    return result


# tìm ra k cặp có tổng lớn nhất từ hai mảng đã sắp xếp.
def k_largest_pairs(nums1, nums2, k):
    heap = []  # Heap để lưu trữ các cặp (tổng, [u, v])

    # Lưu trữ tất cảcác cặp có tổng đầu tiên từ nums1 và nums2 vào heap
    for i in range(min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            pair_sum = nums1[i] + nums2[j]
            heapq.heappush(heap, (-pair_sum, [nums1[i], nums2[j]]))     # đảo ngược dấu - để được cặp lớn nhất

    result = []

    # Lấy k cặp có tổng lớn nhất từ heap
    for _ in range(min(k, len(nums1) * len(nums2))):
        pair_sum, pair = heapq.heappop(heap)
        result.append(pair)

    return result


if __name__ == '__main__':
    # Ví dụ sử dụng
    lists = [[2, 4, 6], [1, 3, 5, 7], [0, 8, 9]]

    result = k_way_merge(lists)
    print(result)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # test k largest pairs
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3

    result = k_largest_pairs(nums1, nums2, k)
    print(result)  # Output: [[11, 6], [11, 4], [7, 6]]
