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


class Factory(ABC):
    @abstractmethod
    def create_product(self):
        pass


class ShoeFactory(Factory):
    def __init__(self):
        self.shoe = None

    def create_product(self):
        self.shoe = Shoe()
        return f"Shoe Product in Factory"

    def get_material(self):
        pass

    def use_machine(self):
        pass

    def get_size(self):
        self.shoe.size = 38

    def add_decorator(self):
        pass


class ShirtFactory(Factory):
    def __init__(self):
        self.shirt = None

    def create_product(self):
        self.shirt = Shirt()
        return f"Shirt Product in Factory"

    def get_material(self):
        pass

    def use_machine(self):
        pass

    def get_size(self):
        self.shirt.size = 31

    def add_decorator(self):
        pass


class HatFactory(Factory):
    def __init__(self):
        self.hat = None

    def create_product(self):
        self.hat = Hat()
        return f"Hat Product in Factory"

    def get_material(self):
        pass

    def use_machine(self):
        pass

    def get_size(self):
        self.hat.size = 'L'

    def add_decorator(self):
        pass


'''Như bạn thấy trong phương thức này mỗi sản phẩm ta tao ra 1 nhà máydđể tạo ra sản phẩm.
Khi có thêm sản phẩm mới thì bạn sẽ không phải sửa thông tin cũ nhu Simple Factory. 
Thêm 1 class về product và ProductFactory mới là xong'''


def operate_product(factory: Factory):
    print(factory.create_product())


if __name__ == '__main__':
    shoe_factory = ShoeFactory()
    operate_product(shoe_factory)

    hat_factory = HatFactory()
    operate_product(hat_factory)
