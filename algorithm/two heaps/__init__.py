# Ý tưởng sử dụng two heap: dùng 2 cây nhị phân: max heap: node dinh là lớn nhất, nhỏ dần xuống dưới
# min heap th ngược lại: node dinh là nhỏ nhất, lớn dần xuống dưới.
# => rất dễ dàng thư hiện: tim giá trị lớn nhất, nhỏ nhất, trung vị (max +min)/2 của dãy
# các ứng dụng Priority Queue, Scheduling

from heapq import *


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def add_number(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # Cân bằng kích thước của hai heap
        if len(self.max_heap) - len(self.min_heap) > 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0]


class PriorityQueue:
    def __init__(self):
        self.min_heap = []  # Min heap

    def push(self, item, priority):
        heappush(self.min_heap, (priority, item))

    def pop(self):
        if self.min_heap:
            _, item = heappop(self.min_heap)
            return item
        return None

    def is_empty(self):
        return len(self.min_heap) == 0


if __name__ == '__main__':
    # Tạo một đối tượng MedianFinder
    median_finder = MedianFinder()

    # Thêm các số vào dãy số và tính median sau mỗi bước
    numbers = [4, 7, 2, 9, 1, 5]
    for num in numbers:
        median_finder.add_number(num)
        median = median_finder.find_median()
        print("Current median:", median)

    # Tạo một đối tượng PriorityQueue
    queue = PriorityQueue()

    # Thêm các phần tử vào hàng đợi với độ ưu tiên tương ứng
    queue.push("Task 1", 2)
    queue.push("Task 2", 1)
    queue.push("Task 3", 3)

    # Lấy các phần tử từ hàng đợi theo độ ưu tiên
    while not queue.is_empty():
        item = queue.pop()
        print("Processing:", item)
