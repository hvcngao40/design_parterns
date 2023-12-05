'''Sử dụng khi bạn muốn thêm 1 số hành vi cho đối tượng trong lúc chạy nó mà không làm thay đổi nội dung bên trong
Hoặc đối tượng khó có thể thêm hành vi khác bằng sử dụng tính kế thừa
'''


def repeat_decorator(func):
    def wrapper(*args, **kwargs):
        print("Bắt đầu lặp lại hàm")
        for _ in range(3):
            result = func(*args, **kwargs)
            print("Kết quả:", result)
        print("Kết thúc lặp lại hàm")
    return wrapper


@repeat_decorator
def add_numbers(a, b):
    return a + b


# Gọi hàm add_numbers sẽ tự động áp dụng decorator repeat_decorator
add_numbers(2, 3)
