#!/usr/bin/python

#create a class for Nodes. Objects of this class will be the actual nodes 
#that we insert in our linkedlist.

class Node:	
	
	def __init__(self, data):
		self.item = data
		self.ref = None

#create a class for the linkedlist. This class will contain methods to
#insert, delete, traverse and sort

class LinkedList:

	def __init__(self):
		self.start_node = None

#method to insert items from the end of the linkedlist
	def insert_at_end(self, data):
		new_node = Node(data)
		if self.start_node is None:
			self.start_node = new_node
			return
		node_itr = self.start_node
		while node_itr.ref is not None:
			node_itr = node_itr.ref
		node_itr.ref = new_node

#method to insert items from the begining of the linkedlist
	def insert_at_start(self, data):
		new_node = Node(data)
		new_node.ref = self.start_node
		self.start_node = new_node

#method to insert items after another item of the linkedlist
	def insert_after_item(self, x, data):
		node_itr = self.start_node
#		print(n.ref)
		while node_itr is not None:
			if node_itr.item == x:
				break
			node_itr = node_itr.ref
		if node_itr is None:
			print("The item is not in the list.")
		else:
			new_node = Node(data)
			new_node.ref = node_itr.ref
			node_itr.ref = new_node

#method to insert items before another item of the linkedlist
	def insert_before_item(self, x, data):
		if self.start_node is None:
			print("List has no elements.")
			return

		if x == self.start_node.item:
			new_node = Node(data)
			new_node.ref = self.start_node
			self.start_node = new_node
			return

		n = self.start_node
#		print(n.ref)
		while n.ref is not None:
			if n.ref.item == x:
				break
			n = n.ref
		if n.ref is None:
			print("Item not is list.")
		else:
			new_node = Node(data)
			new_node.ref = n.ref
			n.ref = new_node

#method to insert items at a specific index of the linkedlist
	def insert_at_index(self, index, data):
		if index == 1:
			new_node = Node(data)
			new_node.ref = self.start_node
			self.start_node = new_node

		i = 1
		n = self.start_node
		while i < index-1 and n is not None:
			n = n.ref
			i = i + 1
		if n is None:
			print("Index out of bound")
		else:
			new_node = Node(data)
			new_node.ref = n.ref
			n.ref = new_node

#method to traverse the linkedlist
	def traverse_list(self):
		if self.start_node is None:
			print("The list has no elements.")
			return
		else:
			n = self.start_node
			while n is not None:
				print(n.item , " ")
				n = n.ref

#method to get the total count of elements in the linkedlist
	def get_count(self):
		if self.start_node is None:
			return 0
		n = self.start_node
		count = 0
		while n is not None:
			count = count + 1
			n = n.ref
		return count

#method to search an item in the linkedlist
	def search_item(self, x):
		if self.start_node is None:
			print("The list has no elements.")
			return
		n = self.start_node
		while n is not None:
			if n.item == x:
				print("True. Item found")
				return True
			n = n.ref
		print("False. Not found")
		return False

	def bub_sort_datachange(self):
		end = None
		while end != self.start_node:
			p = self.start_node
			while p.ref != end:
				q = p.ref
				if p.item > q.item:
					p.item, q.item = q.item, p.item
				p = p.ref
			end = p

	def bub_sort_linkchange(self):
		end = None
		while end != self.start_node:
			r = p = self.start_node
			while p.ref != end:
				q = p.ref
				if p.item > q.item:
					p.ref = q.ref
					q.ref = p
					if p != self.start_node:
						r.ref = q
					else:
						self.start_node = q
					p, q = q, p 
				r = p
				p = p.ref
			end = p


new_linked_list = LinkedList()

#new_linked_list.insert_after_item(4, 5)

new_linked_list.insert_at_end(4)
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(1)
new_linked_list.insert_before_item(1, 451)
#new_linked_list.insert_at_start(451)
#new_linked_list.insert_before_item(4, 45)
#new_linked_list.insert_after_item(5, 51)
#new_linked_list.insert_at_index(3, 41)

new_linked_list.traverse_list()
print("The total elements in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

#new_linked_list.search_item(4511)
'''new_linked_list.bub_sort_datachange()
print("sorted LinkedList\n")
new_linked_list.traverse_list()
'''

new_linked_list.bub_sort_linkchange()
print("sorted LinkedList\n")
new_linked_list.traverse_list()