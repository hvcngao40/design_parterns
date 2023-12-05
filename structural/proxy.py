'''Tạo lớp trung gian proxy để kiểm soát truy cập, giữ đối tượng gốc ẩn danh, tối ưu hiệu suất bằng cache, chặn và
mở rộng chức năng của lớp chính
lưu ý: tăng phức tạp, Overhead, duy trì kết nối Proxy và đối tượng gốc
ví dụ: credit card là lớp proxy của tài khoản trong ngân hàng
1. Chỉ 1 số client mới có quyền truy cập tới service này
2. Có thể khởi tạo service này sau (khi nó nặng) trong khi hệ thống chính lên trước
3. Khi service đặt trên máy chủ từ xa -> remote server
4. Ghi log - proxy logging
5. Caching proxy, lưu lại đỡ phải gọi đến service nặng tốn thời gian
6. Smart reference, tính toán service không còn dùng thì giải phóng cache, tài nguyên tham chiếu đến nó
'''
# Subject interface
class Subject:
    def request(self):
        pass

# RealSubject
class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request")

# Proxy
class Proxy(Subject):
    def __init__(self):
        self.real_subject = RealSubject()

    def request(self):
        # Thực hiện các hành động bổ sung trước khi gọi đến đối tượng gốc
        print("Proxy: Performing additional actions before calling the RealSubject")

        # Gọi đến đối tượng gốc
        self.real_subject.request()

        # Thực hiện các hành động bổ sung sau khi gọi đến đối tượng gốc
        print("Proxy: Performing additional actions after calling the RealSubject")

# Sử dụng trong ứng dụng
proxy = Proxy()

# Gọi phương thức request thông qua proxy
proxy.request()
