class Stack:
	"""docstring for Stack
	通过列表实现堆栈

	"""
	def __init__(self):
		self.items = []
	def push(self,item):
		self.items.append(item)
	def isEmpty(self):
		return len(self.items) == 0
	def pop(self):
		return self.items.remove() if not self.isEmpty() else -1
	def top(self):
		return self.items[len(self.items)-1]
		