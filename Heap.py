import heapq

# Visualize how a heap works
# What is the complexity of inserting and popping a heap?

# What is a heap best used for?
# Questions take deal with trying to find the top K elements

# Use whenever you need quick access to the largest or smallest items

if __name__ == "__main__":
	test_list = [6,1,2,3,7,5,4,8]
	heapq.heapify(test_list)
	print(test_list)