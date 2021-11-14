# Node class
class Node:

    # Function to initialize the node
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:

    # Function to initialize head of linked list
    def __init__(self):
        self.head = None

    # Function to creates iterator object
    def __iter__(self):
        self.current = self.head
        return self

    # Function to define the next of a iterator
    def __next__(self):
        if self.current is not None:
            element = self.current.data
            self.current = self.current.next
            return element
        else:
            raise StopIteration

    # Function to check the linked list is empty
    def is_empty(self):
        if self.head is None:
            print("\nLinked list is empty")
            return True

    # Function to insert a new node at the beginning
    def insert_at_the_beginning(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Function to insert a new node at the end
    def insert_at_the_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    # Function to insert a new node at the any position
    def insert_at_any_position(self, pos, new_data):
        if pos > (self.list_size() + 1) or pos < 0:
            print("Invalid Position")
            return
        if pos == 0 or pos == 1:
            self.insert_at_the_beginning(new_data)
        else:
            if pos == self.list_size() + 1:
                self.insert_at_the_end(new_data)
            else:
                new_node = Node(new_data)
                count = 1
                current = self.head
                while count < pos - 1:
                    count += 1
                    current = current.next
                new_node.next = current.next
                current.next = new_node

    # Function to delete a new node from the beginning
    def delete_at_the_beginning(self):
        if self.is_empty():
            return
        else:
            element = self.head.data
            self.head = self.head.next
            return element

    # Function to delete a new node from the end
    def delete_at_the_end(self):
        if self.is_empty():
            return
        elif self.list_size() == 1:
            return self.delete_at_the_beginning()
        else:
            current = self.head
            prev = self.head
            element = current.data
            while current.next is not None:
                prev = current
                current = current.next
                element = current.data
            prev.next = None
            return element

    # Function to delete a new node from the any position
    def delete_at_any_position(self, pos):
        if pos > self.list_size() or pos < 1:
            print("\nInvalid Position")
            return
        if pos == 1:
            return self.delete_at_the_beginning()
        elif pos == self.list_size():
            return self.delete_at_the_end()
        else:
            current = self.head
            prev = self.head
            element = current.data
            count = 1
            while count < pos:
                count += 1
                prev = current
                current = current.next
                element = current.data
            prev.next = current.next
            return element

    # Function to get the center of linked list
    def center(self):
        if self.is_empty():
            return
        else:
            if self.list_size() == 1:
                return self.head.data
            mid = self.list_size() // 2
            count = 1
            current = self.head
            while count < mid:
                count += 1
                current = current.next
            if (self.list_size()) % 2 == 0:
                return current.data
            else:
                return current.next.data

    # Function to reverse the linked list
    def reverse(self):
        if self.is_empty():
            return
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return True

    # Function to get the size of the linked list
    def list_size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    # Function to traverse/print the linked list
    def traverse(self):
        if self.is_empty():
            return
        temp = self.head
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
            print(" 1: Insert \n 2: Delete \n 3: Center \n 4: Reverse \n 5: Size "
                  "\n 6: Iterator \n 7: Traverse/Print \n 8: Exit")
            print("-" * 100)
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                while True:
                    print("-" * 50)
                    print(" 1: Insert at the beginning \n 2: Insert at the end "
                          "\n 3: Insert at any position \n 4: Go Back")
                    print("-" * 50)
                    insert_choice = int(input("Please enter your insert choice: "))
                    if insert_choice == 1:
                        data = input("\nEnter the data you want to insert: ")
                        singly_l_list.insert_at_the_beginning(data)
                    elif insert_choice == 2:
                        data = input("\nEnter the data you want to insert: ")
                        singly_l_list.insert_at_the_end(data)
                    elif insert_choice == 3:
                        pos = int(input("\nEnter the position: "))
                        print()
                        data = input("Enter the data: ")
                        singly_l_list.insert_at_any_position(pos, data)
                    elif insert_choice == 4:
                        break
                    else:
                        print("\nInvalid Choice")
            elif choice == 2:
                while True:
                    print("-" * 50)
                    print(" 1: Delete at the beginning \n 2: Delete at the end "
                          "\n 3: Delete at any position \n 4: Go Back")
                    print("-" * 50)
                    delete_choice = int(input("Please enter your delete choice: "))
                    if delete_choice == 1:
                        element = singly_l_list.delete_at_the_beginning()
                        if element:
                            print(f"\nDeleted element is {element}")
                    elif delete_choice == 2:
                        element = singly_l_list.delete_at_the_end()
                        if element:
                            print(f"\nDeleted element is {element}")
                    elif delete_choice == 3:
                        if not singly_l_list.is_empty():
                            pos = int(input("Enter the position: "))
                            element = singly_l_list.delete_at_any_position(pos)
                            if element:
                                print(f"\nDeleted element is {element}")
                    elif delete_choice == 4:
                        break
                    else:
                        print("\nInvalid Choice")
            elif choice == 3:
                element = singly_l_list.center()
                if element:
                    print(f"\nCenter of linked list is = {element}")
            elif choice == 4:
                if singly_l_list.reverse():
                    print("\nLinked List reversed")
            elif choice == 5:
                print(f"\nSize of linked list is = {singly_l_list.list_size()}")
            elif choice == 6:
                if not singly_l_list.is_empty():
                    print()
                    list_iter = iter(singly_l_list)
                    for i in list_iter:
                        print(i, end="-->")
                    print("\n")
            elif choice == 7:
                singly_l_list.traverse()
            elif choice == 8:
                print("\nProgram Exited")
                break
            else:
                print("\nChoice Not Found!, Please Choose form available choice")
        except ValueError:
            print("\nInvalid Input!, Please enter valid input")


# Main Driver
if __name__ == "__main__":
    singly_l_list = LinkedList()  # creation of object of Linked list class
    run()  # calling the run function
