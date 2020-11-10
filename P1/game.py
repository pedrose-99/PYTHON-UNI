from characters import Bookworm, Worker, Procrastinator, Whatsapper
from enemies import Teacher, Final_exam, Partial_exam, Theoretical_class
import random

Bookworm_HP = 25
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
		self.rondas = 1
		self.players = players
		self.monsters = 3
		self.stages = stages
		self.momment_stage = 0


	def print_all_Characters(self):
		print("***********		 AVAILABLE Characters		 ***********")
		bookworm = Bookworm().__str__()
		worker = Worker().__str__()
		procrasti = Procrastinator().__str__()
		whats = Whatsapper().__str__()
		print("1.- ", bookworm)
		print("2.- ", worker)
		print("3.- ",procrasti)
		print("4.- ", whats)
		print("	********************************************************\n")
	
	def print_actual_stage(self):
		print("		********************************************************")
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

	def print_monsters(self):
		for e in self.enemies:
			cadena = e.__str__()
			print(cadena)

	def print_characters(self):
		num = 1
		print("")
		for p in self.personajes:
			cadena = p.__str__()
			print(num,".- ",cadena)
			num= num + 1
	
	def add_player(self, eleccion):
		if (eleccion == 1):
			self.personajes.append(Bookworm())
		elif (eleccion == 2):
			self.personajes.append(Worker())
		elif (eleccion == 3): 
			self.personajes.append(Procrastinator())
		elif (eleccion == 4):
			self.personajes.append(Whatsapper())

	def add_enemies(self):
		num = 0
		while (num < self.monsters):
			enemy = random.randrange(1, 4)
			if (enemy == 1):
				self.enemies.append(Partial_exam())
				num = num + 1
			elif (enemy == 2 and self.momment_stage >= 4):
				self.enemies.append(Final_exam())
				num = num + 1
			elif (enemy == 3):
				self.enemies.append(Theoretical_class())
				num = num + 1
			elif (enemy == 4):
				self.enemies.append(Teacher())
				num = num + 1
		return self.enemies

	def add_dead_player(self, character):
		if (character == "Bookworm"):
			self.muertos.append(Bookworm())
		elif (character == "Worker"):
			self.muertos.append(Worker())
		elif (character == "Procrastinator"): 
			self.muertos.append(Procrastinator())
		elif (character == "Whatsapper"):
			self.muertos.append(Whatsapper()) 

	def print_character_stats(self, num):
		print("The current round is :"+ str(self.rondas))
		print("My character has "+str(self.personajes[num].hp_real)+"/"+str(self.personajes[num].hp)+" hp")
		print("My cooldown is "+str(self.personajes[num].special))
	
	def cooldown_reduction(self, num):
		if (self.personajes[num].special > 0):
			self.personajes[num].special = self.personajes[num].special - 1

	def Procrastinator_passive(self, num, damage):
		if (self.personajes[num] == Procrastinator):
			damage = damage + self.rondas - 1
		return damage

	def type_character(self, character):
		if (character == "Bookworm"):
			self.personajes.append(Bookworm())
		elif (character == "Worker"):
			self.personajes.append(Worker())
		elif (character == "Procrastinator"): 
			self.personajes.append(Procrastinator())
		elif (character == "Whatsapper"):
			self.personajes.append(Whatsapper()) 

	def Bookworm_revive(self, num):
		correct_option = False
		damage = 0
		while (not correct_option):
			election = input("which character do you want to revive: ")
			election = int(election)
			if (election >= 1 and election <= (len(self.muertos))):
				election = election - 1
				new_player = type(self.muertos[election]).__name__
				print(new_player)
				self.type_character(new_player)
				self.personajes[num].special = Bookworm_SPECIAL
				correct_option = True
		return damage

	def Worker_special_attack(self, num):
		damage = random.randrange(1, self.personajes[num].dmg)
		damage = (damage + self.personajes[num].dmg) * 1.5
		self.personajes[num].special = Worker_SPECIAL
		return damage

	def Procrastinator_special_attack(self, num):
		damage = random.randrange(1, self.personajes[num].dmg)
		damage = damage + self.personajes[num].dmg + self.momment_stage
		self.personajes[num].special = PROCRASTINSTOR_SPECIAL
		self.personajes[num].uso_habilidad = 0
		return damage

	def Whatsapper_heal(self, num):
		cura = self.personajes[num].dmg * 2
		self.personajes[num].special = Whatsapper_SPECIAL
		return cura

