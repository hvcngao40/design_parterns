
class Product(object):
    pass


class Shoe(Product):
    pass


class Shirt(Product):
    pass


class Hat(Product):
    pass


class Glass(Product):
    pass


class SimpleFactory:  # Đây là 1 nhà máy đơn giản: gom nhiều sản phẩm vào và sản xuất chúng
    def __init__(self):
        self.shoe = Shoe()
        self.shirt = Shirt()
        self.hat = Hat()
        self.glass = Glass()

    def create_casual_style(self):
        pass

    def create_formal_style(self):
        pass

