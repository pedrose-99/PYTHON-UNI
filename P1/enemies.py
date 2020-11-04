class Enemies:
	def __init__(self, hp, dmg):
		self.hp = hp
		self.dmg = dmg


class Partial_exam(Enemies):
	def __init__(self, hp, dmg):
		super().__init__(hp, dmg)
		#self.ability = ability

class Final_exam(Enemies):
	def __init__(self, hp, dmg):
		super().__init__(hp, dmg)
		#self.ability = ability

class theoretical_class(Enemies):
	def __init__(self, hp, dmg):
		super().__init__(hp, dmg)
		#self.ability = ability

class Teacher(Enemies):
	def __init__(self, hp, dmg):
		super().__init__(hp, dmg)
		#self.ability = ability

