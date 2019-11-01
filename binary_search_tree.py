#!/usr/bin/python3

class Node:

	#Node Class constructor. Initialize the Node.
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def insert(self, data):
		if self.data == data:
			return False
		elif self.data > data:
			if self.left:
				return self.left.insert(data)
			else:
				self.left = Node(data)
				return True
		else:
			if self.right:
				return self.right.insert(data)
			else:
				self.right = Node(data)
				return True

	def search(self, data):
		if self.data == data:
			return self
		elif data < self.data and self.left is not None:
			return self.left.search(data)
		elif data > self.data and self.right is not None:
			return self.right.search(data)
		return "Node with value " + str(data) + " you're searching for not found"

	def GET_MIN_NODE(self, node):
		current = node
		while current.left is not None:
			current = current.left
		return current

	def GET_MAX_NODE(self, node):
		current = node
		while current.right is not None:
			current = current.right
		return current

	def remove(self, data):
		if self is None:
			return None

		if data < self.data:
			self.left = self.left.remove(data)
		elif data > self.data:
			self.right = self.right.remove(data)
		else:
			if self.left is None and self.right is None:
				self = None
			elif self.left is not None and self.right is None:
				temp = self.GET_MAX_NODE(self.left)
				self.data = temp.data
				self.left = self.left.remove(temp.data)
			else:
				temp = self.GET_MIN_NODE(self.right)
				self.data = temp.data
				self.right = self.right.remove(temp.data)

		return self
		

	def preorder(self, l):
		l.append(self.data)
		if self.left:
			self.left.preorder(l)
		if self.right:
			self.right.preorder(l)
		return l

	def inorder(self, l):
		if self.left:
			self.left.inorder(l)
		l.append(self.data)
		if self.right:
			self.right.inorder(l)
		return l

	def postorder(self, l):
		if self.left:
			self.left.postorder(l)
		if self.right:
			self.right.postorder(l)
		l.append(self.data)
		return l


class Tree:

	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			self.root.insert(data)
		else:
			self.root = Node(data)

	def search(self, data):
		if self.root is None:
			print("The tree is empty. Insert values to search")
			return
		return self.root.search(data)

	def remove(self, data):
		if self.root is not None:
			return self.root.remove(data)

	def preorder(self):
		if self.root:
			return self.root.preorder([])
		else:
			return []

	def inorder(self):
		if self.root:
			return self.root.inorder([])
		else:
			return []

	def postorder(self):
		if self.root:
			return self.root.postorder([])
		else:
			return []

	def insert_nodes(self):
		nums = int(input("Enter the number of nodes: "))
		for i in range(nums):
			node_data = int(input("Enter value of Node " + str(i + 1) + ": "))
			self.insert(node_data)

	def remove_nodes(self):
		nums = int(input("Enter number of nodes to delete: "))
		for i in range(nums):
			node_data = int(input("Enter value to be removed in the tree: "))
			self.remove(node_data)


new_bst = Tree()

new_bst.insert_nodes()
print(new_bst.preorder())
print(new_bst.inorder())
print(new_bst.postorder())

new_bst.remove_nodes()

print("\n")
print(new_bst.preorder())
print(new_bst.inorder())
print(new_bst.postorder())
print(new_bst.search(47))