class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new node in the binary tree."""
        new_node = Node(key)
        if not self.root:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        """Helper function to insert a new node in the binary tree."""
        if current.left is None:
            current.left = new_node
        elif current.right is None:
            current.right = new_node
        else:
            # Recur on the left child first
            self._insert_recursive(current.left, new_node)

    def search(self, key):
        """Search for a node in the binary tree."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return None
        if node.val == key:
            return node
        left_result = self._search_recursive(node.left, key)
        if left_result:
            return left_result
        return self._search_recursive(node.right, key)

    def update(self, old_key, new_key):
        """Update the value of a node in the binary tree."""
        node = self.search(old_key)
        if node:
            node.val = new_key

    def delete(self, key):
        """Delete a node from the binary tree."""
        if not self.root:
            return
        if self.root.val == key:
            self.root = None  # If the root is to be deleted
            return
        
        queue = [self.root]
        target_node = None
        parent_node = None
        
        while queue:
            current = queue.pop(0)
            if current.val == key:
                target_node = current
            if current.left:
                parent_node = current
                queue.append(current.left)
            if current.right:
                parent_node = current
                queue.append(current.right)

        if target_node:
            target_node.val = current.val  # Replace the target's value with the last node's value
            if parent_node.left == current:
                parent_node.left = None
            else:
                parent_node.right = None

    def inorder_traversal(self, node):
        """Perform in-order traversal of the binary tree."""
        if node:
            self.inorder_traversal(node.left)
            print(node.val, end=' ')
            self.inorder_traversal(node.right)


# Example usage
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)

    print("Inorder traversal of the tree:")
    tree.inorder_traversal(tree.root)
    print()

    print("Search for node 30:", tree.search(30))
    print("Search for node 60:", tree.search(60))

    print("Updating node 30 to 35...")
    tree.update(30, 35)

    print("Inorder traversal after update:")
    tree.inorder_traversal(tree.root)
    print()

    print("Deleting node 20...")
    tree.delete(20)

    print("Inorder traversal after deletion:")
    tree.inorder_traversal(tree.root)
    print()
