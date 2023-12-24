# Hàm sắp xếp mảng bằng Cyclic sort
def cycleSort(arr):
    # Đếm số lần ghi vào mảng
    writes = 0
    # Duyệt qua các phần tử của mảng và đặt chúng vào vị trí đúng
    for cycle_start in range(0, len(arr) - 1):
        # Lấy phần tử bắt đầu của chu kỳ hiện tại
        item = arr[cycle_start]
        # Tìm vị trí đúng của phần tử này trong mảng đã sắp xếp
        pos = cycle_start
        for i in range(cycle_start + 1, len(arr)):
            if arr[i] < item:
                pos += 1
        # Nếu phần tử đã ở vị trí đúng, bỏ qua
        if pos == cycle_start:
            continue
        # Nếu có phần tử trùng với phần tử hiện tại, tăng pos lên 1
        while item == arr[pos]:
            pos += 1
        # Hoán vị phần tử hiện tại với phần tử ở vị trí đúng
        arr[pos], item = item, arr[pos]
        writes += 1
        # Tiếp tục quay vòng chu kỳ cho đến khi quay lại vị trí bắt đầu
        while pos != cycle_start:
            # Tìm lại vị trí đúng của phần tử hiện tại
            pos = cycle_start
            for i in range(cycle_start + 1, len(arr)):
                if arr[i] < item:
                    pos += 1
            # Nếu có phần tử trùng với phần tử hiện tại, tăng pos lên 1
            while item == arr[pos]:
                pos += 1
            # Hoán vị phần tử hiện tại với phần tử ở vị trí đúng
            arr[pos], item = item, arr[pos]
            writes += 1
    # Trả về số lần ghi vào mảng
    return writes


# Mảng cần sắp xếp
arr = [3, 5, 2, 1, 4]
# Gọi hàm sắp xếp
cycleSort(arr)
# In ra mảng đã sắp xếp
print("Mảng đã sắp xếp:")
for i in range(0, len(arr)):
    print(arr[i], end=" ")
