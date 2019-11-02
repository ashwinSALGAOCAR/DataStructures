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

	def print_heap(self):
		print(self.heap)


new_heap = MaxHeap()
new_heap.insert(25)
new_heap.insert(2)
new_heap.insert(13)
new_heap.insert(47)
new_heap.insert(5)
new_heap.insert(50)
new_heap.insert(100)
new_heap.insert(200)
new_heap.insert(150)

new_heap.print_heap()