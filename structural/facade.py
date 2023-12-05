'''Tạo một giao diện để thông qua nó điều khiển những chức năng bên trong (ẩn đi cấu trúc của nó)
Dùng khi hệ thống có cấu trúc bên trong quá phức tạp. Dùng Facade để client tương tác dễ dàng hơn (cung cấp 1 giao
diện thuận tiện)
Ví dụ: Hệ thống tài liệu, tài chính, đa phương tiện, điều khiển thiết bị (IOT), API (swagger)
'''


class ProductManager:
    def get_product_info(self, product_id):
        # Lấy thông tin sản phẩm từ cơ sở dữ liệu
        return f"Thông tin sản phẩm với ID {product_id}"


class CustomerManager:
    def get_customer_info(self, customer_id):
        # Lấy thông tin khách hàng từ cơ sở dữ liệu
        return f"Thông tin khách hàng với ID {customer_id}"


class OrderManager:
    def create_order(self, product_info, customer_info):
        # Tạo đơn hàng và lưu vào cơ sở dữ liệu
        return f"Đơn hàng được tạo với sản phẩm: {product_info}, khách hàng: {customer_info}"


class EmailService:
    def send_email(self, email, message):
        # Gửi email
        print(f"Gửi email đến {email}: {message}")


class OnlineOrderFacade:
    def __init__(self):
        self.product_manager = ProductManager()
        self.customer_manager = CustomerManager()
        self.order_manager = OrderManager()
        self.email_service = EmailService()

    def place_order(self, product_id, customer_id, email):
        product_info = self.product_manager.get_product_info(product_id)
        customer_info = self.customer_manager.get_customer_info(customer_id)
        order_info = self.order_manager.create_order(product_info, customer_info)
        self.email_service.send_email(email, order_info)


# Sử dụng facade để đặt hàng trực tuyến
online_order = OnlineOrderFacade()
online_order.place_order("123", "456", "example@example.com")
