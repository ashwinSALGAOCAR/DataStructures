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
				self.left.insert(data)
			else:
				self.left = Node(data)
				return True
		else:
			if self.right:
				self.right.insert(data)
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

	def get_min_node(self, node):
		current = node
		while current.left is not None:
			current = current.left
		return current


	def remove(self, data):
		if self is None:
			return False

		if data < self.data:
			self.left = self.left.remove(data)
		elif data> self.data:
			self.right = self.right.remove(data)
		else:
			if self.left is None:
				temp = self.right
				self = None
				return temp
			if self.right is None:
				temp = self.left
				self = None
				return temp

			temp = self.get_min_node(self.right)
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

new_bst.remove(50)
new_bst.remove(47)
new_bst.remove(60)
new_bst.remove(53)
new_bst.remove(55)
print("\n")
print(new_bst.preorder())
print(new_bst.inorder())
print(new_bst.postorder())
print(new_bst.search(37))