class Stack:
    def __init__(self, size_stack):
        self.size_stack = size_stack
        self.data = [None]*size_stack
        self.top = -1

    def push_stack(self, data):
        if self.top == (self.size_stack) -1:
            print("Stack is Full!")
            return
        self.top += 1
        self.data[self.top] = data
        

    def pop_stack(self):
        if self.top == -1:
            print("Stack is empty!")
            return
        # self.top -= 1
        data = self.data[self.top]
        self.top -= 1
        print("Stack value is: ", data)


    
if __name__ == '__main__':
    stack = Stack(5)
    
    stack.push_stack(1)
    stack.push_stack(2)
    stack.push_stack(3)
    stack.push_stack(4)
    stack.push_stack(5)
    stack.push_stack(6)

    stack.pop_stack()
    stack.pop_stack()
    stack.pop_stack()
    stack.pop_stack()
    stack.pop_stack()
    stack.pop_stack()

