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
	
	def __str__(self):
		pass

	def get_damage(self):
		return random.randrange(1, self.dmg + 1)
	
	def take_life(self, damage):
		self.hp = self.hp - damage


class Partial_exam(Enemies):
	def __init__(self):
		super().__init__(PARTIAL_HP, PARTIAL_DMG)

	def __str__(self):
		return ("			"+__class__.__name__+": Stats: " + str(self.hp) +"HP and "+ str(self.dmg)+"DMG")

class Final_exam(Enemies):
	def __init__(self):
		super().__init__(FINAL_HP, FINAL_DMG)

	def __str__(self):
		return ("			"+__class__.__name__+": Stats: " + str(self.hp) +"HP and "+ str(self.dmg)+"DMG")

class Theoretical_class(Enemies):
	def __init__(self):
		super().__init__(THEORICAL_HP, THEORICAL_DMG)

	def __str__(self):
		return ("			"+__class__.__name__+": Stats: " + str(self.hp) +"HP and "+ str(self.dmg)+"DMG")

class Teacher(Enemies):
	def __init__(self):
		super().__init__(TEACHER_HP, TEACHER_DMG)

	def __str__(self):
		return ("			"+__class__.__name__+": Stats: " + str(self.hp) +"HP and "+ str(self.dmg)+"DMG")
		
	def get_damage(self):
		damage = random.randrange(1, TEACHER_DMG + 1)
		if (damage == 7):
			damage = 14
		return damage
