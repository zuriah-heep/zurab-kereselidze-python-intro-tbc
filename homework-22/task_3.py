class Stack:
    def __init__(self):
        self.my_list = []

    def push(self, element):
        self.my_list.append(element)

    def pop(self):
        if self.my_list:
            last = self.my_list[-1]
            del self.my_list[-1]
            return last

    def peek(self):
        if self.my_list:
            return self.my_list[-1]

    def is_empty(self):
        return False if self.my_list else True

    def size(self):
        return len(self.my_list)

def main():
    s = Stack()
    print(s.is_empty())
    print(s.size())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.peek())
    print(s.is_empty())

if __name__ == '__main__':
    main()