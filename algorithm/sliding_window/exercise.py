# TÌM TỔNG CỰC ĐẠI CỦA MẢNG CON CÓ ĐỘ DÀI CỐ ĐỊNH
def maximum_sum_subarray_k_distinct(s, k):
    # kiem tra hop le
    if len(s) <= 0 or k <= 0:
        return 0
    # khoi tao window size
    start = end = 0
    max_sum = 0
    max_array = []

    # run
    while end < len(s):
        end += 1
        if end - start + 1 == k:
            if sum(s[start:end+1]) > max_sum:
                max_sum = sum(s[start:end+1])
                max_array = s[start:end+1]
            start += 1

    return max_sum, max_array


# TÌM TẤT CẢ MẢNG CON CÓ TỔNG BẰNG 1 GIÁ TRỊ XÁC ĐỊNH : so ko am
def find_subarray_with_sum_equal_k(s, k):
    # kiem tra hop le
    if len(s) <= 0 or k < 0:
        return 0

    # khoi tao
    start = end = 0
    result = []

    # run
    while end < len(s):
        if sum(s[start:end+1]) == k:
            result.append(s[start:end+1])
            start += 1
        elif sum(s[start:end+1]) > k:
            start += 1
        else:
            end += 1
    return result


# TÌM KIẾM ĐOẠN VĂN BẢN
def sliding_window_search(text, pattern):
    window_size = len(pattern)
    results = []

    # Khởi tạo cửa sổ ban đầu
    window = text[:window_size]

    # Duyệt qua văn bản
    for i in range(len(text) - window_size + 1):
        # Kiểm tra cửa sổ hiện tại có khớp với mẫu không
        if window == pattern:
            results.append(i)

        # Di chuyển cửa sổ
        window = text[i+1:i+window_size+1]

    return results


if __name__ == '__main__':
    print(find_subarray_with_sum_equal_k([1,2,3,4,5,1,3], 5))

    # Ví dụ sử dụng
    text = "This is an example text"
    pattern = "example"
    results = sliding_window_search(text, pattern)
    print(results)  # Output: [11]
