from abc import abstractmethod, ABC


class Product(ABC):
    pass


class Shoe(Product):
    pass


class Shirt(Product):
    pass


class Hat(Product):
    pass


class Glass(Product):
    pass


class DressFactory(ABC):    # lớp abstract factory
    def __init__(self):
        self.shoe = self.shirt = self.hat = None

    @abstractmethod
    def create_shoe(self):
        pass

    @abstractmethod
    def create_shirt(self):
        pass

    @abstractmethod
    def create_hat(self):
        pass

    def create_product_line(self):
        print(self.create_shoe())
        print(self.create_hat())
        print(self.create_shirt())


class CasualDressFactory(DressFactory):

    def create_shoe(self):
        self.shoe = Shoe()
        return f"Shoe Product in Casual Dress Factory"

    def create_shirt(self):
        self.shirt = Shirt()
        return f"Shirt Product in Casual Dress Factory"

    def create_hat(self):
        self.hat = Hat()
        return f"Hat Product in Casual Dress Factory"


class FormalDressFactory(DressFactory):

    def create_shoe(self):
        self.shoe = Shoe()
        return f"Shoe Product in Formal Dress Factory"

    def create_shirt(self):
        self.shirt = Shirt()
        return f"Shirt Product in Formal Dress Factory"

    def create_hat(self):
        self.hat = Hat()
        return f"Hat Product in Formal Dress Factory"


class TrendyDressFactory(DressFactory):

    def create_shoe(self):
        self.shoe = Shoe()
        return f"Shoe Product in Trendy Dress Factory"

    def create_shirt(self):
        self.shirt = Shirt()
        return f"Shirt Product in Trendy Dress Factory"

    def create_hat(self):
        self.hat = Hat()
        return f"Hat Product in Trendy Dress Factory"


'''Như bạn thấy trong phương thức này thay vì tạo nhà máy cho mỗi sản phẩm thì là 1 dòng sản phẩm.
Khi có thêm dòng sản phẩm mới là xong'''


def operate_product_line(factory: DressFactory):
    factory.create_product_line()


if __name__ == '__main__':
    casual_factory = CasualDressFactory()
    operate_product_line(casual_factory)
    print("\n")
    formal_factory = FormalDressFactory()
    operate_product_line(formal_factory)
