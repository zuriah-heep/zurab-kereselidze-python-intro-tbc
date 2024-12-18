class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print('საკმარისი თანხა არ არის')
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance

def main():
    z = BankAccount(100)
    print('ბალანსი -', z.get_balance())
    print('ჩავრიცხოთ 40')
    z.deposit(40)
    print('ბალანსი -', z.get_balance())
    print('გამოვიტანოთ 60')
    z.withdraw(60)
    print('ბალანსი -', z.get_balance())
    print('ვეცადოთ 150-ის გამოტანა')
    z.withdraw(150)
    print('ბალანსი -', z.get_balance())

    #ეს მოგვცემს შეცდომას
    #print(z.balance)

if __name__ == '__main__':
    main()