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
	def __init__(self, hp, dmg, ability):
		super().__init__(self, PARTIAL_HP, PARTIAL_DMG)
		self.hability = hability

class Final_exam(Enemies):
	def __init__(self, hp, dmg, ability):
		super().__init__(self, FINAL_HP, FINAL_DMG)
		self.hability = hability

class theoretical_class(Enemies):
	def __init__(self, hp, dmg, ability):
		super().__init__(self, THEORICAL_HP, THEORICAL_DMG)
		self.hability = hability

class Teacher(Enemies):
	def __init__(self, hp, dmg, ability):
		super().__init__(self, TEACHER_HP, TEACHER_DMG)
		self.hability = hability

