# 1. Tìm phần tử giữa của 1 danh sách liên kết
# Định nghĩa lớp Node để biểu diễn một phần tử trong danh sách liên kết
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Định nghĩa hàm để tìm phần tử giữa của một danh sách liên kết
def find_middle(head):
    # Khởi tạo hai con trỏ nhanh và chậm từ phần tử đầu tiên
    fast = head
    slow = head
    # Duyệt qua danh sách liên kết cho đến khi con trỏ nhanh hết danh sách hoặc chỉ còn một phần tử
    while fast and fast.next:
        # Di chuyển con trỏ nhanh hai bước mỗi lần
        fast = fast.next.next
        # Di chuyển con trỏ chậm một bước mỗi lần
        slow = slow.next
    # Trả về phần tử mà con trỏ chậm đang trỏ đến
    return slow


# 2. Phát hiện vòng lặp trong 1 danh sách liên kết

# Định nghĩa hàm để phát hiện vòng lặp trong một danh sách liên kết
def detect_cycle(head):
    # Khởi tạo hai con trỏ nhanh và chậm từ phần tử đầu tiên
    fast = head
    slow = head
    # Duyệt qua danh sách liên kết cho đến khi con trỏ nhanh hết danh sách
    while fast and fast.next:
        # Di chuyển con trỏ nhanh hai bước mỗi lần
        fast = fast.next.next
        # Di chuyển con trỏ chậm một bước mỗi lần
        slow = slow.next
        # Nếu hai con trỏ gặp nhau, có nghĩa là có vòng lặp
        if fast == slow:
            return True
    # Nếu không gặp nhau, có nghĩa là không có vòng lặp
    return False


# 3. Tìm điểm giao nhau của 2 danh sách liên kết

# Định nghĩa hàm để tìm độ dài của một danh sách liên kết
def get_length(head):
    # Khởi tạo một biến để lưu độ dài
    length = 0
    # Duyệt qua danh sách liên kết và tăng độ dài mỗi lần
    current = head
    while current:
        length += 1
        current = current.next
    # Trả về độ dài
    return length


# Định nghĩa hàm để tìm điểm giao nhau của hai danh sách liên kết
def find_intersection(headA, headB):
    # Tìm độ dài của hai danh sách liên kết
    lenA = get_length(headA)
    lenB = get_length(headB)
    # Khởi tạo hai con trỏ từ hai phần tử đầu tiên của hai danh sách
    currentA = headA
    currentB = headB
    # Nếu độ dài của danh sách A lớn hơn danh sách B, di chuyển con trỏ A đến khi hai danh sách có cùng độ dài
    while lenA > lenB:
        currentA = currentA.next
        lenA -= 1
    # Nếu độ dài của danh sách B lớn hơn danh sách A, di chuyển con trỏ B đến khi hai danh sách có cùng độ dài
    while lenB > lenA:
        currentB = currentB.next
        lenB -= 1
    # Duyệt qua hai danh sách liên kết cho đến khi gặp phần tử chung hoặc hết danh sách
    while currentA and currentB:
        # Nếu hai con trỏ trỏ đến cùng một phần tử, trả về phần tử đó
        if currentA == currentB:
            return currentA
        # Di chuyển hai con trỏ sang phần tử tiếp theo
        currentA = currentA.next
        currentB = currentB.next
    # Nếu không tìm thấy phần tử chung, trả về None
    return None


# 4. Kiểm tra danh sách liên kết có phải Palindrome

# Định nghĩa hàm để kiểm tra một danh sách liên kết có phải là Palindrome hay không
def is_palindrome(head):
    # Khởi tạo hai con trỏ nhanh và chậm từ phần tử đầu tiên
    fast = head
    slow = head
    # Khởi tạo một ngăn xếp để lưu các phần tử của nửa đầu danh sách
    stack = []
    # Duyệt qua danh sách liên kết cho đến khi con trỏ nhanh hết danh sách hoặc chỉ còn một phần tử
    while fast and fast.next:
        # Đẩy phần tử mà con trỏ chậm đang trỏ vào ngăn xếp
        stack.append(slow.data)
        # Di chuyển con trỏ nhanh hai bước mỗi lần
        fast = fast.next.next
        # Di chuyển con trỏ chậm một bước mỗi lần
        slow = slow.next
    # Nếu số phần tử của danh sách là lẻ, bỏ qua phần tử giữa
    if fast:
        slow = slow.next
    # Duyệt qua nửa sau của danh sách liên kết
    while slow:
        # So sánh phần tử mà con trỏ chậm đang trỏ với phần tử được rút ra từ ngăn xếp
        if slow.data != stack.pop():
            # Nếu khác nhau, trả về False
            return False
        # Di chuyển con trỏ chậm sang phần tử tiếp theo
        slow = slow.next
    # Nếu tất cả các phần tử đều giống nhau, trả về True
    return True
