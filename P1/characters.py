class Characters:
	def __init__(self, hp, dmg, special):
		self.hp = hp
		self.dmg = dmg
		self.hp_actual = hp
	#	self.hability = ability
		self.vida = True
		self.special = special

class bookworm(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(hp, dmg, special)
		self.type = 1
		#self.hability = bookworm_ability

class worker(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(hp, dmg, special)
		self.type = 2
		#self.hability = worker_ability

class procrastinator(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(hp, dmg, special)
		self.type = 3
		self.uso_habilidad = 1
	#	self.hability = ability

class whatsapper(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(hp, dmg, special)
		self.type = 4
	#	self.hability = ability




