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
			return True
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

#	def remove(self, data):


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

#	def remove(self, data):


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
print(new_bst.preorder())
print(new_bst.inorder())
print(new_bst.postorder())