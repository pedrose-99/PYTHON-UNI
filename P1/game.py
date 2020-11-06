from characters import bookworm, worker, procrastinator, whatsapper
from enemies import Teacher, Final_exam, Partial_exam, theoretical_class
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

PARTIAL_HP = 20
PARTIAL_DMG = 6
FINAL_HP = 40
FINAL_DMG = 12
THEORICAL_HP = 8
THEORICAL_DMG = 4
TEACHER_HP = 15
TEACHER_DMG = 7

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


	def print_all_characters(self):
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
			self.personajes.append(bookworm(BOOKWORM_HP, BOOKWORM_DMG, BOOKWORM_SPECIAL))
		elif (eleccion == 2):
			self.personajes.append(worker(WORKER_HP, WHATSAPPER_DMG, WHATSAPPER_SPECIAL))
		elif (eleccion == 3): 
			self.personajes.append(procrastinator(PROCRASTINSTOR_HP, PROCRASTINSTOR_DMG, PROCRASTINSTOR_SPECIAL))
		elif (eleccion == 4):
			self.personajes.append(whatsapper(WHATSAPPER_HP, WHATSAPPER_DMG, WHATSAPPER_SPECIAL))

	def add_enemies(self):
		num = 0
		while (num < self.monsters):
			enemy = random.randrange(1, 4)
			if (enemy == 1):
				self.enemies.append(Partial_exam(PARTIAL_HP, PARTIAL_DMG))
				num = num + 1
			elif (enemy == 2 and self.momment_stage >= 4):
				self.enemies.append(Final_exam(FINAL_HP, FINAL_DMG))
				num = num + 1
			elif (enemy == 3):
				self.enemies.append(theoretical_class(FINAL_HP, FINAL_DMG))
				num = num + 1
			elif (enemy == 4):
				self.enemies.append(Teacher(TEACHER_HP, TEACHER_DMG))
				num = num + 1
		return self.enemies
#mirar pq no furula bien
	def add_dead_player(self, character):
		if (character == bookworm):
			self.muertos.append(bookworm)
		elif (character == worker):
			self.muertos.append(worker)
		elif (character == procrastinator): 
			self.muertos.append(procrastinator)
		elif (character == whatsapper):
			self.muertos.append(whatsapper) 

	
	def cooldown_reduction(self, num):
		if (self.personajes[num].special > 0):
			self.personajes[num].special = self.personajes[num].special - 1
#mirar xq no me identifica el name procrastinator
	def procrastinator_passive(self, num, damage):
		if (self.personajes[num] == procrastinator):
			damage = damage + self.rondas
		return damage
#Mirar porque no me identifica el name de bookworm
	def type_character(self, muerto):
		if (muerto  == bookworm):
			new_player = 1
		elif (muerto  == worker):
			new_player = 2
		elif (muerto  == procrastinator):
			new_player = 3
		elif (muerto  == whatsapper):
			new_player = 4
		return new_player

	def bookworm_revive(self, num):
		correct_option = False
		damage = 0
		while (not correct_option):
			election = input("which character do you want to revive: ")
			election = int(election)
			if (election >= 1 and election <= (len(self.muertos))):
				election = election - 1
				muerto = self.muertos[election]
				print(muerto)
				new_player = self.type_character(muerto)
				self.add_player(new_player)
				self.personajes[num].special = BOOKWORM_SPECIAL
				correct_option = True
		return damage

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

