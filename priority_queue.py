# Node class
class Node:

    # Function to initialize the node
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None


# Priority Queue class
class PriorityQueue:

    # Function to initialize front queue
    def __init__(self):
        self.front = None

    # Function to creates iterator object
    def __iter__(self):
        self.current = self.front
        return self

    # Function to define the next of a iterator
    def __next__(self):
        if self.current is not None:
            data = self.current.data
            prio = self.current.priority
            self.current = self.current.next
            return data, prio
        else:
            raise StopIteration

    # Function to check the queue is empty
    def is_empty(self):
        if self.front is None:
            print("\nQueue is empty")
            return True

    # Function to enqueue the element in queue
    def enqueue(self, new_data, priority):
        new_node = Node(new_data, priority)
        if self.front is None or self.front.priority > priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    # Function to dequeue the element from the queue
    def dequeue(self):
        if self.is_empty():
            return
        else:
            element = self.front.data
            self.front = self.front.next
            return element

    # Function to get the peek element of the queue
    def peek(self):
        if self.is_empty():
            return
        return self.front.data

    # Function to check whether the queue contains the element or not
    def contains(self, element):
        temp = self.front
        while temp:
            if temp.data == element:
                return True
            temp = temp.next
        return False

    # Function to get the size of the queue
    def queue_size(self):
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    # Function to reverse the queue
    def reverse(self):
        if self.is_empty():
            return
        current = self.front
        res = []
        while current:
            res.append([current.data, current.priority])
            current = current.next
        res = res[::-1]
        return res

    # Function to traverse/print the queue
    def traverse(self):
        if self.is_empty():
            return
        temp = self.front
        print()
        while temp:
            print(f"{temp.data} prio[{temp.priority}]", end="--> ")
            temp = temp.next
        print("\n")


# Run function
def run():
    while True:
        try:
            print("-" * 100)
            print(" 1: Enqueue \n 2: Dequeue \n 3: Peek \n 4: Contains \n 5: Size "
                  "\n 6: Reverse \n 7: Iterator \n 8: Traverse/Print \n 9: Exit")
            print("-" * 100)
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                element = input("\nEnter the element you want to insert: ")
                priority = int(input("Enter its priority: "))
                queue.enqueue(element, priority)
            elif choice == 2:
                element = queue.dequeue()
                if element:
                    print(f"\nDequeue element is {element}")
            elif choice == 3:
                element = queue.peek()
                if element:
                    print(f"\nPeek element is {element}")
            elif choice == 4:
                if not queue.is_empty():
                    element = input("\nEnter the element you want to search: ")
                    if queue.contains(element):
                        print(f"\nYes, Queue contain {element}")
                    else:
                        print(f"\nNo, Queue does not contain {element}")
            elif choice == 5:
                print(f"\nSize of queue is = {queue.queue_size()}")
            elif choice == 6:
                if queue.reverse():
                    queue_rev = queue.reverse()
                    print("\nReverse priority queue:-\n")
                    for i in queue_rev:
                        print(f"{i[0]} prio[{i[1]}]", end="--> ")
                    print()
            elif choice == 7:
                if not queue.is_empty():
                    queue_iter = iter(queue)
                    print()
                    for element, prio in queue_iter:
                        print(f"{element} prio[{prio}]", end="--> ")
                    print("\n")
            elif choice == 8:
                queue.traverse()
            elif choice == 9:
                print("\nProgram Exited")
                break
            else:
                print("\nChoice Not Found!, Please Choose form available choice")
        except ValueError:
            print("\nInvalid Input!, Please enter valid input")


# Main Driver
if __name__ == "__main__":
    queue = PriorityQueue()  # creation of object of Priority Queue class
    run()  # calling the run function
