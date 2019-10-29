
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


new_linked_list = LinkedList()
new_linked_list.insert_at_end(4)
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(1)

new_linked_list.insert_at_start(451)
new_linked_list.insert_at_start(154)
new_linked_list.insert_at_start(155)

new_linked_list.insert_after_item(5, 51)
new_linked_list.insert_after_item(154, 11)
new_linked_list.insert_after_item(1, 111)

new_linked_list.insert_before_item(1, 451)
new_linked_list.insert_before_item(4, 4511)
new_linked_list.insert_before_item(2, 45)

#new_linked_list.insert_after_item(4511, 11)

new_linked_list.insert_at_index(1, 41)
new_linked_list.insert_at_index(2, 42)
new_linked_list.insert_at_index(7, 43)
new_linked_list.insert_at_index(12, 45)
new_linked_list.insert_at_index(17, 3313)

new_linked_list.traverse_list()

print("\nThe total elements in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.search_item(4511)
new_linked_list.search_item(45)
new_linked_list.search_item(4521)


'''new_linked_list.bubble_sort_change_data()
print("sorted LinkedList\n")
new_linked_list.traverse_list()
'''

new_linked_list.bubble_sort_change_link()
print("sorted LinkedList\n")
new_linked_list.traverse_list()

'''print("\n")
new_linked_list.delete_at_start()
new_linked_list.traverse_list()
print("\nThe total elements after first deletion at start in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.delete_at_start()
new_linked_list.traverse_list()
print("The total elements after second deletion at start in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.delete_at_end()
new_linked_list.traverse_list()
print("The total elements after first deletion at end in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.delete_at_end()
new_linked_list.traverse_list()
print("The total elements after second deletion at end in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")


new_linked_list.delete_element_by_value(45)
new_linked_list.traverse_list()
print("The total elements after deleting item 45 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")
new_linked_list.delete_element_by_value(4)
new_linked_list.traverse_list()
print("The total elements after deleting item 4 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")
new_linked_list.delete_element_by_value(4522)
new_linked_list.traverse_list()
print("The total elements after deleting item 4522 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.delete_by_index(1)
new_linked_list.traverse_list()
print("The total elements after deletion at index 1 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.delete_by_index(5)
new_linked_list.traverse_list()
print("The total elements after deletion at index 5 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.delete_by_index(7)
new_linked_list.traverse_list()
print("The total elements after deletion at index 7 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.delete_by_index(19)
new_linked_list.traverse_list()
print("The total elements after deletion at index 19 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")

new_linked_list.reverse_linkedlist()
print("The reversed linkedlist is \n")
new_linked_list.traverse_list()

new_linked_list.delete_element_by_value(3313)
print("\n")
new_linked_list.traverse_list()
print("The total elements after deleting item 3313 in the linkedlist are:" 
	+ str(new_linked_list.get_count()) + "\n")
'''

another_new_linked_list = LinkedList()
another_new_linked_list.make_new_list()
another_new_linked_list.traverse_list()
print("\n")

another_new_linked_list.bubble_sort_change_link()
another_new_linked_list.traverse_list()