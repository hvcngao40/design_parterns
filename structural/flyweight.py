'''Tiê kiệm RAM bằng cách chia sẻ tài nguyên của 1 số đối tưựng: thuộc tính chung (hay tĩnh) flyweight
Cần lưu ý về tính toàn vẹn dữ liệu, vì nếu thay đổi dữ liêu của 1dđối tượng thì các đối tượng khác có thể thay đổi chung
Dữ liệu Ram có thể chuyển sang độ phức tạp của CPU khi phải tính toán lại nhiều

Sử dụng khi phải tạo nhiều đối tượng, các đội tượng có điểm chung và có thể tối ưu tài nguyên
Flyweight pattern chia thành hai loại đối tượng: flyweight objects và context objects.
Flyweight objects chứa các thuộc tính không thay đổi và có thể được chia sẻ giữa các trường hợp khác nhau.
Context objects chứa các thuộc tính có thể thay đổi và không được chia sẻ.

Nhận xét: khá giống Singleton nhưng khác biệt ở 2 điểm: 1 là SingleTon là 1 instance còn Flyweight là nhiều, 2 là
SingleTon có thể thay đổi còn flyweight dữ liệu không thay đổi
Ứng dụng: hệ thống đồ họa, GPS, video game, xử lý ngôn ngữ tự nhiên (dùng làm từ điển)
'''


class CharacterFlyweight:
    def __init__(self, character_type, image=''):
        self.character_type = character_type
        self.image = image

    def render(self, position_x, position_y):
        print(f"Rendering a {self.character_type} character with image {self.image} at position ({position_x}, {position_y})")


class CharacterFlyweightFactory:
    def __init__(self):
        self.characters = {}

    def get_character(self, character_type):
        if character_type not in self.characters:
            self.characters[character_type] = CharacterFlyweight(character_type)
        return self.characters[character_type]


# Sử dụng trong ứng dụng
factory = CharacterFlyweightFactory()
character1 = factory.get_character("enemy")  # đối tượng flyweight
character2 = factory.get_character("enemy")  # tái sử dụng đối tượng flyweight

character1.render(100, 200)  # Output: Rendering an enemy character at position (100, 200)
character2.render(300, 400)  # Output: Rendering an enemy character at position (300, 400)



'''Composite with flyweight'''


class TreeComponent:
    def operation(self):
        pass


class Leaf(TreeComponent):
    def __init__(self, name):
        self.name = name

    def operation(self):
        print(f"Leaf {self.name} is performing operation")


class Composite(TreeComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        print(f"Composite {self.name} is performing operation")
        for child in self.children:
            child.operation()


class TreeFlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_leaf(self, name):
        if name not in self.flyweights:
            self.flyweights[name] = Leaf(name)
        return self.flyweights[name]


# Usage in application
factory = TreeFlyweightFactory()

# Create the composite tree
root = Composite("Root")
branch1 = Composite("Branch 1")
branch2 = Composite("Branch 2")

# Create and add shared leaf nodes
leafA = factory.get_leaf("Leaf A")  # Shared leaf node
leafB = factory.get_leaf("Leaf B")  # Shared leaf node
leafC = factory.get_leaf("Leaf C")  # Shared leaf node
leafD = factory.get_leaf("Leaf D")  # Shared leaf node

root.add(branch1)
root.add(branch2)
branch1.add(leafA)
branch1.add(leafB)
branch1.add(leafD)
branch2.add(leafC)
branch2.add(leafD)

# Perform operations on the composite tree
root.operation()
