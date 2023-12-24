# 1. Hợp nhất tất cả các khoảng thời gian chồng chéo trong 1 tập hợp tất cả các khoaảng thời gian
def merge(intervals):
    # Sắp xếp các khoảng thời gian theo thứ tự tăng dần của thời gian bắt đầu
    intervals.sort(key=lambda x: x[0])
    # Khởi tạo kết quả là một danh sách trống
    result = []
    # Duyệt qua các khoảng thời gian
    for interval in intervals:
        # Nếu kết quả rỗng hoặc khoảng thời gian hiện tại không chồng chéo với khoảng thời gian cuối cùng trong kết quả
        if not result or result[-1][1] < interval[0]:
            # Thêm khoảng thời gian hiện tại vào kết quả
            result.append(interval)
        else:
            # Nếu khoảng thời gian hiện tại chồng chéo với khoảng thời gian cuối cùng trong kết quả
            # Cập nhật thời gian kết thúc của khoảng thời gian cuối cùng bằng thời gian kết thúc lớn hơn
            result[-1][1] = max(result[-1][1], interval[1])
    # Trả về kết quả
    return result


# 2. tìm tất cả các vị trí bắt đầu của các chuổi con là anagram của 1 chuỗi cho trước
def find_anagrams(s, p):
    # Khởi tạo kết quả là một danh sách trống
    result = []
    # Kiểm tra điều kiện hợp lệ
    if len(s) < len(p) or len(p) == 0:
        return result
    # Khởi tạo hai bộ đếm cho chuỗi p và cửa sổ đầu tiên của chuỗi s
    p_count = [0] * 26
    s_count = [0] * 26
    for i in range(len(p)):
        p_count[ord(p[i]) - ord('a')] += 1
        s_count[ord(s[i]) - ord('a')] += 1
    # Duyệt qua các cửa sổ còn lại của chuỗi s
    for i in range(len(p), len(s)):
        # Nếu hai bộ đếm bằng nhau, thêm vị trí bắt đầu của cửa sổ vào kết quả
        if p_count == s_count:
            result.append(i - len(p))
        # Cập nhật bộ đếm cho cửa sổ mới bằng cách bớt đi phần tử đầu và cộng thêm phần tử cuối
        s_count[ord(s[i]) - ord('a')] += 1
        s_count[ord(s[i - len(p)]) - ord('a')] -= 1
    # Kiểm tra bộ đếm cho cửa sổ cuối cùng
    if p_count == s_count:
        result.append(len(s) - len(p))
    # Trả về kết quả
    return result


# 3. Tìm giao điểm của 2 danh sách các khoảng thời gian
def interval_intersection(A, B):
    # Khởi tạo kết quả là một danh sách trống
    result = []
    # Khởi tạo hai chỉ số để duyệt qua hai danh sách
    i = 0
    j = 0
    # Duyệt qua hai danh sách cho đến khi hết một trong hai danh sách
    while i < len(A) and j < len(B):
        # Tìm thời gian bắt đầu và kết thúc của giao điểm giữa hai khoảng thời gian hiện tại
        start = max(A[i][0], B[j][0])
        end = min(A[i][1], B[j][1])
        # Nếu giao điểm tồn tại, thêm nó vào kết quả
        if start <= end:
            result.append([start, end])
        # Di chuyển chỉ số của danh sách có thời gian kết thúc nhỏ hơn sang khoảng thời gian tiếp theo
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    # Trả về kết quả
    return result
