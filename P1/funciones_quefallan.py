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
					damage = self.procrastinator_passive(num, damage)
				elif (charac == 's'):
					if (self.personajes[num].special == 0):
						if (type(self.personajes[num]).__name__  == bookworm):
							if(len(self.personajes) < self.players):
								correct_election = self.bookworm_revive(num, correct_election)
							else:
								print("All players are alive. The skill can not used")
						elif (type(self.personajes[num]).__name__  == type(worker).__name__):
							damage = self.worker_special_attack(num)
							correct_election = True
						elif ((type(self.personajes[num]).__name__  == procrastinator) and self.personajes[num].uso_habilidad == 1):
							damage = self.procrastinator_special_attack(num)
							correct_election = True
						elif (type(self.personajes[num]).__name__  == whatsapper):
							damage = 0
							cura = self.whatsapper_heal(num)
							correct_election = True
		return damage, cura, charac

	def type_character(self, muerto):
		if (type(self.muertos[muerto]).__name__  == bookworm):
			new_player = 1
		if (type(self.personajes[muerto]).__name__  == worker):
			new_player = 2
		if (type(self.personajes[muerto]).__name__  == procrastinator):
			new_player = 3
		if (type(self.personajes[muerto]).__name__  == whatsapper):
			new_player = 4
		return new_player

		def add_dead_player(self, character):
			if (type(character).__name__ == bookworm):
			self.muertos.append(bookworm)
		elif (type(character).__name__ == worker):
			self.muertos.append(worker)
		elif (type(character).__name__ == procrastinator): 
			self.muertos.append(procrastinator)
		elif (type(character).__name__ == whatsapper):
			self.muertos.append(whatsapper) 

		def hit_all_enemies(self, num):
			damage = self.personajes[num].get_damage() + self.personajes[num].dmg + self.momment_stage
		for e in self.enemies :
			e.hp = self.quitar_vida(e.hp, damage)
			self.print_damage(num, e, damage)
			if (self.enemies[e].hp <= 0):
				print("ENEMIGO", type(self.enemies[e]).__name__, "ESTA MUERTISIMO")
				self.enemies.pop(e)
