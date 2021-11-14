# Tree node class
class TreeNode:

    #  Function to initialize the children of root
    def __init__(self, data):
        self.data = data
        self.children = []


# Breadth first iterator class
class BreadthFirstIterator:

    # Function to initialize the root of tree
    def __init__(self, root):
        self.root = root

    # Function to creates iterator object
    def __iter__(self):
        self.stack = [self.root]
        return self

    # Function to define the next of a iterator
    def __next__(self):
        while len(self.stack) != 0:
            n = len(self.stack)
            while n > 0:
                p = self.stack[0]
                self.stack.pop(0)
                for i in range(len(p.children)):
                    self.stack.append(p.children[i])
                n -= 1
                return p.data
        else:
            raise StopIteration


# Depth first iterator class
class DepthFirstIterator:

    # Function to initialize the root of tree
    def __init__(self, root):
        self.root = root

    # Function to creates iterator object
    def __iter__(self):
        self.stack = [self.root]
        return self

    # Function to define the next of a iterator
    def __next__(self):
        while self.stack:
            temp = self.stack.pop()
            x = temp.data
            self.stack.extend(temp.children[::-1])
            return x
        else:
            raise StopIteration


# N Child tree class
class NChildTree:

    # Function to initialize the root of tree
    def __init__(self):
        self.root = None

    # Function to create a new node
    @staticmethod
    def new_node(data):
        temp = TreeNode(data)
        return temp

    # Function to insert the node
    def insert(self, parent):
        try:
            n = int(input(f"Enter the number of children of [{parent.data}] node: "))
            for i in range(1, n + 1):
                ith_child = input(f"Enter the ({i}) child of [{parent.data}] node: ")
                child = self.new_node(ith_child)
                parent.children.append(child)
                self.insert(child)
            print()
        except ValueError:
            print("\nInvalid Input!, Number of children should be integer value")

    # Function to delete all the leaf node present in tree
    def delete(self, root):
        if root is None:
            return
        if len(root.children) == 0:
            return None
        i = 0
        while i < len(root.children):
            child = root.children[i]
            if len(child.children) == 0:
                for j in range(i, len(root.children) - 1):
                    root.children[j] = root.children[j + 1]
                root.children.pop()
                i -= 1
            i += 1

        for i in range(len(root.children)):
            root.children[i] = self.delete(root.children[i])
        return root

    # Function to check whether the tree contains the node element or not
    @staticmethod
    def contains(root, element):
        if root is None:
            return
        q = [root]
        while len(q) != 0:
            n = len(q)
            while n > 0:
                p = q[0]
                q.pop(0)
                if p.data == element:
                    return True
                for i in range(len(p.children)):
                    q.append(p.children[i])
                n -= 1
        return False

    # Function to get the elements by value
    @staticmethod
    def get_element_by_value(root, value):
        ans = []
        stack = [root]
        result = []
        found = False
        while stack:
            temp = stack.pop()

            # if the value matches to the node data
            if value == temp.data:
                ans.extend(temp.children[::-1])
                found = True
                break
            stack.extend(temp.children[::-1])

        if found:
            while ans:
                x = ans.pop()
                result.append(x.data)
            return result, True
        else:
            return result, False

    # Function to get the elements by level
    @staticmethod
    def get_elements_by_level(root, level):
        if root is None:
            return
        try:
            q = [root]
            res = []
            while len(q) != 0:
                n = len(q)
                l = []
                while n > 0:
                    p = q[0]
                    q.pop(0)
                    l.append(p.data)
                    for i in range(len(p.children)):
                        q.append(p.children[i])
                    n -= 1
                res.append(l)
            return res[level]
        except:
            print("\nLevel not found")
            return None

    # Function to print the tree in breadth first (Level order) pattern
    @staticmethod
    def breadth_first(root):
        if root is None:
            return
        q = [root]
        level = 0
        while len(q) != 0:
            n = len(q)
            print(f"L-{level} ->", end=" ")
            # If this node has children
            while n > 0:
                # Dequeue an item from queue and print it
                p = q[0]
                q.pop(0)
                print(p.data, end=" ")
                for i in range(len(p.children)):
                    q.append(p.children[i])
                n -= 1
            print()
            level += 1

    # Function to print the tree in depth first (Preorder) pattern
    @staticmethod
    def depth_first(root):
        ans = []
        stack = [root]
        while stack:
            temp = stack.pop()
            ans.append(temp.data)
            stack.extend(temp.children[::-1])
        return ans


# Run function
def run():
    root = TreeNode(None)  # creating the object of tree node class
    while True:
        try:
            print("-" * 100)
            print(" 1: Insert \n 2: Delete \n 3: Contains \n 4: Get Elements by value \n 5: Get Elements by level "
                  "\n 6: Iterator Breadth First (Level Order Traversal) \n 7: Iterator Depth First (Preorder Traversal)"
                  "\n 8: Traverse Breadth First (Level Order Traversal) \n 9: Traverse Depth First (Preorder Traversal)"
                  "\n 10: Exit")
            print("-" * 100)
            choice = int(input("Please enter your choice: "))
            print("-" * 100)
            if choice == 1:
                root = TreeNode(input("\nEnter the root node: "))
                tree.insert(root)
            elif choice == 2:
                if tree.delete(root):
                    print("\nAll Leaf Nodes Deleted/Remove")
                else:
                    print("\nNone, No leaf node found")
            elif choice == 3:
                element = input("\nEnter the element you want to search: ")
                result = tree.contains(root, element)
                if result:
                    print(f"\nYes, Tree contain {element}")
                else:
                    print(f"\nNo, Tree does not contain {element}")
            elif choice == 4:
                value = input("\nEnter the value to get its element: ")
                res, found = tree.get_element_by_value(root, value)
                if found:
                    if res:
                        print("\nElements (Children of given value) =", *res)
                    else:
                        print("\nNo child exists for given value")
                else:
                    print("\nNo match found")
            elif choice == 5:
                level = int(input("\nEnter the level to get its elements: "))
                result = tree.get_elements_by_level(root, level)
                if result:
                    print(f"\nL-{level} ->", *result)
            elif choice == 6:
                print("\nIterator Breadth First = ", end="")
                iter_class = BreadthFirstIterator(root)
                tree_iter = iter(iter_class)
                for element in tree_iter:
                    print(element, end=" ")
                print()
            elif choice == 7:
                print("\nIterator Depth First = ", end="")
                iter_class = DepthFirstIterator(root)
                tree_iter = iter(iter_class)
                for element in tree_iter:
                    print(element, end=" ")
                print()
            elif choice == 8:
                print("\nBreadth First (Level-order traversal)")
                tree.breadth_first(root)
                print()
            elif choice == 9:
                print("\nDepth First (Pre-order traversal) = ", end="")
                print(*tree.depth_first(root))
                print()
            elif choice == 10:
                print("\nProgram Exited")
                break
            else:
                print("\nChoice Not Found!, Please Choose form available choice")
        except ValueError:
            print("\nInvalid Input!, Please enter valid input")


# Main Driver
if __name__ == "__main__":
    tree = NChildTree()  # creation of object of N-child tree class
    run()  # calling the run function
