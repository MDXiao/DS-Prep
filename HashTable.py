# When would you use a hashtable?
# Problems that deal with...

#LIST


class HashTable:

	def __init__(self, h_size):
		self.hash_table = [[] for _ in range(h_size)]
		self.table_size = h_size-1

	# Always create a hash where it is modded by m-1
	def hash_key(self, val):
		return (val % self.table_size)

	def insert_key(self, hash_val, val):
		key = self.hash_key(hash_val)
		self.hash_table[key].append(val)

	## Complexity of searching and getting is O(1)
	def get_val(self, hash_val, val):


	def display_table(self):
		for key in range(self.table_size+1):
			print(key, end=" ")
			for val in self.hash_table[key]:
				print("-->", end=" ")
				print(val, end=" ")
			print()


if __name__ == "__main__":
	my_table = HashTable(10)

	my_table.insert_key(25, "TestHello")
	my_table.insert_key(12, "AnotherTest")

	my_table.display_table()