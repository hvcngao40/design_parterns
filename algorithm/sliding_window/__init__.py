# 1 TÌM TỔNG LỚN NHẤT CỦA K PHẦN TỬ LIÊN TIẾP TRONG 1 MẢNG
def max_sum_subarray(arr, k):
    # Kiểm tra điều kiện hợp lệ
    if len(arr) < k or k <= 0:
        return None

    # Tính tổng cửa sổ đầu tiên
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Duyệt qua các cửa sổ còn lại
    for i in range(k, len(arr)):
        # Cập nhật tổng cửa sổ bằng cách bớt đi phần tử đầu và cộng thêm phần tử cuối
        window_sum += arr[i] - arr[i - k]
        # Cập nhật tổng lớn nhất
        max_sum = max(max_sum, window_sum)

    return max_sum


# 2. TÌM ĐỘ DÀI CHUỖI CON KHÔNG CÓ KÝ TỰ TRÙNG LẶP DÀI NHẤT
def longest_substring_no_repeat(s):
    # Kiểm tra điều kiện hợp lệ
    if not s:
        return 0

    # Khởi tạo cửa sổ và tập hợp các ký tự đã xuất hiện
    start = 0
    end = 0
    seen = set()
    max_string = ''
    max_length = 0

    # Duyệt qua chuỗi
    while end < len(s):
        # Nếu ký tự cuối cùng của cửa sổ chưa xuất hiện trước đó
        if s[end] not in seen:
            # Thêm ký tự vào tập hợp
            seen.add(s[end])
            # Cập nhật độ dài lớn nhất
            # max_length = max(max_length, end - start + 1)
            if max_length < end-start+1:
                max_string = s[start:end+1]
                max_length = end-start+1
            else:
                max_length = max_length
            # Mở rộng cửa sổ sang phải
            end += 1
        else:
            # Nếu ký tự cuối cùng của cửa sổ đã xuất hiện trước đó
            # Loại bỏ ký tự đầu tiên của cửa sổ khỏi tập hợp
            seen.remove(s[start])
            # Thu hẹp cửa sổ sang phải
            start += 1

    return max_length, max_string


# 3. TÌM SỐ LƯỢNG CHUỖI CON CÓ SỐ KÝ TỰ KHÔNG VƯỢT QUÁ K
from collections import Counter


def count_substrings_k_distinct(s, k):
    # Kiểm tra điều kiện hợp lệ
    if not s or k <= 0:
        return 0

    # Khởi tạo cửa sổ và bộ đếm các ký tự trong cửa sổ
    start = 0
    end = 0
    counter = Counter()
    count = 0

    # Duyệt qua chuỗi
    while end < len(s):
        # Tăng số lần xuất hiện của ký tự cuối cùng của cửa sổ
        counter[s[end]] += 1
        # Mở rộng cửa sổ sang phải
        end += 1

        # Nếu số ký tự khác nhau trong cửa sổ vượt quá k
        while len(counter) > k:
            # Giảm số lần xuất hiện của ký tự đầu tiên của cửa sổ
            counter[s[start]] -= 1
            # Nếu số lần xuất hiện bằng 0, loại bỏ ký tự khỏi bộ đếm
            if counter[s[start]] == 0:
                del counter[s[start]]
            # Thu hẹp cửa sổ sang phải
            start += 1

        # Cập nhật số lượng chuỗi con thỏa mãn
        count += end - start

    return count


if __name__ == '__main__':
    print(count_substrings_k_distinct('abcd', 2))
