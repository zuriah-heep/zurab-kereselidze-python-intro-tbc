class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, v):
        self._balance = v

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print('საკმარისი თანხა არ არის')
        else:
            self._balance -= amount

    @property
    def get_balance(self):
        return self._balance

def main():
    z = BankAccount(100)
    print('ბალანსი -', z.get_balance)
    print('ჩავრიცხოთ 40')
    z.deposit(40)
    print('ბალანსი -', z.get_balance)
    print('გამოვიტანოთ 60')
    z.withdraw(60)
    print('ბალანსი -', z.get_balance)
    print('ვეცადოთ 150-ის გამოტანა')
    z.withdraw(150)
    print('ბალანსი -', z.get_balance)

    print(z.balance)

if __name__ == '__main__':
    main()