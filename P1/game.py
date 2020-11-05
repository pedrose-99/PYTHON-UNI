from characters import bookworm, worker, procrastinator, whatsapper, Characters
from enemies import Teacher, Final_exam, Partial_exam, theoretical_class
import random

BOOKWORM_SPECIAL = 4
WORKER_SPECIAL = 3
PROCRASTINSTOR_SPECIAL = 3
WHATSAPPER_SPECIAL = 3

class Game:
	def __init__(self, players, stages):
		self.personajes = []
		self.enemies = []
		self.muertos = []
		self.rondas = 0
		self.players = players
		self.monsters = 3
		self.stages = stages
		self.momment_stage = 0


	def print_characters(self):
		print("***********		 AVAILABLE CHARACTERS		 ***********\n")
		print("1.- The bookworn -> Stats: 25HP and 9DMG\n")
		print("		Skill: Revives one player(4 rounds)\n")
		print("2.- The worker -> Stats: 40HP and 10DMG\n")
		print("		Skill: 1.5 * (DMG + DMG roll) damage to one enemy (3 rounds)\n")
		print("3.- The whatsapper -> Stats: 20HP and 6DMG\n")
		print("		Skill: Heals 2*DMG to one player (3 rounds)\n")
		print("4.- The procrastinator-> Stats: 30HP and 6DMG\n")
		print("		Passive: Adds +1 DMG each round. Resets at the beginning of each level.\n")
		print("		Skill: DMG + DMG roll + stage level to all the enemies\n after the third round of each stage and once per stage.\n")
		print("********************************************************\n")
	
	def print_actual_stage(self):
		print("********************************************************")
		print("				************************					")
		print("				*        STAGE", self.momment_stage,"      *	")
		print("				************************					")
		print("				---- CURRENT MONSTERS ----			")
		print("		 	  ++++++++++++++++++++++++++++++++++++++		")

	def print_players_turn(self):
		print("		")
		print("				 ------------------------")
		print("				 -     PLAYERS TURN     -")
		print("				 ------------------------")
		print("		")

	def print_monster_turn(self):
		print("		")
		print("				 ------------------------")
		print("				 -     MONSTER TURN     -")
		print("				 ------------------------")
		print("		")

	
	def add_player(self, eleccion):
		if (eleccion == 1):
			self.personajes.append(bookworm)
		elif (eleccion == 2):
			self.personajes.append(worker)
		elif (eleccion == 3): 
			self.personajes.append(procrastinator)
		elif (eleccion == 4):
			self.personajes.append(whatsapper)

	def add_enemies(self):
		num = 0
		while (num < self.monsters):
			enemie = random.randrange(1, 4)
			if (enemie == 1):
				self.enemies.append(Partial_exam)
			elif (enemie == 2 and self.momment_stage >= 4):
				self.enemies.append(Final_exam)
			elif (enemie == 3):
				self.enemies.append(theoretical_class)
			elif (enemie == 4):
				self.enemies.append(Teacher)
			num = num + 1
		return self.enemies

	def add_dead_player(self, character):
		if (type(character).__name__ == characters.bookworm):
			self.muertos.append(bookworm)
		elif (type(character).__name__ == characters.worker):
			self.muertos.append(worker)
		elif (type(character).__name__ == characters.procrastinator): 
			self.muertos.append(procrastinator)
		elif (type(character).__name__ == characters.whatsapper):
			self.muertos.append(whatsapper) 

	
	def eleccion_Character(self, num):
		correct_election = False
		while (not correct_election):
			charac = input(("Player", num, ". Please, choose a character (1-4):"))
			charac = int(charac)
			if (charac >= 1 and charac <= 4):
				print(charac,"\n")
				correct_election = True
				return charac

	def couldown_reduction(self, num):
		if (self.personajes[num].special > 0):
			self.personajes[num].special = self.personajes[num].special - 1
	
	def procrastinator_passive(self, num):
		if (type(self.personajes[num]).__name__ == characters.procrastinator):
			damage = damage + self.rondas
		return damage

	def type_character(self, muerto):
		if (type(self.muertos[muerto]).__name__  == characters.bookworm):
			new_player = 1
		if (type(self.personajes[num]).__name__  == characters.worker):
			new_player = 2
		if (type(self.personajes[num]).__name__  == characters.procrastinator):
			new_player = 3
		if (type(self.personajes[num]).__name__  == characters.whatsapper):
			new_player = 4
		return new_player

	def bookworm_revive(self, num, correct_election):
		correct_option = False
		while (not correct_option):
			election = input("which character do you want to revive: ")
			election = int(election)
			if (election >= 1 and election <= (len(self.muertos))):
				election = election - 1
				muerto = (type(self.muertos[election]).__name__)
				new_player = self.type_character(muerto)
				self.add_player(new_player)
				selfpersonajes[num].special = BOOKWORM_SPECIAL
				damage = 0
				cura = 0
				correct_option = True
		correct_election = correct_option
		return (correct_election)

	def worker_special_attack(self, num):
		damage = random.randrange(1, self.personajes[num].dmg)
		damage = (damage + self.personajes[num].dmg) * 1.5
		self.personajes[num].special = WORKER_SPECIAL
		return damage

	def procrastinator_special_attack(self, num):
		damage = random.randrange(1, self.personajes[num].dmg)
		damage = damage + self.personajes[num].dmg + self.momment_stage
		self.personajes[num].special = PROCRASTINSTOR_SPECIAL
		self.personajes[num].uso_habilidad = 0
		return damage

	def whatsapper_heal(self, num):
		cura = self.personajes[num].dmg * 2
		self.personajes[num].special = WHATSAPPER_SPECIAL
		return cura

	def eleccion_attack(self, num, jugador):
		correct_election = False
		cura = 0
		while (not correct_election):
			charac = input((type(selfpersonajes[num]).__name__+"Player"+ str(jugador)+".""What are you going to do?: "))
			if (charac == 'a' or charac == 's'):
				if (charac == 'a'):
					damage = self.personajes[num].get_damage()
					self.couldown_reduction(num)
					correct_election = True
					damage = self.procrastinator_passive(num)
				elif (charac == 's'):
					if (self.personajes[num].special == 0):
						if (type(self.personajes[num]).__name__  == characters.bookworm):
							if(len(self.characters) < self.players):
								correct_eleption = self.bookworm_revive(num)
							else:
								print("All players are alive. The skill can not used")
						elif (type(self.personajes[num]).__name__  == characters.worker):
							damage = self.worker_special_attack(num)
							correct_election = True
						elif ((type(self.personajes[num]).__name__  == characters.procrastinator) and self.personajes[num].uso_habilidad == 1):
							damage = self.procrastinator_special_attack(num)
							correct_election = True
						elif (type(self.personajes[num]).__name__  == characters.whatsapper):
							damage = 0
							cura = self.whatsapper_heal(num)
							correct_election = True
		return damage, cura, charac

	def reset_stats(self):
		num = 0
		while (num < len(self.personajes)):
			if (type(self.personajes[num]).__name__ == Characters.procrastinator):
				self.personajes[num].special = PROCRASTINSTOR_SPECIAL
				self.personajes[num].uso_habilidad = 1
			else:
				self.personajes[num].special = 3
			self.personajes[num].hp_real = self.personajes[num].hp_real + self.personajes[num].hp/4
			if (self.personajes[num].hp_real > self.personajes[num].hp):
				self.personajes[num].hp_real = self.personajes[num].hp
			num = num + 1
		self.rondas = 1

	def quitar_vida(self, hp, damage):
		hp = hp - damage
		return hp
	
	def print_monsters(self):
		for e in self.enemies:
      		print(self.enemies[e].get_stats())

	def print_damage(self, num, enemy):
		print(type(self.personajes[num]).__name__,"did", damage,"damage to ", type(self.enemies[e]).__name__,".", type(self.enemies[e]).__name__, "has", self.enemies[e].hp,"hp left.")
	
	def hit_all_enemies(self, num, damage):
		for e in self.enemies :
			self.enemies[e].hp = self.quitar_vida(self.enemies[e].hp, damage)
			self.print_damage(num, e)
			if (self.enemies[e].hp <= 0):
				print("ENEMIGO", type(self.enemies[e]).__name__, "ESTA MUERTISIMO")
					self.enemies.pop(e)

	def hit_an_enemy(self, num, damage):
		enemy_random =random.randrange(0, len(self.enemies))
		self.enemies[enemy_random].hp = self.quitar_vida(self.enemies[enemy_random].hp, damage)
		self.print_damage(num, enemy_random)
			if (self.enemies[enemy_random].hp <= 0):
				print("ENEMIGO", type(self.enemies[enemy_random]).__name__, "ESTA MUERTISIMO")
				self.enemies.pop(enemy_random)
	
	def choose_heal(self):
		correct_heal = False
		while (not correct_heal):
			random_charac = input("Which character do you want to heal: ")
			random_charac = int(random_charac)
			if (random_charac > len(self.players)):
				print("Incorrect value")
			elif (self.personajes[random_charac].hp_real < self.personajes[random_charac].hp):
				correct_heal = True
				self.personajes[random_charac].hp_real = self.personajes[random_charac].hp_real + cura
					if (self.personajes[random_charac].hp_real > self.personajes[random_charac].hp):
						self.personajes[random_charac].hp_real = self.personajes[random_charac].hp
						print(type(self.personajes[random_charac]).__name__, "has been completely restored. Hp =", self.personajes[random_charac].hp_real)
					else:
						print(type(self.personajes[random_charac]).__name__, "has",self.personajes[random_charac].hp_real,"of",self.personajes[random_charac].hp, "hp ")
			else:
				print(type(self.personajes[random_charac]).__name__ ,"can not be heal" )	

	def players_turn(self):
		Finish_turn = False
		self.print_players_turn()
		jugador = 1
		num = 0
		while ((num < len(self.players) and not Finish_turn):
			print(type(self.personajes[num]).__name__+"Player"+ str(jugador)+". ")
			damage, cura, charac = self.eleccion_attack(num, jugador)
			if (charac == 's' and type(self.personajes[num]).__name__ == Characters.procrastinator)):
				self.hit_all_enemies(num, damage)
			elif (damage > 0):
				self.hit_an_enemy(num, samage)
			elif (damage == 0 and cura == 0):
				print("El jugador ha sido revivido")
			else:
				self.choose_heal()
			num = num + 1
			jugador = jugador + 1

	def enemies_turn(self):
		finish_turn = False
		self.print_monster_turn()
		while (num < len(self.enemies) and not finish_turn):
			random_charac = random.randrange(0, len(self.personajes))
			damage = self.enemies[num].get_damage()
			self.personajes[random_charac].hp_real = self.quitar_vida(self.personajes[random_charac].hp_real, damage)
			print(type(self.enemies[num]).__name__,"did", damage,"damage to ", type(self.personajes[random_charac]).__name__,".", type(self.personajes[random_charac]).__name__, "has", self.personajes[random_charac].hp_real,"hp left.")
			num = num + 1
			if (self.personajes[random_charac].hp_real <= 0):
				print("EL PERSONAJE", type(self.personajes[random_charac]).__name__, "NECESITA QUE LE REVIVAN")
				self.add_dead_player(self.personajes[random_charac])
				self.personajes.pop(random_charac)

	def print_characters(self, game, num):
		if (game.personajes[num].type == 1):
			print(num + 1,".- The bookworn -> Stats: 25HP and 9DMG")
			print("		Skill: Revives one player(4 rounds)")
		elif (game.personajes[num].type == 2):
			print(num + 1," .- The worker -> Stats: 40HP and 10DMG")
			print("		Skill: 1.5 * (DMG + DMG roll) damage to one enemy (3 rounds)")
		elif (game.personajes[num].type == 3):
			print(num + 1,".- The whatsapper -> Stats: 20HP and 6DMG")
			print("		Skill: Heals 2*DMG to one player (3 rounds)")
		elif (game.personajes[num].type == 4):
			print(num + 1,".- The procrastinator-> Stats: 30HP and 6DMG")
			print("		Passive: Adds +1 DMG each round. Resets at the beginning of each level.")
			print("		Skill: DMG + DMG roll + stage level to all the enemies")
			print("after the third round of each stage and once per stage.")

	def update_stage(self):
		self.momment_stage = self.momment_stage + 1
		self.print_actual_stage()
		self.reset_stats()
		self.enemies = self.add_enemies()

	def fight(self):
		finish_fight = False
		self.print_actual_stage()
		self.print_monsters()
		while (not finish_fight):
			self.players_turn()
			self.monsters_turn()
			if (len(self.enemies) == 0):
				dead_monsters = True
			if (len(self.personajes) == 0):
				dead_players = True
		return dead_players