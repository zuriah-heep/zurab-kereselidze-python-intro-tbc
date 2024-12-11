# ამოცანაში ალბათ იგულისხმება რომ pop() არამარტო აბრუნებს პირველ ელემენტს, არამედ შლის კიდევაც.

class Queue:
    def __init__(self):
        self.my_list = []

    def insert(self, element):
        self.my_list.append(element)

    def pop(self):
        if self.my_list:
            first = self.my_list[0]
            #თუ წაშლა არ იგულისხმება და მარტო პირველი ელემენტი უნდა აბრუნოს განუწყვეტლივ მაშინ მე-14 ხაზი უნდა მოსცილდეს.
            del self.my_list[0]
            return first
        else:
            return 'List is empty.'

def main():
    q = Queue()
    q.insert(1)
    q.insert(2)
    q.insert(3)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

if __name__ == '__main__':
    main()