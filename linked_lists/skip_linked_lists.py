import random

class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level, probability=0.5):
        self.max_level = max_level
        self.probability = probability
        self.head = Node(None, self.max_level)
        self.level = 0  # Current highest level in skip list

    def random_level(self):
        level = 0
        while random.random() < self.probability and level < self.max_level:
            level += 1
        return level

    def insert(self, value):
        new_level = self.random_level()
        new_node = Node(value, new_level)

        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                self.head.forward[i] = None
            self.level = new_level

        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] is not None:
                current = current.forward[i]
            if i <= new_level:
                new_node.forward[i] = current.forward[i]
                current.forward[i] = new_node
        print(f"Inserted {value} at level {new_level}")

    def search(self, value):
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value != value:
                current = current.forward[i]

        current = current.forward[0]
        if current and current.value == value:
            print(f"Found {value}")
            return True
        print(f"{value} not found")
        return False

    def delete(self, value):
        current = self.head
        found = False
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value != value:
                current = current.forward[i]
            if current.forward[i] and current.forward[i].value == value:
                current.forward[i] = current.forward[i].forward[i]
                found = True

        if found:
            print(f"Deleted {value}")
            return True
        else:
            print(f"{value} not found for deletion")
            return False

# Usage example
if __name__ == "__main__":
    max_level = 4
    skip_list = SkipList(max_level)

    # Insert values in original order
    skip_list.insert(9)
    skip_list.insert(5)
    skip_list.insert(3)
    skip_list.insert(7)
    skip_list.insert(1)

    # Search for values
    skip_list.search(7)
    skip_list.search(4)

    # Delete values
    skip_list.delete(3)
    skip_list.delete(1)
