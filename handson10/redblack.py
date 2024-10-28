class RBNode:
    def __init__(self, value, color="R"):
        self.value = value
        self.color = color  # "R" for Red, "B" for Black
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = RBNode(0, color="B")  # Sentinel node for leaves
        self.root = self.TNULL

    def insert(self, value):
        new_node = RBNode(value)
        new_node.left = self.TNULL
        new_node.right = self.TNULL
        new_node.color = "R"
        
        # Standard BST insertion
        y = None
        x = self.root
        while x != self.TNULL:
            y = x
            if new_node.value < x.value:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        
        if y is None:
            self.root = new_node
        elif new_node.value < y.value:
            y.left = new_node
        else:
            y.right = new_node

        if new_node.parent is None:
            new_node.color = "B"
            return

        if new_node.parent.parent is None:
            return

        # Fix the Red-Black Tree properties
        self._fix_insert(new_node)

    def _fix_insert(self, k):
        while k.parent.color == "R":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Uncle node
                if u.color == "R":  # Case 1: Recolor
                    u.color = "B"
                    k.parent.color = "B"
                    k.parent.parent.color = "R"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:  # Case 2: Rotate
                        k = k.parent
                        self._rotate_right(k)
                    k.parent.color = "B"
                    k.parent.parent.color = "R"
                    self._rotate_left(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "R":
                    u.color = "B"
                    k.parent.color = "B"
                    k.parent.parent.color = "R"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._rotate_left(k)
                    k.parent.color = "B"
                    k.parent.parent.color = "R"
                    self._rotate_right(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "B"

    def delete(self, value):
        self._delete_node(self.root, value)

    def _delete_node(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.value == key:
                z = node
            if node.value <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Couldn't find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self._rb_transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self._rb_transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "B":
            self._fix_delete(x)

    def _rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _fix_delete(self, x):
        while x != self.root and x.color == "B":
            if x == x.parent.left:
                s = x.parent.right
                if s.color == "R":
                    s.color = "B"
                    x.parent.color = "R"
                    self._rotate_left(x.parent)
                    s = x.parent.right
                if s.left.color == "B" and s.right.color == "B":
                    s.color = "R"
                    x = x.parent
                else:
                    if s.right.color == "B":
                        s.left.color = "B"
                        s.color = "R"
                        self._rotate_right(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = "B"
                    s.right.color = "B"
                    self._rotate_left(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == "R":
                    s.color = "B"
                    x.parent.color = "R"
                    self._rotate_right(x.parent)
                    s = x.parent.left
                if s.right.color == "B" and s.left.color == "B":
                    s.color = "R"
                    x = x.parent
                else:
                    if s.left.color == "B":
                        s.right.color = "B"
                        s.color = "R"
                        self._rotate_left(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = "B"
                    s.left.color = "B"
                    self._rotate_right(x.parent)
                    x = self.root
        x.color = "B"

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, value):
        node = self.root
        while node != self.TNULL and value != node.value:
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return node if node != self.TNULL else None

    def _minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node
# Utility function to print the tree in order (for debugging)
def inorder_traversal(node, result, TNULL):
    if node != TNULL:
        inorder_traversal(node.left, result, TNULL)
        result.append(node.value)
        inorder_traversal(node.right, result, TNULL)

# Function to verify Red-Black Tree properties
def check_red_black_properties(tree):
    def is_red_black_compliant(node):
        if node == tree.TNULL:
            return True, 1  # Null nodes are black with black height of 1

        # Check for Red-Black Tree properties
        if node.color == "R":
            # Property 4: Red nodes cannot have red children
            if node.left.color == "R" or node.right.color == "R":
                return False, 0
        
        # Recursively check subtrees
        left_valid, left_black_height = is_red_black_compliant(node.left)
        right_valid, right_black_height = is_red_black_compliant(node.right)

        # Property 5: Black heights must be the same
        if left_black_height != right_black_height or not left_valid or not right_valid:
            return False, 0

        # Include this node's color in black height if it is black
        black_height = left_black_height + (1 if node.color == "B" else 0)
        return True, black_height

    # Check root color (Property 2)
    if tree.root.color != "B":
        print("Property 2 violated: Root is not black.")
        return False

    # Validate all nodes and check black height consistency
    is_valid, _ = is_red_black_compliant(tree.root)
    if not is_valid:
        print("Red-Black properties are violated.")
        return False

    return True

# Main testing function
def test_red_black_tree():
    tree = RedBlackTree()

    # Test Insertion
    print("Testing insertion...")
    values_to_insert = [10, 20, 30, 15, 25, 5, 1]
    for value in values_to_insert:
        tree.insert(value)
        assert check_red_black_properties(tree), f"Red-Black properties violated after inserting {value}"
    
    # Verify Inorder Traversal is sorted
    result = []
    inorder_traversal(tree.root, result, tree.TNULL)
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
        inorder_traversal(tree.root, result, tree.TNULL)
        assert check_red_black_properties(tree), f"Red-Black properties violated after deleting {value}"
        assert value not in result, f"Value {value} still present after deletion"
    print("Deletion test passed.")

    # Final Red-Black Property Check
    assert check_red_black_properties(tree), "Red-Black properties are violated in the final tree."
    print("All tests passed successfully, and Red-Black properties are intact.")

# Run the tests
test_red_black_tree()
