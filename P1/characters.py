BOOKWORM_HP = 25
BOOKWORM_DMG = 9
WORKER_HP = 40
WORKER_DMG = 10
PROCRASTINSTOR_HP = 30
PROCRASTINSTOR_DMG = 6
WHATSAPPER_HP = 20
WHATSAPPER_DMG = 6

class Characters:
	def __init__(self, hp, dmg):
		self.hp = hp
		self.dmg = dmg
		self.hpactual = hp
	#	self.hability = ability
		self.vida = True

class bookworm(Characters):
	def __init__(self, hp, dmg):
		super().__init__(hp, dmg)
		#self.hability = bookworm_ability

class worker(Characters):
	def __init__(self, hp, dmg):
		super().__init__(hp, dmg)
		#self.hability = worker_ability

class procrastinator(Characters):
	def __init__(self, hp, dmg):
		super().__init__(hp, dmg)
	#	self.hability = ability

class whatsapper(Characters):
	def __init__(self, hp, dmg):
		super().__init__(hp, dmg)
	#	self.hability = ability




