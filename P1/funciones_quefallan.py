	def eleccion_attack(self, num, jugador):
		correct_election = False
		cura = 0
		while (not correct_election):
			charac = input((type(self.personajes[num]).__name__+" (Player "+ str(jugador)+") .""What are you going to do?: "))
			if (charac == 'a' or charac == 's'):
				if (charac == 'a'):
					damage = self.personajes[num].get_damage()
					self.cooldown_reduction(num)
					correct_election = True
					damage = self.Procrastinator_passive(num, damage)
				elif (charac == 's'):
					if (self.personajes[num].special == 0):
						if (type(self.personajes[num]).__name__  == Bookworm):
							if(len(self.personajes) < self.players):
								correct_election = self.Bookworm_revive(num, correct_election)
							else:
								print("All players are alive. The skill can not used")
						elif (type(self.personajes[num]).__name__  == type(Worker).__name__):
							damage = self.Worker_special_attack(num)
							correct_election = True
						elif ((type(self.personajes[num]).__name__  == Procrastinator) and self.personajes[num].uso_habilidad == 1):
							damage = self.Procrastinator_special_attack(num)
							correct_election = True
						elif (type(self.personajes[num]).__name__  == Whatsapper):
							damage = 0
							cura = self.Whatsapper_heal(num)
							correct_election = True
		return damage, cura, charac

	def type_character(self, muerto):
		if (type(self.muertos[muerto]).__name__  == Bookworm):
			new_player = 1
		if (type(self.personajes[muerto]).__name__  == Worker):
			new_player = 2
		if (type(self.personajes[muerto]).__name__  == Procrastinator):
			new_player = 3
		if (type(self.personajes[muerto]).__name__  == Whatsapper):
			new_player = 4
		return new_player

		def add_dead_player(self, character):
			if (type(character).__name__ == Bookworm):
				self.muertos.append(Bookworm)
		elif (type(character).__name__ == Worker):
			self.muertos.append(Worker)
		elif (type(character).__name__ == Procrastinator): 
			self.muertos.append(Procrastinator)
		elif (type(character).__name__ == Whatsapper):
			self.muertos.append(Whatsapper) 

		def hit_all_enemies(self, num):
			damage = self.personajes[num].get_damage() + self.personajes[num].dmg + self.momment_stage
		for e in self.enemies :
			e.hp = self.quitar_vida(e.hp, damage)
			self.print_damage(num, e, damage)
			if (self.enemies[e].hp <= 0):
				print("ENEMIGO", type(self.enemies[e]).__name__, "ESTA MUERTISIMO")
				self.enemies.pop(e)
