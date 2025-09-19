import numpy as np
class CreditCardPayment:
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment:
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BankTransferPayment:
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of ${amount}")

def make_payment(payment_method, amount):
    payment_method.process_payment(amount)

if __name__ == "__main__":
    amount = 100.0
    
    credit_card_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()
    bank_transfer_payment = BankTransferPayment()
    
    make_payment(credit_card_payment, amount)
    make_payment(paypal_payment, amount)
    make_payment(bank_transfer_payment, amount)

    