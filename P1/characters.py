class Characters:
	def __init__(self, hp, dmg):
		self.hp = hp
		self.dmg = dmg
		self.hp_actual = hp
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




