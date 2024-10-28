For each tree implementation, you’ll want to cover the following features and methods:

### 1. **Binary Search Tree (BST)**
   - **Operations**: 
     - `insert`: To add nodes based on BST properties.
     - `delete`: Implement deletion for nodes with no children, one child, or two children.
     - `search`: To locate a node with a specific value.
     - `min` / `max`: To get the minimum or maximum value in the tree.
     - `inorder`, `preorder`, `postorder` traversals: For validating tree structure.

### 2. **Red Black Tree**
   - **Properties**:
     - Each node is either red or black.
     - The root is black.
     - Red nodes cannot have red children.
     - Every path from a node to its descendant leaves must have the same number of black nodes.
   - **Operations**:
     - `insert`: Including rotations and color adjustments.
     - `delete`: Requires more complex adjustments, involving color changes and rotations.
     - `search`: For locating a node.
   - **Rotations**: Implement left and right rotations.
   - **Tests**: Use assertions to check tree balance and color properties after operations.

### 3. **AVL Tree**
   - **Properties**:
     - Self-balancing, with each node maintaining a balance factor.
     - Balance factor kept within -1, 0, or +1 by rotating as necessary.
   - **Operations**:
     - `insert` with balancing.
     - `delete` with rebalancing.
     - `search`: For finding a specific value.
   - **Rotations**: Single and double rotations (LL, RR, LR, RL) based on imbalance type.

### Testing
For each tree, include a testing suite (possibly with `unittest` in Python or an equivalent) to cover:
   - **Basic Insertion**: Confirm that all nodes can be inserted correctly.
   - **Edge Cases**: Test inserting duplicate values and edge values (e.g., min/max integer values).
   - **Deletion Scenarios**: Test deleting leaf nodes, nodes with one child, and nodes with two children.
   - **Traversal Validations**: Ensure traversals return expected order.
   - **Balance and Property Checks** (for Red-Black and AVL Trees): Validate that trees meet their balance requirements after each operation.
### Expected Output
**For bst:**
print("Testing search...")
print("Testing search passed...")
print("Testing deletion...")
print("Testing deletion passed...")


### Expected Output
**For red black tree:**
Testing insertion...
Insertion test passed.
Testing search...
Search test passed.
Testing deletion...
Deletion test passed.
All tests passed successfully, and Red-Black properties are intact.

### Expected Output
**Running test_red_black_tree() should display:**

Testing insertion...
Insertion test passed.
Testing search...
Search test passed.
Testing deletion...
Deletion test passed.
All tests passed successfully, and Red-Black properties are intact.