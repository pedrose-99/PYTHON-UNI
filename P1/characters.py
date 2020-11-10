import random
Bookworm_HP = 225
Bookworm_DMG = 9
Worker_HP = 40
Worker_DMG = 10
PROCRASTINSTOR_HP = 30
PROCRASTINSTOR_DMG = 6
Whatsapper_HP = 20
Whatsapper_DMG = 6
Bookworm_SPECIAL = 4
Worker_SPECIAL = 3
PROCRASTINSTOR_SPECIAL = 3
Whatsapper_SPECIAL = 3

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
	
	def take_life(self, damage):
		pass

class Bookworm(Characters):
	def __init__(self):
		super().__init__(Bookworm_HP, Bookworm_DMG, Bookworm_SPECIAL)
	
	def __str__(self):
		cadena = (__class__.__name__+": Stats: " + str(self.hp) +"HP and "+ str(self.dmg)+"DMG \n		Skill: Revives one player(4 rounds)\n")
		return cadena

	def get_damage(self):
		damage = random.randrange(1, Bookworm_DMG)
		return damage

	def take_life(self, damage):
		self.hp_real = self.hp_real - damage

class Worker(Characters):
	def __init__(self):
		super().__init__(Worker_HP, Worker_DMG, Worker_SPECIAL)
	
	def __str__(self):
		cadena = (__class__.__name__+": Stats: " + str(self.hp) +"HP and "+ str(self.dmg)+"DMG\n		Skill: 1.5 * (DMG + DMG roll) damage to one enemy (3 rounds)\n")
		return cadena
	
	def get_damage(self):
		damage = random.randrange(1, Worker_DMG)
		return damage

	def take_life(self, damage):
		self.hp_real = self.hp_real - damage

class Procrastinator(Characters):
	def __init__(self):
		super().__init__(PROCRASTINSTOR_HP,PROCRASTINSTOR_DMG, PROCRASTINSTOR_SPECIAL)
		self.uso_habilidad = 1

	def __str__(self):
		cadena = (__class__.__name__+": Stats: " + str(self.hp) +"HP and "+ str(self.dmg)+"DMG\n		Passive: Adds +1 DMG each round. Resets at the beginning of each level.\n		Skill: DMG + DMG roll + stage level to all the enemies after the third\n 		round of each stage and once per stage.\n")
		return cadena
	def get_damage(self):
		damage = random.randrange(1, PROCRASTINSTOR_DMG)
		return damage

	def take_life(self, damage):
		self.hp_real = self.hp_real - damage

class Whatsapper(Characters):
	def __init__(self):
		super().__init__(Whatsapper_HP, Whatsapper_DMG, Whatsapper_SPECIAL)
	
	def __str__(self):
		cadena = (__class__.__name__+": Stats: " + str(self.hp) +"HP and "+ str(self.dmg)+"DMG\n		Skill: Heals 2*DMG to one player (3 rounds)\n")
		return cadena

	def get_damage(self):
		damage = random.randrange(1, Whatsapper_DMG)
		return damage

	def take_life(self, damage):
		self.hp_real = self.hp_real - damage

