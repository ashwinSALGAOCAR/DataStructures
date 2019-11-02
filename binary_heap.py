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

		'''We begin from the top node. The node with the heighest value and traverse down
		the height. We loop till we reach one less than the height. In the second loop we
		untill both child nodes exist. In this loop we move the top node down untill it is
		pushed to the end of the list and eliminated.

		If the node has only left child(even list length means it has only left child), we
		interchange the positions of the child and eliminate the parent.
		'''

		length = len(self.heap)
		height = math.log(length)
		i = h = 0
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
		
		self.heap = self.heap[: -1]
		
	def print_heap(self):
		print(self.heap)
		print("Length of Heap: " + str(len(self.heap)) + "\n")


new_heap = MaxHeap()
new_heap.insert(25)
new_heap.insert(2)
new_heap.insert(13)
new_heap.insert(34)
new_heap.insert(1)
new_heap.insert(47)
new_heap.insert(5)
new_heap.insert(88)
new_heap.insert(50)
new_heap.insert(100)
new_heap.insert(200)
new_heap.insert(150)

new_heap.print_heap()

new_heap.delete()
new_heap.delete()
new_heap.delete()
new_heap.delete()
new_heap.delete()

new_heap.print_heap()