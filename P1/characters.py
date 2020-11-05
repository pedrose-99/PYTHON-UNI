import random
BOOKWORM_HP = 25
BOOKWORM_DMG = 9
WORKER_HP = 40
WORKER_DMG = 10
PROCRASTINSTOR_HP = 30
PROCRASTINSTOR_DMG = 6
WHATSAPPER_HP = 20
WHATSAPPER_DMG = 6

class Characters:
	def __init__(self, hp, dmg, special):
		self.hp = hp
		self.dmg = dmg
		self.hp_real = hp
		self.special = special
	
	def get_stats(self):
		pass

	def get_damage(self):
		pass

class bookworm(Characters):
	def __init__(self, special):
		super().__init__(BOOKWORM_HP, BOOKWORM_DMG, special)
	
	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)
	
	def get_damage(self):
		damage = random.randrange(1, BOOKWORM_DMG)
		return damage

class worker(Characters):
	def __init__(self, special):
		super().__init__(WORKER_HP, WORKER_DMG, special)
	
	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)
	
	def get_damage(self):
		damage = random.randrange(1, WORKER_DMG)
		return damage

class procrastinator(Characters):
	def __init__(self, special):
		super().__init__(PROCRASTINSTOR_HP,PROCRASTINSTOR_DMG, special)
		self.uso_habilidad = 1

	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)

	def get_damage(self):
		damage = random.randrange(1, PROCRASTINSTOR_DMG)
		return damage

class whatsapper(Characters):
	def __init__(self, special):
		super().__init__(WHATSAPPER_HP, WHATSAPPER_DMG, special)
	
	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)

	def get_damage(self):
		damage = random.randrange(1, WHATSAPPER_DMG)
		return damage

