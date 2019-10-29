#Implementation of a Queue using a linkedlist

class Node:

	def __init__(self, data):
		self.item = data
		self.ref = None

class Queue:

	def __init__(self):
		self.first = self.last = None

	def enqueue(self, data):
		new_node = Node(data)
		if self.last is None:
			self.first = self.last = new_node
			return
		self.last.ref = new_node
		self.last = new_node

	def dequeue(self):
		if self.first is None:
			print("Not enough values in the Queue to be dequeued.")
			return
		print("Removed " + str(self.first.item) + " from the Queue.")
		self.first = self.first.ref

	def traverse_queue(self):
		n = self.first
		while n is not None:
			print(n.item)
			n = n.ref

	def add_elements_to_queue(self):
		nums = int(input("How many values do you want to add in the Queue:"))
		if nums == 0:
			print("Wow!! What a waste of time")
		else:
			for i in range(nums):
				value = int(input("Enter the value to be queued:"))
				self.enqueue(value)

	def get_count(self):
		n = self.first
		count = 0
		while n is not None:
			count = count + 1
			n = n.ref
		return count


new_queue = Queue()
new_queue.add_elements_to_queue()
new_queue.traverse_queue()
print("\n")
new_queue.dequeue()
new_queue.dequeue()
new_queue.dequeue()
new_queue.traverse_queue()