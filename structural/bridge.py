'''Mục đích là tách thanh 2 phần phát triển độc lập: abstraction và implementation. Trong đó lớp được Implementation
được dùng trong lớp abstraction. Như vậy khi thêm abstraction mơi ta có thể thoải mái dùng các implementation khác
mà chẳng liên quan gì với abstraction cũ.
Sự khác biệt chính với adapter là adapter chỉ mới mục đích giúp 2 lớp giao tiếp với nhau, quy về cùng 1 chuẩn
Còn Bridge là muốn mo rộng, phát triển độc lâp 2 nhóm đối tượng này.
Ví dụ dươi day là điểm chạm giữa adapter và bridge về mặt cấu trúc
'''
from abc import abstractmethod, ABC


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class PaymentProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, amount):
        self.payment_gateway.process_payment(amount)


class CreditCardPayment:
    def send_payment(self, amount):
        print(f"Sending credit card payment of {amount} dollars")


class EWalletPayment:
    def make_payment(self, amount):
        print(f"Making e-wallet payment of {amount} dollars")


######  Adapter - ngữ cảnh: đã có các lớp trên và cần chuyển Các phương thức thanh toán khác về Payment của PayPal


class PayPalAdapter(PaymentGateway):
    def __init__(self, paypal_payment):
        self.paypal_payment = paypal_payment

    def process_payment(self, amount):
        self.paypal_payment.make_payment(amount)


########  Bridge: tách các implementation là các lớp phương thức thanh toán qua vi như: Momo, ViettelPay, ck MB,....
# Còn abstractions là lớp thanh toán của ứng dụng: chuyen khoan Ngan hang, thanh toán vi momo,......


class ImplementationPayment:
    @abstractmethod
    def pay(self, amount):
        pass


class MomoPay(ImplementationPayment):
    def pay(self, amount):
        print(f"Momo payment {amount}")


class ViettelPay(ImplementationPayment):
    def pay(self, amount):
        print(f"Viettel pay payment of {amount} dollars")


class ZaloPay(ImplementationPayment):
    def pay(self, amount):
        print(f"Zalo pay payment of {amount} dollars")


class AbstractionEWalletPayment:
    def __init__(self, implementation_payment: ImplementationPayment):
        self.implementation_payment = implementation_payment

    def process_payment(self, amount):
        self.implementation_payment.pay(amount)


if __name__ == '__main__':
    # adapter
    print("ADAPTER")
    credit_card_payment = CreditCardPayment()
    ewallet_payment = EWalletPayment()

    paypal_adapter = PayPalAdapter(ewallet_payment)
    payment_processor = PaymentProcessor(paypal_adapter)

    payment_processor.process_payment(100)  # Output: "Making e-wallet payment of 100 dollars"
    # Bridge
    print("BRIDGE")
    shipper_pay = MomoPay()
    app_payment = AbstractionEWalletPayment(shipper_pay)
    app_payment.process_payment(100)
    credit_pay = ViettelPay()
    app_payment.implementation_payment = credit_pay
    app_payment.process_payment(100)
