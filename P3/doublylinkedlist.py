class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:  
	def __init__(self):
		self.__head = None
		self.__tail = None

	def is_empty(self):
		return self.__head == None

	def get_head(self):
		return self.__head
	
	def get_last(self):
		return self.__tail

	def insert_first(self, dato):
		temporal = Node(dato)
		if self.is_empty():
			self.__head = temporal
			self.__tail = temporal
		else:
			temporal.next = self.__head
			self.__head.prev = temporal
			self.__head = temporal

	def insert_last(self, dato):
		temporal = Node(dato)
		if self.is_empty():
			self.__head = temporal
			self.__tail = temporal
		else:
			temporal.prev = self.__tail
			self.__tail.next = temporal
			self.__tail = temporal

	def delete_first(self):
		if self.__head.next == None:
			self.__head = None
			self.__tail = None
		else:
			self.__head = self.__head.next
			self.__head.prev = None

	def delete_last(self):
		if self.__tail.prev == None:
			self.__head = None
			self.__tail = None
		else:
			self.__tail = self.__tail.prev 
			self.__tail.next = None

	def delete_node(self, data):
		prev = self.__head
		current = self.__head
		if self.__head.data == data:
			self.delete_first()
		elif self.__tail.data == data:
			self.delete_last()
		else:
			while current.data != data and current.next != None:
				prev = current
				current = current.next
			if current.data == data:
				temporal = current.next
				prev.next = current.next
				temporal.prev = prev

class Cursor:
	def __init__(self, iterable):
		self.iterable = iterable
		self.pointer = None
	
	def first(self):
		self.pointer = self.iterable.get_head()
	
	def last(self):
		self.pointer = self.iterable.get_last()

	def next(self):
		if self.pointer is None:
			self.pointer = None
		else:
			self.pointer = self.pointer.next
	
	def prev(self):
		if self.pointer is None:
			self.pointer = None
		else:
			self.pointer = self.pointer.prev

	def empty(self):
		return self.pointer

	def get(self):
		return self.pointer.data