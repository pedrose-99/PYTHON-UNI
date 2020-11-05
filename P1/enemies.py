import random
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
	
	def get_stats(self):
		pass

	def get_damage(self):
		pass


class Partial_exam(Enemies):
	def __init__(self):
		super().__init__(PARTIAL_HP, PARTIAL_DMG)

	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)
	
	def get_damage(self):
		damage = random.randrange(1, PARTIAL_DMG)
		return damage

# type(class.__name__)

class Final_exam(Enemies):
	def __init__(self):
		super().__init__(FINAL_HP, FINAL_DMG)

	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)

	def get_damage(self):
		damage = random.randrange(1, FINAL_DMG)
		return damage

class theoretical_class(Enemies):
	def __init__(self):
		super().__init__(THEORICAL_HP, THEORICAL_DMG)
	
	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)

	def get_damage(self):
		damage = random.randrange(1, THEORICAL_DMG)
		return damage

class Teacher(Enemies):
	def __init__(self):
		super().__init__(TEACHER_HP, TEACHER_DMG)

	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)

	def get_damage(self):
		damage = random.randrange(1, TEACHER_DMG)
		if (damage == 7):
			damage = 14
		return damage