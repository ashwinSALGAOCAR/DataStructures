#!/usr/bin/python3
import math

class MaxHeap:

	def __init__(self):
		self.heap = []

	def insert(self, data):

		'''We begin inserting in the heap by appending new data at the end of the list.
		Then we get the index of the newly inserted child and the height of the heap.
		Since the child node is at the end of the list we would be traversing up the height,
		therefore we will loop through the heap till we reach height 0.
		Since this is a Max Heap we compare the child node with the parent and replace each
		other if the parent is smaller than the child.
		'''

		self.heap.append(data)
		length = len(self.heap)
		child_index = length
		height = math.log(length)
		while height > 0:
			parent_index = int(child_index / 2)
			if self.heap[child_index - 1] > self.heap[parent_index - 1]:
				temp = self.heap[parent_index - 1]
				self.heap[parent_index - 1] = self.heap[child_index - 1]
				self.heap[child_index - 1] = temp
				child_index = parent_index

			height = height - 1

	def delete(self):

		'''We begin from the top node. The node with the heighest value and replace it with
		the last value of the heap and then traverse down the height. We loop till we reach
		one less than the height. In the second loop we untill both child nodes exist. In 
		this loop we move the top node down untill it is pushed to the end of the list and
		eliminated.

		If the node has only left child(even list length means it has only left child), we
		interchange the positions of the child and eliminate the parent.
		'''

		del_node = self.heap[0]
		self.heap[0] = self.heap[- 1]
		self.heap[- 1] = del_node

		self.heap = self.heap[: -1]

		length = len(self.heap)
		height = math.log(length)
		i = h = 0

		if height == 0:
			self.heap[0] = ''
			return

		while h < height:
			while 2 * i + 2 < length:
				temp = self.heap[i]
				if self.heap[2 * i + 1] > self.heap[2 * i + 2]:
					if self.heap[2 * i + 1] > self.heap[i]:
						self.heap[i] = self.heap[2 * i + 1]
					else:
						self.heap[i] = temp
						break
					i = 2 * i + 1
				elif self.heap[2 * i + 2] > self.heap[2 * i + 1]:
					if self.heap[2 * i + 2] > self.heap[i]:
						self.heap[i] = self.heap[2 * i + 2]
					else:
						self.heap[i] = temp
						break
					i = 2 * i + 2
				self.heap[i] = temp
			h = h + 1

		if length % 2 == 0 and 2 * i + 1 < length:
			if self.heap[2 * i + 1] > self.heap[i]:
				self.heap[i] = self.heap[2 * i + 1]
				self.heap[2 * i + 1] = temp
			else:
				i = 2 * i + 1

	def sort(self):

		length = len(self.heap)
		height = math.log(length)
		i = h = 0
		sort_list = []
		for i in range(length):
			while h < height:
				while 2 * i + 2 < length:
					temp = self.heap[i]
					if self.heap[2 * i + 1] > self.heap[2 * i + 2]:
						self.heap[i] = self.heap[2 * i + 1]
						i = 2 * i + 1
					else:
						self.heap[i] = self.heap[2 * i + 2]
						i = 2 * i + 2

					self.heap[i] = temp

				h = h + 1

			if length % 2 == 0 and 2 * i + 1 < length:
				self.heap[i] = self.heap[2 * i + 1]
		
			max_node = self.heap[-1]
			sort_list.append(max_node)
			print(max_node)
			self.heap = self.heap[:-1]
		print(sort_list)
		
	def insert_nodes(self):
		nums = int(input("How many nodes do you need: "))
		for i in range(nums):
			data = int(input("Value of Node" + str(i + 1) +": "))
			self.insert(data)

	def delete_nodes(self):
		nums = int(input("How many nodes to delete: "))
		for i in range(nums):
			self.delete()

	def print_heap(self):
		print(self.heap)
		print("Length of Heap: " + str(len(self.heap)) + "\n")


new_heap = MaxHeap()
new_heap.insert_nodes()
new_heap.print_heap()

new_heap.delete_nodes()
new_heap.print_heap()
#new_heap.sort()