#Comprobar tambien esta 
	def reset_stats(self):
		num = 0
		while (num < len(self.personajes)):
			if (self.personajes[num] == bookworm):
				self.personajes[num].special = BOOKWORM_SPECIAL
			elif (self.personajes[num] == procrastinator):
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
		#for e in self.enemies:
        	#print(e.get_stats())
		print("pintar monstruos")


	def print_damage(self, num, enemy, damage):
		print(type(self.personajes[num]).__name__,"did", damage,"damage to ", type(self.enemies[enemy]).__name__,".", type(self.enemies[enemy]).__name__, "has", self.enemies[enemy].hp,"hp left.")
	
	def hit_all_enemies(self, num, damage):
		enemy_random = 0
		while (enemy_random < len(self.enemies)):
			self.enemies[enemy_random].hp = self.quitar_vida(self.enemies[enemy_random].hp, damage)
			self.print_damage(num, enemy_random, damage)	
			if (self.enemies[enemy_random].hp <= 0):
				print("ENEMIGO", type(self.enemies[enemy_random]).__name__, "ESTA MUERTISIMO")
				self.enemies.pop(enemy_random)
			else:
				enemy_random = enemy_random + 1

	def hit_an_enemy(self, num, damage):
		enemy_random =random.randrange(0, len(self.enemies))
		self.enemies[enemy_random].hp = self.quitar_vida(self.enemies[enemy_random].hp, damage)
		self.print_damage(num, enemy_random, damage)
		if (self.enemies[enemy_random].hp <= 0):
			print("ENEMIGO", type(self.enemies[enemy_random]).__name__, "ESTA MUERTISIMO")
			self.enemies.pop(enemy_random)
	
	def choose_heal(self, cura):
		correct_heal = False
		while (not correct_heal):
			random_charac = input("Which character do you want to heal: ")
			random_charac = int(random_charac)
			if (random_charac > len(self.personajes) or random_charac < 0):
				print("Incorrect value")
			elif (self.personajes[random_charac - 1].hp_real < self.personajes[random_charac - 1].hp):
				correct_heal = True
				self.personajes[random_charac - 1].hp_real = self.personajes[random_charac - 1].hp_real + cura
				if (self.personajes[random_charac - 1].hp_real > self.personajes[random_charac - 1].hp):
					self.personajes[random_charac - 1].hp_real = self.personajes[random_charac - 1].hp
					print(type(self.personajes[random_charac - 1]).__name__, "has been completely restored. Hp =", self.personajes[random_charac - 1].hp_real)
				else:
					print(type(self.personajes[random_charac - 1]).__name__, "has",self.personajes[random_charac - 1].hp_real,"of",self.personajes[random_charac - 1].hp, "hp ")
			else:
				print(type(self.personajes[random_charac - 1]).__name__ ,"can not be heal" )	

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
						if (type(self.personajes[num]).__name__  == "bookworm"):
							if(len(self.personajes) < self.players):
								damage = self.bookworm_revive(num)
								correct_election = True
							else:
								print("All players are alive. The skill can not used")
						elif (type(self.personajes[num]).__name__  == "worker"):
							damage = self.worker_special_attack(num)
							correct_election = True
						elif ((type(self.personajes[num]).__name__  == "procrastinator") and (self.personajes[num].uso_habilidad == 1)):
							damage = self.procrastinator_special_attack(num)
							correct_election = True
						elif (type(self.personajes[num]).__name__  == "whatsapper"):
							damage = 0
							cura = self.whatsapper_heal(num)
							correct_election = True
		return damage, cura, charac
#mirar este tambien
	def players_turn(self):
		finish_turn = False
		self.print_players_turn()
		jugador = 1
		num = 0
		while ((num < len(self.personajes))and (len(self.enemies) > 0) and not finish_turn):
			damage, cura, charac = self.eleccion_attack(num, jugador)
			if (charac == 's' and (type(self.personajes[num]).__name__ == "procrastinator")):
				self.hit_all_enemies(num, damage)
			elif (damage > 0):
				self.hit_an_enemy(num, damage)
			elif (damage == 0 and cura == 0):
				print("El jugador ha sido revivido")
			else:
				self.choose_heal(cura)
			num = num + 1
			jugador = jugador + 1

	def enemies_turn(self):
		finish_turn = False
		num = 0
		self.print_monster_turn()
		while (num < len(self.enemies) and (len(self.personajes) > 0) and not finish_turn):
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
		self.print_monsters()

	def fight(self):
		finish_fight = False
		dead_players = False
		while (not finish_fight):
			self.players_turn()
			self.enemies_turn()
			if (len(self.enemies) == 0):
				finish_fight = True
			if (len(self.personajes) == 0):
				finish_fight = True
				dead_players = True
		return dead_players