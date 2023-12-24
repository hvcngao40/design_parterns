# 1A Reverse bằng cách đệ quy
# Định nghĩa một lớp Node để biểu diễn một nút trong danh sách liên kết
class Node:
    def __init__(self, data):
        self.data = data  # giá trị của nút
        self.next = None  # con trỏ đến nút tiếp theo


# Định nghĩa một hàm để đảo ngược một danh sách liên kết bằng đệ quy
def reverse_list(head):
    # Nếu danh sách liên kết rỗng hoặc chỉ có một nút, trả về head
    if head is None or head.next is None:
        return head
    # Gọi đệ quy cho nút tiếp theo
    new_head = reverse_list(head.next)
    # Đặt con trỏ của nút tiếp theo thành head
    head.next.next = head
    # Đặt con trỏ của head thành None
    head.next = None
    # Trả về nút mới làm head của danh sách liên kết đảo ngược
    return new_head


# 1B Reverse bằng dùng 3 con tro: current, next, previous
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # Reverse a sublist: đảo ngược 1 phần của danh sách liên kêt- từ p-> q
    def reverse_sublist(self, p, q):
        if p == q:
            # No need to reverse if p and q are the same
            return self.head

        # Find the node at position p-1
        current = self.head
        previous = None
        i = 0
        while current is not None and i < p - 1:
            previous = current
            current = current.next
            i += 1

        # Store the node at position p-1 to connect later
        p_minus_1 = previous
        # Store the node at position p as the new tail of the reversed sub-list
        new_tail = current

        # Reverse the sub-list from position p to position q
        previous = None
        i = 0
        while current is not None and i < q - p + 1:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            i += 1

        # Connect the reversed sub-list to the rest of the list
        if p_minus_1 is not None:
            p_minus_1.next = previous
        else:
            self.head = previous

        # Connect the new tail of the reversed sub-list to the node at position q+1
        new_tail.next = current

    def reverse_k_elements(self, k):
        if k <= 1 or self.head is None:
            # No need to reverse if k is 1 or less, or if the list is empty
            return self.head

        current = self.head
        previous = None

        while True:
            last_node_of_previous_part = previous
            last_node_of_sub_list = current

            # Reverse k nodes
            i = 0
            while current is not None and i < k:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
                i += 1

            if last_node_of_previous_part is not None:
                # Connect the last node of the previous part to the new head of the reversed sub-list
                last_node_of_previous_part.next = previous
            else:
                # The new head of the list is the head of the reversed sub-list
                self.head = previous

            # Connect the last node of the reversed sub-list to the next node
            last_node_of_sub_list.next = current

            if current is None:
                # Reached the end of the list
                break

            # Move the pointers to the next group of k nodes
            previous = last_node_of_sub_list


if __name__ == '__main__':
    # Create a linked list
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)

    print("Original linked list:")
    my_list.print_list()

    # # Reverse the linked list
    # my_list.reverse()
    # print("Reversed linked list:")
    # my_list.print_list()

    my_list.reverse_k_elements(3)
    my_list.print_list()
