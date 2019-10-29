#Implementation of a stack using a LinkedList

class Node:

	def __init__(self, data):
		self.item = data
		self.ref = None

class Stack:

	def __init__(self):
		self.top = None

	def push(self, data):
		top_node = Node(data)
		top_node.ref = self.top
		self.top = top_node

	def add_elements_to_stack(self):
		nums = int(input("How many values do you want to stack up:"))
		if nums == 0:
			print("Wow!! What a waste of my use")
			return
		for i in range(nums):
			value = int(input("Enter the value to be pushed:"))
			self.push(value)

	def pop(self):
		if self.top == None:
			print("There are no items to pop from the stack.")
			return False
		print("popped out: " + str(self.top.item))
		self.top = self.top.ref

	def traverse_stack(self):
		n = self.top
		while n is not None:
			print(n.item)
			n = n.ref


new_stack = Stack()
new_stack.add_elements_to_stack()
new_stack.traverse_stack()

print("\n")

new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.traverse_stack()