#Comprobar tambien esta 
	def reset_stats(self):
		num = 0
		while (num < len(self.personajes)):
			character = type(self.personajes[num]).__name__
			if (character == "Bookworm"):
				self.personajes[num].special = Bookworm_SPECIAL
			elif (character == "Procrastinator"):
				self.personajes[num].special = PROCRASTINSTOR_SPECIAL
				self.personajes[num].uso_habilidad = 1
			else:
				self.personajes[num].special = 3
			self.personajes[num].hp_real = self.personajes[num].hp_real + self.personajes[num].hp/4
			if (self.personajes[num].hp_real > self.personajes[num].hp):
				self.personajes[num].hp_real = self.personajes[num].hp
			num = num + 1
		self.rondas = 0

	def quitar_vida(self, hp, damage):
		hp = hp - damage
		return hp

	def print_damage(self, num, enemy, damage):
		print(type(self.personajes[num]).__name__,"did", damage,"damage to ", type(self.enemies[enemy]).__name__,".", type(self.enemies[enemy]).__name__, "has", self.enemies[enemy].hp,"hp left.")
	
	def dead_monster(self, enemy_random):
		dead_monster = False
		if (self.enemies[enemy_random].hp <= 0):
			print(type(self.enemies[enemy_random]).__name__, "has been defeated. It can not make any move.")
			self.enemies.pop(enemy_random)
			dead_monster = True
		return dead_monster

	def hit_all_enemies(self, num, damage):
		enemy_random = 0
		while (enemy_random < len(self.enemies)):
			self.enemies[enemy_random].take_life(damage)
			if (self.enemies[enemy_random].hp < 0):
				self.enemies[enemy_random].hp = 0
			self.print_damage(num, enemy_random, damage)	
			dead_monster = self.dead_monster(enemy_random)
			if(not dead_monster):
				enemy_random = enemy_random + 1
			
	def hit_an_enemy(self, num, damage):
		enemy_random =random.randrange(0, len(self.enemies))
		self.enemies[enemy_random].take_life(damage)
		if (self.enemies[enemy_random].hp < 0):
			self.enemies[enemy_random].hp = 0
		self.print_damage(num, enemy_random, damage)
		dead_monster = self.dead_monster(enemy_random)
	
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
			if (charac == 'a' or charac == 's' or charac == 'm'):
				if (charac == 'a'):
					damage = self.personajes[num].get_damage()
					self.cooldown_reduction(num)
					correct_election = True
					damage = self.Procrastinator_passive(num, damage)
				elif (charac == 's'):
					if (self.personajes[num].special == 0):
						if (type(self.personajes[num]).__name__  == "Bookworm"):
							if(len(self.personajes) < self.players):
								damage = self.Bookworm_revive(num)
								correct_election = True
							else:
								print("All players are alive. The skill can not used")
						elif (type(self.personajes[num]).__name__  == "Worker"):
							damage = self.Worker_special_attack(num)
							correct_election = True
						elif ((type(self.personajes[num]).__name__  == "Procrastinator") and (self.personajes[num].uso_habilidad == 1)):
							damage = self.Procrastinator_special_attack(num)
							correct_election = True
						elif (type(self.personajes[num]).__name__  == "Whatsapper"):
							damage = 0
							cura = self.Whatsapper_heal(num)
							correct_election = True
					else:
						print("The skill is currently in cooldown for ", self.personajes[num].special," more rounds.")
				elif (charac == 'm'):
					self.print_character_stats(num)
		return damage, cura, charac
#mirar este tambien
	def players_turn(self):
		finish_turn = False
		self.print_players_turn()
		jugador = 1
		num = 0
		while ((num < len(self.personajes))and (len(self.enemies) > 0) and not finish_turn):
			damage, cura, charac = self.eleccion_attack(num, jugador)
			if (charac == 's' and (type(self.personajes[num]).__name__ == "Procrastinator")):
				self.hit_all_enemies(num, damage)
			elif (damage > 0):
				self.hit_an_enemy(num, damage)
			elif (damage == 0 and cura == 0):
				print("El jugador ha sido revivido")
			else:
				self.choose_heal(cura)
			num = num + 1
			jugador = jugador + 1
	
	def character_dead(self, random_charac):
		if (self.personajes[random_charac].hp_real <= 0):
			name = type(self.personajes[random_charac]).__name__
			print(name, "has been defeated. It can not make any move until revived.")
			self.add_dead_player(name)
			self.personajes.pop(random_charac)

	def enemies_turn(self):
		finish_turn = False
		num = 0
		if(len(self.enemies) > 0):
			self.print_monster_turn()
		while (num < len(self.enemies) and (len(self.personajes) > 0) and not finish_turn):
			random_charac = random.randrange(0, len(self.personajes))
			damage = self.enemies[num].get_damage()
			if(self.enemies[num] == Theoretical_class):
				damage = damage + self.momment_stage
			self.personajes[random_charac].take_life(damage)
			if (self.personajes[random_charac].hp_real < 0):
				self.personajes[random_charac].hp_real = 0
			print(type(self.enemies[num]).__name__,"did", damage,"damage to ", type(self.personajes[random_charac]).__name__,".", type(self.personajes[random_charac]).__name__, "has", self.personajes[random_charac].hp_real,"hp left.")
			num = num + 1
			self.character_dead(random_charac)

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
			self.rondas = self.rondas + 1
			if (len(self.enemies) == 0):
				finish_fight = True
			if (len(self.personajes) == 0):
				finish_fight = True
				dead_players = True
		return dead_players