#!/usr/bin/python3
import math

class MaxHeap:

	def __init__(self):
		self.heap = []

	def insert(self, data):
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

		if length % 2 == 0:
			self.heap[i] = self.heap[2 * i + 1]
			i = 2 * i + 1

		self.heap = self.heap[: -1]
		
	def print_heap(self):
		print(self.heap)
		print("Length of Heap: " + str(len(self.heap)) + "\n")


new_heap = MaxHeap()
new_heap.insert(25)
new_heap.insert(2)
new_heap.insert
new_heap.insert(13)
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
new_heap.delete()
new_heap.print_heap()