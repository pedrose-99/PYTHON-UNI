#Constantes de la vida y daño de los enemigos
PARTIAL_HP = 20
PARTIAL_DMG = 6
FINAL_HP = 40
FINAL_DMG = 12
THEORICAL_HP = 8
THEORICAL_DMG = 4
TEACHER_HP = 15
TEACHER_DMG = 7
class Enemies:
	def __init__(self, hp, dmg):
		self.hp = hp
		self.dmg = dmg


class Partial_exam(Enemies):
	def __init__(self, hp, dmg):
		super().__init__(hp, dmg)
		self.type = 1
		#self.ability = ability

class Final_exam(Enemies):
	def __init__(self, hp, dmg):
		super().__init__(hp, dmg)
		self.type = 2
		#self.ability = ability

class theoretical_class(Enemies):
	def __init__(self, hp, dmg):
		super().__init__(hp, dmg)
		#self.ability = ability
		self.type = 3

class Teacher(Enemies):
	def __init__(self, hp, dmg):
		super().__init__(hp, dmg)
		#self.ability = ability
		self.type = 4
