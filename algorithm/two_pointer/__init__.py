# thường hoạt động trong 1 iterable đã sắp xếp
# tìm 2 phần tử trong mảng (đã sắp xếp) có tổng bằng 1 số cho trước
def two_sum(arr, target):
    # Khởi tạo hai con trỏ ở hai đầu mảng
    left = 0
    right = len(arr) - 1
    # Duyệt qua mảng cho đến khi hai con trỏ gặp nhau
    while left < right:
        # Tính tổng hai phần tử tại hai con trỏ
        total = arr[left] + arr[right]
        # Nếu tổng bằng số cho trước, trả về hai chỉ số
        if total == target:
            return arr[left], arr[right]
        # Nếu tổng nhỏ hơn số cho trước, tăng con trỏ bên trái
        elif total < target:
            left += 1
        # Nếu tổng lớn hơn số cho trước, giảm con trỏ bên phải
        else:
            right -= 1
    # Nếu không tìm thấy cặp phù hợp, trả về None
    return None


if __name__ == '__main__':
    print(two_sum([1, 2, 3, 4, 5, 6, 7, 9], 9))
