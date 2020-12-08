# Binary Tree in Python

#

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

#### TRAVERSALS ####

## Depth First Traversal Methods (DFS) ##
# Complexities
# Runtime: O(n + m) n = # of nodes, m = # edges (Graph Like)
# Due to there being two edges, it's just O(n)
# Space: O(h), h = height of tree

# Inorder BST Traversal
# Left Child, root, right child
def inorder(root):
	if root == None:
		return
	inorder(root.left)
	print(root.data)
	inorder(root.right)

# Preorder BST Traversal
# Root, left, right
def preorder(root):
	if root == None:
		return
	print(root.data)
	inorder(root.left)
	inorder(root.right)

# Postorder BST Traversal	
# Left, right, root
def postorder(root):
	if root == None:
		return
	inorder(root.left)
	inorder(root.right)	
	print(root.data)

## Breadth First Traversal ##
# For level order traversals
def bfs(root):
	queue = [root]
	while queue:
		current_node = queue.pop(0)
		print(current_node.data)
		if current_node.left:
			queue.append(current_node.left)
		if current_node.right:
			queue.append(current_node.right)


### SEARCH ALGOS ###

# Binary Search
def binary_search(root, val):
	if root is None or root.data == val:
		return root

	if val > root.data:
		return binary_search(root.right, val)

	return binary_search(root.left,val)

if __name__ == "__main__":
	new_tree = Node(5)
	new_tree.left = Node(4)
	new_tree.right = Node(7)
	new_tree.left.left = Node(2)
	new_tree.left.right = Node(3)
	new_tree.right.left = Node(6)
	new_tree.right.right = Node(8)

	print("INORDER")
	inorder(new_tree)
	print("BFS")
	bfs(new_tree)

	print("Binary Search")
	print(binary_search(new_tree, 8).data)
	print(binary_search(new_tree, 100))
