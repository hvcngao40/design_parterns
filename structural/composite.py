'''Cấu trúc cây gồm: Component(định nghĩa giao diện chung), leaf(thực hiện chức năng), composite(gôm leaf bên trong vàcó thể thực hiện
chức năng)
-> Nhược điểm: hiệu xuất kém khi cây lớn và phức tạp. Khi thêm 1 phương thức vào component thì các con của nó đều có
điều này làm tăng độ phức tạp

dùng khi không cần phân biệt caác thành phần leaf hay composite bên trong, mở rộng linh hoạt, không coi trọng hiệu suất
Không dùng nếu các thành phần bên trong cây không TƯƠNG ĐỒNG

Ứng dụng: Giao diện người dùng đa cấp (Component gồm component và các leaf như button, image,...)
Cấu trúc tài liệu: 1 thư mục gồm các thư mục và các file, mỗi thư mục gôm các file khác
Phân cấp sản phẩm
'''


from abc import ABC, abstractmethod


# Component
class OrganizationComponent(ABC):
    @abstractmethod
    def display_info(self):
        pass


# Leaf
class Employee(OrganizationComponent):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Employee: {self.name}, Position: {self.position}")


# Composite
class Department(OrganizationComponent):
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.departments = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def add_department(self, department):
        self.departments.append(department)

    def remove_department(self, department):
        self.departments.remove(department)

    def display_info(self):
        print(f"\nDepartment: {self.name}")
        print("Employees:")
        for employee in self.employees:
            employee.display_info()
        print("Departments:")
        for department in self.departments:
            department.display_info()


# Usage
# Tạo các nhân viên
employee1 = Employee("John Doe", "Software Engineer")
employee2 = Employee("Jane Smith", "Sales Executive")

# Tạo các bộ phận
department1 = Department("CEO")
department2 = Department("Sales")
department3 = Department("Engineering")

# Thêm nhân viên vào bộ phận Sales
department2.add_employee(employee2)

# Thêm nhân viên vào bộ phận Engineering
department3.add_employee(employee1)

# Thêm bộ phận Sales và Engineering vào bộ phận CEO
department1.add_department(department2)
department1.add_department(department3)

# Hiển thị thông tin tổ chức
department1.display_info()


### Ví dụ 2: phân cấp sản phẩm


class ProductComponent:
    def display(self, indent):
        raise NotImplementedError("Phương thức display chưa được triển khai.")


class Product(ProductComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent):
        print(indent + self.name)


class ProductCategory(ProductComponent):
    def __init__(self, name):
        self.name = name
        self.subcategories = []
        self.products = []

    def add_subcategory(self, subcategory):
        self.subcategories.append(subcategory)

    def remove_subcategory(self, subcategory):
        self.subcategories.remove(subcategory)

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def display(self, indent=""):
        print(indent + self.name)
        for subcategory in self.subcategories:
            subcategory.display(indent + "  ")
        for product in self.products:
            product.display(indent + "  ")


# Sử dụng Composite để biểu diễn cây phân cấp danh mục sản phẩm
root_category = ProductCategory("Danh mục gốc")

# Danh mục con 1
subcategory1 = ProductCategory("Danh mục con 1")
subcategory1_1 = ProductCategory("Danh mục con 1.1")
subcategory1_2 = ProductCategory("Danh mục con 1.2")
product1_1_1 = Product("Sản phẩm 1.1.1")
product1_1_2 = Product("Sản phẩm 1.1.2")
subcategory1.add_subcategory(subcategory1_1)
subcategory1.add_subcategory(subcategory1_2)
subcategory1_1.add_product(product1_1_1)
subcategory1_1.add_product(product1_1_2)

# Danh mục con 2
subcategory2 = ProductCategory("Danh mục con 2")
product2_1 = Product("Sản phẩm 2.1")
product2_2 = Product("Sản phẩm 2.2")
subcategory2.add_product(product2_1)
subcategory2.add_product(product2_2)

root_category.add_subcategory(subcategory1)
root_category.add_subcategory(subcategory2)

# Hiển thị cây phân cấp danh mục sản phẩm
root_category.display()
