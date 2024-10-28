class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return AVLNode(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def _balance(self, node):
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) >= 0:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        if balance < -1:
            if self._get_balance(node.right) <= 0:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._min_value_node(node.left)

# Utility function to print the tree in order (for debugging)
def inorder_traversal(node, result):
    if node:
        inorder_traversal(node.left, result)
        result.append(node.value)
        inorder_traversal(node.right, result)

# Function to verify AVL Tree properties
def check_avl_properties(tree):
    def is_balanced(node):
        if not node:
            return True, 0  # Null nodes have height 0 and are balanced

        # Recursively check left and right subtrees
        left_balanced, left_height = is_balanced(node.left)
        right_balanced, right_height = is_balanced(node.right)

        # Node balance factor should be at most 1 for AVL
        balance_factor = abs(left_height - right_height)
        if balance_factor > 1:
            print(f"AVL property violated at node with value {node.value}: balance factor is {balance_factor}")
            return False, 0

        # Return balance status and node height
        height = max(left_height, right_height) + 1
        return left_balanced and right_balanced, height

    is_tree_balanced, _ = is_balanced(tree.root)
    return is_tree_balanced

# Main testing function
def test_avl_tree():
    tree = AVLTree()

    # Test Insertion
    print("Testing insertion...")
    values_to_insert = [10, 20, 30, 15, 25, 5, 1]
    for value in values_to_insert:
        tree.insert(value)
        assert check_avl_properties(tree), f"AVL property violated after inserting {value}"
    
    # Verify Inorder Traversal is sorted
    result = []
    inorder_traversal(tree.root, result)
    assert result == sorted(values_to_insert), "Inorder traversal is incorrect after insertions."
    print("Insertion test passed.")
    
    # Test Search
    print("Testing search...")
    for value in values_to_insert:
        node = tree.search(value)
        assert node is not None, f"Search failed for existing value {value}"
    assert tree.search(100) is None, "Search found non-existing value."
    print("Search test passed.")
    
    # Test Deletion
    print("Testing deletion...")
    values_to_delete = [10, 20, 5]
    for value in values_to_delete:
        tree.delete(value)
        result = []
        inorder_traversal(tree.root, result)
        assert check_avl_properties(tree), f"AVL property violated after deleting {value}"
        assert value not in result, f"Value {value} still present after deletion"
    print("Deletion test passed.")

    # Final AVL Property Check
    assert check_avl_properties(tree), "AVL properties are violated in the final tree."
    print("All tests passed successfully, and AVL properties are intact.")

# Run the tests
test_avl_tree()
