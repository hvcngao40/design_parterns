'''Mục đích của prototype đơn giản là lấy giá trị của 1 instance, đơn giản trong python có hỗ trợ deepcopy'''
import copy
from abc import ABC


class Product(ABC):
    def __init__(self):
        self.name = self.size = self.color = None

    def __str__(self):
        return f"{self.name} có size là {self.size} và màu {self.color}"

    def __eq__(self, other):
        if isinstance(self, self.__class__):
            return (self.name == other.name and
                    self.size == other.size and
                    self.color == other.color)
        return False


class Shoe(Product):
    def __init__(self):
        self.name = "Giầy"
        self.size = 30
        self.color = "trắng"


class Shirt(Product):
    def __init__(self):
        self.name = "Áo"
        self.size = "L"
        self.color = "Đen"


class Hat(Product):
    def __init__(self):
        self.name = "Mũ"
        self.size = "M"
        self.color = "Đỏ"


class Glass(Product):
    pass


class DressFactory(ABC):
    def __init__(self):
        self.shoe = Shoe()
        self.shirt = Shirt()
        self.hat = Hat()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (
                    self.shoe == other.shoe and
                    self.shirt == other.shirt and
                    self.hat == other.hat
            )
        return False

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    prototype_factory = DressFactory()
    copy_factory = prototype_factory.clone()
    if prototype_factory == copy_factory:
        print("copied")
    else:
        print('No copied')
