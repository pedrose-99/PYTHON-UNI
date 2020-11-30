import random
BOOKWORM_HP = 25
BOOKWORM_DMG = 9
WORKER_HP = 40
WORKER_DMG = 10
PROCRASTINSTOR_HP = 30
PROCRASTINSTOR_DMG = 6
WHATSAPPER_HP = 20
WHATSAPPER_DMG = 6
BOOKWORM_SPECIAL = 4
WORKER_SPECIAL = 3
PROCRASTINSTOR_SPECIAL = 3
WHATSAPPER_SPECIAL = 3

class Characters:
	def __init__(self, hp, dmg, special):
		self.hp = hp
		self.dmg = dmg
		self.hp_real = hp
		self.special = special
	
	def __str__(self):
		pass

	def get_damage(self):
		return random.randrange(1, self.dmg + 1)
	
	def take_life(self, damage):
		self.hp_real = self.hp_real - damage

class Bookworm(Characters):
	def __init__(self):
		super().__init__(BOOKWORM_HP, BOOKWORM_DMG, BOOKWORM_SPECIAL)
	
	def __str__(self):
		return (__class__.__name__+": Stats: " + str(self.hp) +"HP and "+ str(self.dmg)+"DMG \n		Skill: Revives one player(4 rounds)\n")

class Worker(Characters):
	def __init__(self):
		super().__init__(WORKER_HP, WORKER_DMG, WORKER_SPECIAL)
	
	def __str__(self):
		return (__class__.__name__+": Stats: " + str(self.hp) +"HP and "+ str(self.dmg)+"DMG\n		Skill: 1.5 * (DMG + DMG roll) damage to one enemy (3 rounds)\n")

class Procrastinator(Characters):
	def __init__(self):
		super().__init__(PROCRASTINSTOR_HP,PROCRASTINSTOR_DMG, PROCRASTINSTOR_SPECIAL)
		self.uso_habilidad = 1

	def __str__(self):
		return (__class__.__name__+": Stats: " + str(self.hp) +"HP and "+ str(self.dmg)+"DMG\n		Passive: Adds +1 DMG each round. Resets at the beginning of each level.\n		Skill: DMG + DMG roll + stage level to all the enemies after the third\n 		round of each stage and once per stage.\n")

class Whatsapper(Characters):
	def __init__(self):
		super().__init__(WHATSAPPER_HP, WHATSAPPER_DMG, WHATSAPPER_SPECIAL)
	
	def __str__(self):
		return (__class__.__name__+": Stats: " + str(self.hp) +"HP and "+ str(self.dmg)+"DMG\n		Skill: Heals 2*DMG to one player (3 rounds)\n")


