#!/usr/bin/python3

class Node:

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
		elif self.data > data:
			return self.left.search(data)
		else:
			return self.right.search(data)
		return False

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
		self.root.search(data)

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

	def get_min_node(self, node):
		current = node
		current_parent = None
		while current.left is not None:
			current_parent = current
			current = current.left
			return current, current_parent

	def get_max_node(self, node):
		current = node
		current_parent = None
		while current.right is not None:
			current_parent = current
			current = current.right
			return current, current_parent

	def remove(self, data):

		if self.root == None:
			print("Empty tree")
			return False

		#Case 1: Deleting the Root Node
		if self.root.data == data:
			#Case 1.1: Root Node has no Child Node
			if self.root.left is None and self.root.right is None:
				self.root = None
			
			#Case 1.2: Root Node has left child only
			elif self.root.left and self.root.right is None:
				self.root = self.root.left
			
			#Case 1.3: Root Node has right child only
			elif self.root.left is None and self.root.right:
				self.root = self.root.right
			
			#Case 1.4 Root Node has both Children
			elif self.root.left and self.root.right:
				sub_right = self.root.right
				min_node, min_node_parent = self.get_min_node(sub_right)
				if min_node.right:
					max_node, max_node_parent = get_max_node(min_node)

				self.root.data = min_node.data
				min_node_parent.left = None


new_bst = Tree()
new_bst.insert(50)
new_bst.insert(40)
new_bst.insert(60)
new_bst.insert(35)
new_bst.insert(33)
new_bst.insert(37)
new_bst.insert(45)
new_bst.insert(47)
new_bst.insert(43)
new_bst.insert(55)
new_bst.insert(65)
new_bst.insert(53)
new_bst.insert(57)
new_bst.insert(63)
new_bst.insert(67)
#print(new_bst.preorder())
print(new_bst.inorder())
#print(new_bst.postorder())

#new_bst.remove(50)
#snew_bst.remove(53)
#new_bst.remove(55)
print(new_bst.inorder())
print(new_bst.search(50))