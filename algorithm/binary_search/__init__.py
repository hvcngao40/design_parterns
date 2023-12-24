# Binary search thường dùng với mảng, link list,... đã săp xếp. Tìm kiếm (key) thường theo các bước
# 1. Tìm middle = start + (end-start)/2 thay vì middle = (start + end)/2 (số có thể quá lớn so với kiểu dữ liệu được định nghĩa)
# 2. Nếu key = giá trị tại middle thì trả về giá trị middle luôn. Nếu không:
# 3. Nếu key < giá trị tại middle thì gọi đệ quy tìm kiếm trong khoảng từ start -> middle -1
# 4. Nếu key > giá tri tại middle thì gọi đệ quy tìm kiếm trong khoảng middle + 1 -> end


# Order-agnostic Binary Search
def order_agnostic_binary_search(arr, key):
    start, end = 0, len(arr) - 1
    is_ascending = arr[start] < arr[end]
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        if is_ascending:
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


# Search in a Sorted Infinite Array
def search_in_infinite_array(arr, key):
    start, end = 0, 1
    while arr[end] < key:
        new_start = end + 1
        end += (end - start + 1) * 2
        start = new_start
    return binary_search(arr, key, start, end)


def binary_search(arr, key, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


if __name__ == '__main__':
    # Ví dụ sử dụng
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23

    result = order_agnostic_binary_search(arr, target)
    if result != -1:
        print("Giá trị", target, "được tìm thấy tại vị trí", result)
    else:
        print("Giá trị", target, "không tồn tại trong dãy.")

    # ví dụ 2
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91, 108, 126, 137, 150, 167, 185, 200, 215, 230, 245, 260, 275, 290, 305]
    target = 137

    result = search_in_infinite_array(arr, target)
    if result != -1:
        print("Giá trị", target, "được tìm thấy tại vị trí", result)
    else:
        print("Giá trị", target, "không tồn tại trong dãy.")
