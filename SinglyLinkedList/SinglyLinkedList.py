
#!/usr/bin/python

class Node:

	def __init__(self, data):
		self.item = data
		self.ref = None

class LinkedList:

	def __init__(self):
		self.head = None

	def insert_at_end(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		n = self.head
		while n.ref is not None:
			n = n.ref
		n.ref = new_node

	def insert_at_start(self, data):
		new_node = Node(data)
		new_node.ref = self.head
		self.head = new_node

	def insert_after_item(self, x, data):
		n = self.head
		while n is not None:
			if n.item == x:
				break
			n = n.ref
		if n is None:
			print("Item " + str(x) + " not found in the list\n")
			return
		new_node = Node(data)
		new_node.ref = n.ref
		n.ref = new_node

	def insert_before_item(self, x, data):
		new_node = Node(data)
		if self.head == x:
			new_node.ref = self.head
			self.head = new_node
			return
		n = self.head
		while n.ref is not None:
			if n.ref.item == x:
				break
			n = n.ref
		if n.ref is None:
			print("Item " + str(x) + " not found in the list\n")
			return
		new_node.ref = n.ref
		n.ref = new_node

	def insert_at_index(self, index, data):
		if index == 1:
			new_node = Node(data)
			new_node.ref = self.head
			self.head = new_node
			return

		i = 1
		n = self.head
		while i < index - 1 and n is not None:
			i = i + 1
			n = n.ref

		if n is None:
			print("Index " + str(index) + " is out of bounds\n")
			return

		new_node = Node(data)
		new_node.ref = n.ref
		n.ref = new_node

	def get_count(self):
		count = 0
		n = self.head
		while n is not None:
			count = count + 1
			n = n.ref
		return count

	def search_item(self, data):
		if self.head is None:
			print("The list is empty")
			return False
		n = self.head
		while n is not None:
			if n.item == data:
				print("Item " + str(data) + " present in the list\n")
				return True
			n = n.ref

		print("Item " + str(data) + " not present in the list\n")
		return False

	def delete_at_start(self):
		if self.head is None:
			print("The list is empty")
			return
		self.head = self.head.ref

	def delete_at_end(self):
		if self.head is None:
			print("The list is empty")
			return
		n = self.head
		while n.ref.ref is not None:
			n = n.ref
		n.ref = None

	def delete_element_by_value(self, data):
		if self.head is None:
			print("The list is empty")
			return
		if self.head.item == data:
			self.head = self.head.ref
			return
		n = self.head
		while n.ref is not None:
			if n.ref.item == data:
				break
			n = n.ref
		if n.ref is None:
			print("The item " + str(data) + " to delete not in list\n")
			return
		n.ref = n.ref.ref

	def delete_by_index(self, index):
		if index == 1:
			self.head = self.head.ref
			return
		i = 1
		n = self.head
		while i < index - 1 and n.ref is not None:
			n = n.ref
			i = i + 1
		if n.ref is None:
			print("The index " + str(index) + " out of bounds")
			return
		n.ref = n.ref.ref

	def reverse_linkedlist(self):
		prev = None
		current = self.head
		while current is not None:
			next = current.ref
			current.ref = prev
			prev = current
			current = next
		self.head = prev

	def bubble_sort_change_data(self):
		end = None
		while end != self.head:
			p = self.head
			while p.ref != end:
				q = p.ref
				if p.item > q.item:
					p.item, q.item = q.item, p.item
				p = p.ref
			end = p

	def bubble_sort_change_link(self):
		end = None
		while end != self.head:
			r = p = self.head
			while p.ref != end:
				q = p.ref
				if p.item > q.item:
					p.ref = q.ref
					q.ref = p
					if p != self.head:
						r.ref = q
					else:
						self.head = q
					p, q = q, p
				r = p
				p = p.ref
			end = p

	def make_new_list(self):
		nums = int(input("How many nodes do you want:"))
		if nums == 0:
			print("What a waste of my use")
			return
		for i in range(nums):
			value = int(input("Enter the value of the node:"))
			self.insert_at_end(value)

	def traverse_list(self):
		n = self.head
		while n is not None:
			print(n.item," ")
			n = n.ref


