class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
class DoublyLinkedList:  
	def __init__(self):
		self.start_node = None

	def insert_in_emptylist(self, data):
		if self.start_node is None:
			new_node = Node(data)
			self.start_node = new_node

	def insert_at_start(self, data):
		if self.start_node is None:
			new_node = Node(data)
			self.start_node = new_node
			print("node inserted")
			return
		new_node = Node(data)
		new_node.nref = self.start_node
		self.start_node.pref = new_node
		self.start_node = new_node
	
	def insert_at_end(self, data):
		if self.start_node is None:
			new_node = Node(data)
			self.start_node = new_node
			return
		n = self.start_node
		while n.nref is not None:
			n = n.nref
		new_node = Node(data)
		n.nref = new_node
		new_node.pref = n
	
	def insert_after_item(self, x, data):
		if self.start_node is None:
			print("List is empty")
			return
		else:
			n = self.start_node
			while n is not None:
				if n.data == x:
					break
				n = n.nref
			if n is None:
				print("item not in the list")
			else:
				new_node = Node(data)
				new_node.pref = n
				new_node.nref = n.nref
				if n.nref is not None:
					n.nref.prev = new_node
				n.nref = new_node

	def insert_before_item(self, x, data):
		if self.start_node is None:
			print("List is empty")
			return
		else:
			n = self.start_node
			while n is not None:
				if n.data == x:
					break
				n = n.nref
			if n is None:
				print("item not in the list")
			else:
				new_node = Node(data)
				new_node.nref = n
				new_node.pref = n.pref
				if n.pref is not None:
					n.pref.nref = new_node
				n.pref = new_node

	def traverse_list(self):
		if self.start_node is None:
			print("List has no element")
			return
		else:
			n = self.start_node
			while n is not None:
				print(n.data , " ")
				n = n.nref

	def delete_element_by_value(self, x):
		if self.start_node is None:
			print("The list has no element to delete")
			return 
		if self.start_node.nref is None:
			if self.start_node.item == x:
				self.start_node = None
			else:
				print("Item not found")
			return 
		if self.start_node.item == x:
			self.start_node = self.start_node.nref
			self.start_node.pref = None
			return
		n = self.start_node
		while n.nref is not None:
			if n.item == x:
				break;
			n = n.nref
		if n.nref is not None:
			n.pref.nref = n.nref
			n.nref.pref = n.pref
		else:
			if n.item == x:
				n.pref.nref = None
			else:
				print("Element not found")



sjshhshsj

	
	def insert_in_emptylist(self, data):
		if self.start == None:
			new_node = Node(data)
			self.start_node = new_node
			self.tail = new_node

	def insert_at_start(self, data):
		if self.start_node is None:
			new_node = Node(data)
			self.start_node = new_node
			print("node inserted")
			return
		new_node = Node(data)
		new_node.nref = self.start_node
		self.start_node.pref = new_node
		self.start_node = new_node
	
	def insert_at_end(self, data):
		if self.start_node is None:
			new_node = Node(data)
			self.start_node = new_node
			self.tail = new_node
			return
		n = self.start_node
		while n.nref is not None:
			n = n.nref
		new_node = Node(data)
		n.nref = new_node
		new_node.pref = n
	
	def insert_after_item(self, x, data):
		if self.start_node is None:
			print("List is empty")
			return
		else:
			n = self.start_node
			while n is not None:
				if n.data == x:
					break
				n = n.nref
			if n is None:
				print("item not in the list")
			else:
				new_node = Node(data)
				new_node.pref = n
				new_node.nref = n.nref
				if n.nref is not None:
					n.nref.prev = new_node
				n.nref = new_node

	def insert_before_item(self, x, data):
		if self.start_node is None:
			print("List is empty")
			return
		else:
			n = self.start_node
			while n is not None:
				if n.data == x:
					break
				n = n.nref
			if n is None:
				print("item not in the list")
			else:
				new_node = Node(data)
				new_node.nref = n
				new_node.pref = n.pref
				if n.pref is not None:
					n.pref.nref = new_node
				n.pref = new_node

	def traverse_list(self):
		if self.start_node is None:
			print("List has no element")
			return
		else:
			n = self.start_node
			while n is not None:
				print(n.data , " ")
				n = n.nref

	def delete_element_by_value(self, x):
		if self.start_node is None:
			print("The list has no element to delete")
			return 
		if self.start_node.nref is None:
			if self.start_node.item == x:
				self.start_node = None
			else:
				print("Item not found")
			return 
		if self.start_node.item == x:
			self.start_node = self.start_node.nref
			self.start_node.pref = None
			return
		n = self.start_node
		while n.nref is not None:
			if n.item == x:
				break;
			n = n.nref
		if n.nref is not None:
			n.pref.nref = n.nref
			n.nref.pref = n.pref
		else:
			if n.item == x:
				n.pref.nref = None
			else:
				print("Element not found")




	def delete_node(self, data):
		prev = self.head
		current = self.head
		k = 0
		n_games = 0
		game = self.head
		while game != None:
			n_games +=1
			game = game.next
		if pos == 0:
			self.delete_first()
		elif pos == (n_games - 1):
			self.delete_last()
		elif pos > 0:
			while k != pos and current.next != None:
				prev = current
				current = current.next
				k+=1
			if k == pos:
				temporal = current.next
				prev.next = current.next
				temporal.prev = prev