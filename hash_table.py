
class HashMap:

	def __init__(self, capacity):
		self.hashmap = [[] for bucket in range(capacity)]

	def get_hashkey(self, key):
		hashkey = hash(key) % len(self.hashmap)
		return hashkey

	def insert(self, key, value):
		bucket = self.hashmap[self.get_hashkey(key)]
		for i, kv in enumerate(bucket):
			k, v = kv
			if key == k:
				bucket[i] = ((key, value))
				break
		bucket.append((key, value))

	def retrieve(self, key):
		bucket = self.hashmap[self.get_hashkey(key)]
		for kv in bucket:
			k, v = kv
			if key == k:
				return v

		return "No value to be retrieved from this Key."

	def display_hashmap(self):
		print(self.hashmap)


capacity = int(input("Enter the capacity of the HashMap:"))
new_hashmap = HashMap(capacity)
new_hashmap.display_hashmap()

total = int(input("Enter the total elements to be added to the HashMap:"))
for i in range(total):
	key = int(input("Enter the key:"))
	value = input("Enter the value:")
	new_hashmap.insert(key, value)

print("\n")
new_hashmap.display_hashmap()
print("\n")

print(new_hashmap.retrieve('23'))
print(new_hashmap.retrieve('41'))
print(new_hashmap.retrieve('11'))
print(new_hashmap.retrieve('8'))