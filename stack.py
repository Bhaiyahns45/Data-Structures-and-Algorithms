# Node class
class Node:

    # Function to initialize the node
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack class
class Stack:

    # Function to initialize top of stack
    def __init__(self):
        self.top = None

    # Function to creates iterator object
    def __iter__(self):
        self.current = self.top
        return self

    # Function to define the next of a iterator
    def __next__(self):
        if self.current is not None:
            data = self.current.data
            self.current = self.current.next
            return data
        else:
            raise StopIteration

    # Function to check the stack is empty
    def is_empty(self):
        if self.top is None:
            print("\nStack is empty")
            return True

    # Function to push the element at the top of stack
    def push(self, new_data):
        new_node = Node(new_data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    # Function to pop the element from the top of the stack
    def pop(self):
        if self.is_empty():
            return
        else:
            element = self.top.data
            self.top = self.top.next
            return element

    # Function to get the peek element of the stack
    def peek(self):
        if self.is_empty():
            return
        return self.top.data

    # Function to check whether the stack contains the element or not
    def contains(self, element):
        temp = self.top
        while temp:
            if temp.data == element:
                return True
            temp = temp.next
        return False

    # Function to get the size of the stack
    def stack_size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    # Function to reverse the stack
    def reverse(self):
        if self.is_empty():
            return
        prev = None
        current = self.top
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.top = prev
        return True

    # Function to traverse/print the stack
    def traverse(self):
        temp = self.top
        if self.is_empty():
            return
        print()
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("\n")


# Run function
def run():
    while True:
        try:
            print("-" * 100)
            print(" 1: Push \n 2: Pop \n 3: Peek \n 4: Contains \n 5: Size \n 6: Reverse "
                  "\n 7: Iterator \n 8: Traverse/Print \n 9: Exit")
            print("-" * 100)
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                data = input("\nEnter the data you want to push: ")
                stack.push(data)
            elif choice == 2:
                element = stack.pop()
                if element:
                    print(f"\nPop element is {element}")
            elif choice == 3:
                element = stack.peek()
                if element:
                    print(f"\nPeek element is {element}")
            elif choice == 4:
                if not stack.is_empty():
                    element = input("\nEnter the element you want to search: ")
                    if stack.contains(element):
                        print(f"\nYes, stack contain {element}")
                    else:
                        print(f"\nNo, stack does not contain {element}")
            elif choice == 5:
                print(f"\nSize of stack is = {stack.stack_size()}")
            elif choice == 6:
                if stack.reverse():
                    print("\nStack reversed")
            elif choice == 7:
                if not stack.is_empty():
                    print()
                    stack_iter = iter(stack)
                    for i in stack_iter:
                        print(i, end="-->")
                    print("\n")
            elif choice == 8:
                stack.traverse()
            elif choice == 9:
                print("\nProgram Exited")
                break
            else:
                print("\nChoice Not Found!, Please Choose form available choice")
        except ValueError:
            print("\nInvalid Input!, Please enter valid input")


# Main driver
if __name__ == "__main__":
    stack = Stack()  # creation of object of Stack class
    run()  # calling the run function
