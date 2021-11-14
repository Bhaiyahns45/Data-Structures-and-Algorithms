# Hash Table class
class HashTable:

    # Function to initialize the hash table
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for i in range(self.size)]

    # Function to creates iterator object
    def __iter__(self):
        self.i = -1
        self.current = self.buckets
        return self

    # Function to define the next of a iterator
    def __next__(self):
        try:
            if self.i < self.size:
                self.i += 1
                return self.current[self.i]
        except:
            raise StopIteration

    # Function to calculate the hash value for the key
    def hashing_func(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    # Function to insert the data in hash table
    def insert(self, key, value):
        hash_value = self.hashing_func(key)
        key_exists = False
        for i, element in enumerate(self.buckets[hash_value]):
            if element[0] == key:
                key_exists = True
                break
        if key_exists:
            self.buckets[hash_value][i] = (key, value)
        else:
            self.buckets[hash_value].append((key, value))

    # Function to delete the data from the hash table
    def delete(self, key):
        hash_value = self.hashing_func(key)

        key_exists = False
        for i, element in enumerate(self.buckets[hash_value]):
            if element[0] == key:
                key_exists = True
                break
        if key_exists:
            del self.buckets[hash_value][i]
            print(f"\nKey {key} deleted successfully")
        else:
            print(f"\nkey {key} not found in hash table")

    # Function to check whether the hash table contains the key or not
    def contains(self, key):
        hash_value = self.hashing_func(key)
        for n, element in enumerate(self.buckets[hash_value]):
            if element[0] == key:
                return True
        return False

    # Function to get the value from its key
    def get_value_by_key(self, key):
        hash_value = self.hashing_func(key)
        for n, element in enumerate(self.buckets[hash_value]):
            if element[0] == key:
                return element[1]
        return False

    # Function to get the size of the hash table
    def hash_table_size(self):
        return self.size

    # Function to traverse/print the Hash table
    def traverse(self):
        for i in range(len(self.buckets)):
            print(f"[{i}]", end=" ")
            for j in self.buckets[i]:
                print("-->", end=" ")
                print(j, end=" ")
            print()
        print()


# Run function
def run():
    while True:
        try:
            print("-" * 100)
            print(" 1: Insert \n 2: Delete \n 3: Contains \n 4: Get value by key "
                  "\n 5: Size \n 6: Iterator \n 7: Traverse/Print \n 8: Exit")
            print("-" * 100)
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                key = input("\nEnter the key: ")
                value = input("Enter the value: ")
                hash_table.insert(key, value)
            elif choice == 2:
                key = input("\nEnter the key you want to delete: ")
                hash_table.delete(key)
            elif choice == 3:
                key = input("\nEnter the key you want to search: ")
                if hash_table.contains(key):
                    print(f"\nYes, Hash table contain key {key}")
                else:
                    print(f"\nNo, Hash table does not contain key {key}")
            elif choice == 4:
                key = input("\nEnter the key for its value: ")
                value = hash_table.get_value_by_key(key)
                if value:
                    print(f"\nValue = {value}")
                else:
                    print(f"\nkey {key} not found in hash table")
            elif choice == 5:
                print(f"\nSize of Hash table = {hash_table.hash_table_size()}")
            elif choice == 6:
                print("Hash Table:-\n")
                hash_iter = iter(hash_table)
                index = 0
                for i in hash_iter:
                    print(f"[{index}]", end=" ")
                    for j in i:
                        print("-->", end=" ")
                        print(j, end=" ")
                    print()
                    index += 1
                print()
            elif choice == 7:
                print("Hash Table:-\n")
                hash_table.traverse()
            elif choice == 8:
                print("\nProgram Exited")
                break
            else:
                print("\nChoice Not Found!, Please Choose form available choice")
        except ValueError:
            print("\nInvalid Input!, Please enter valid input")


# Main Driver
if __name__ == "__main__":
    try:
        size = int(input("\nEnter the size of hash table: "))
        hash_table = HashTable(size)  # creation of object of Hash table class
        run()  # calling the run function
    except ValueError:
        print("\nInvalid Input!, size should be integer value")
