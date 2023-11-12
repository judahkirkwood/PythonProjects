from abc import ABC, abstractmethod
class rent(ABC):
    def mortgage(self, amount):
        print("Your card will be charged the amount of: ",amount)
#this function is telling us to pass in an argument, but we won't tell you how or what kind
#of data it will be.
        @abstractmethod
        def payment(self, amount):
            pass

class CreditCardPayment(rent):
#here we'vedefined  how to implement the payment function from its parent paySlip class.
    def payment(self, amount):
        print('This month\'s mortgage amount of {} is paid in full.'.format(amount))

obj = CreditCardPayment()
obj.mortgage("$2400")
obj.payment("$2400")
