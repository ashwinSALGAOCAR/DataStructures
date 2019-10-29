class Node:

	def __init__(self, data):
		self.item = data
		self.nref = None
		self.pref = None

class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def insert_at_start(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = self.tail = new_node
			return
		self.head.pref = new_node
		new_node.nref = self.head
		self.head = new_node

	def insert_at_end(self, data):
		new_node = Node(data)
		if self.tail is None:
			self.head = self.tail = new_node
			return
		self.tail.nref = new_node
		new_node.pref = self.tail
		self.tail = new_node

	def insert_before_item(self, x, data):
		if self.head.item == x:
			new_node = Node(data)
			new_node.nref = self.head
			self.head.pref = new_node
			self.head = new_node
			return
		if self.tail.item == x:
			new_node = Node(data)
			new_node.pref = self.tail.pref
			new_node.nref = self.tail
			self.tail.pref.nref = new_node
			self.tail.pref = new_node
			return
		n = self.head
		while n is not None:
			if n.item == x:
				break
			n = n.nref
		if n is None:
			print("Item not in list.")
		else:
			new_node = Node(data)
			new_node.pref = n.pref
			if n.pref is not None:
				n.pref.nref = new_node
			new_node.nref = n
			n.pref = new_node

	def sort_list(self):
		end = self.tail.nref
		while end != self.head:
			p = self.head
			while p.nref != end:
				q = p.nref
				if p.item > q.item:
					p.nref = q.nref
					if q.nref != None:
						q.nref.pref = p
					else:
						self.tail = p
					q.nref = p
					q.pref = p.pref
					if p.pref != None:
						p.pref.nref = q
					else:
						self.head = q
					p.pref = q
					p, q = q, p
				p = p.nref
			end = p

	def reverse_list(self):
		n = self.head
		while n is not None:
			prev = n.pref
			n.pref = n.nref
			n.nref = prev
			n = n.pref

		if prev is not None:
			self.head = prev.pref

	def traverse_list_forward(self):
		n = self.head
		while n is not None:
			print(n.item, "")
			n = n.nref

	def traverse_list_backward(self):
		n = self.tail
		while n is not None:
			print(n.item, "")
			n = n.pref

new_linkedlist = LinkedList()
new_linkedlist.insert_at_start(4)
new_linkedlist.insert_at_start(5)
new_linkedlist.insert_at_start(1)
new_linkedlist.insert_at_start(8)
new_linkedlist.traverse_list_forward()
print("\n")
new_linkedlist.insert_at_end(451)
new_linkedlist.insert_at_end(514)
new_linkedlist.insert_at_end(145)
new_linkedlist.insert_at_end(23)
new_linkedlist.traverse_list_forward()
print("\n")
new_linkedlist.insert_before_item(8, 888)
new_linkedlist.insert_before_item(145, 0)
new_linkedlist.insert_before_item(1, 4511)
new_linkedlist.insert_before_item(23, 4522)
new_linkedlist.traverse_list_forward()
'''print("\n")
new_linkedlist.traverse_list_backward()
'''
print("\n")
new_linkedlist.sort_list()
new_linkedlist.traverse_list_forward()
print("\n")
new_linkedlist.reverse_list()
new_linkedlist.traverse_list_forward()