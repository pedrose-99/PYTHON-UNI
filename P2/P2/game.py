from characters import Bookworm, Worker, Procrastinator, Whatsapper
from enemies import Teacher, Final_exam, Partial_exam, Theoretical_class
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
		self.characters = []
		self.enemies = []
		self.dead_characters = []
		self.rondas = 1
		self.players = players
		self.monsters = 3
		self.stages = stages
		self.momment_stage = 0
		self.sockets = []
		self.current_turn = 0
		self.lleno = False
		self.names = []
		self.turnos_muertos = []

	def characters_dead(self):
		return (len(self.characters) == 0)

	def monsters_dead(self):
		return len(self.enemies) == 0

	def next_turn(self):
		self.current_turn += 1

#funciones de los print necesarios
	def print_all_characters(self):
		bookworm = Bookworm().__str__()
		worker = Worker().__str__()
		procrasti = Procrastinator().__str__()
		whats = Whatsapper().__str__()
		all_characters = ("***********		 AVAILABLE CHARACTERS		 ***********\n"+"1.- "+bookworm+ "2.- "+worker+ "3.- "+procrasti+ "4.- "+ whats+ "\n********************************************************\n")
		return all_characters

	def print_current_stage(self):
		return ("		********************************************************\n"+"				************************					\n"+"				*        STAGE"+str(self.momment_stage)+"      *	\n"+"				************************					\n"+"				---- CURRENT MONSTERS ----			\n"+"		 	  ++++++++++++++++++++++++++++++++++++++		\n")

	def print_players_turn(self):
		return ("		\n"+"				 ------------------------\n"+"				 -     PLAYERS TURN     -\n"+"				 ------------------------\n"+"		\n")

	def print_monster_turn(self):
		return ("		\n"+"				 ------------------------\n"+"				 -     MONSTERS TURN     -\n"+"				 ------------------------\n"+"		\n")


	def print_characters_hp(self):
		num = 1
		for c in self.characters:
			print(str(num)+".- "+c.__class__.__name__+" has "+str(c.hp_real)+"/"+str(c.hp)+" hp")
			num = num + 1
	
	def print_dead_characters(self):
		num = 1
		mg = ""
		for c in self.dead_characters:
			mg = (mg+str(num)+".- "+c.__class__.__name__+" ("+self.names[num - 1]+")\n")
			num = num + 1
		return mg
	
	def print_monsters(self):
		mg = ""
		for e in self.enemies:
			cadena = e.__str__()
			mg = mg+(cadena)+"\n"
		mg = mg+"		 	  ++++++++++++++++++++++++++++++++++++++		\n"
		return mg

	def print_characters(self):
		num = 1
		mg = ""
		for p in self.characters:
			cadena = p.__str__()
			mg = (mg+num+".- "+cadena+"\n")
			num= num + 1
		return mg

	def print_damage(self, num, enemy, damage):
		return(str(type(self.characters[num]).__name__)+" ("+(self.names[num])+") did "+str(damage)+" damage to "+str(type(self.enemies[enemy]).__name__)+"."+ str(type(self.enemies[enemy]).__name__)+ " has "+ str(self.enemies[enemy].hp)+" hp left.")

#funciones de control de estadisticas	
	def cooldown_reduction(self, num):
		if (self.characters[num].special > 0):
			self.characters[num].special = self.characters[num].special - 1

	def reset_stats(self):
		num = 0
		while (num < len(self.characters)):
			character = type(self.characters[num]).__name__
			if (character == "Bookworm"):
				self.characters[num].special = BOOKWORM_SPECIAL
			elif (character == "Procrastinator"):
				self.characters[num].special = PROCRASTINSTOR_SPECIAL
				self.characters[num].uso_habilidad = 1
			else:
				self.characters[num].special = 3
			self.characters[num].hp_real = self.characters[num].hp_real + self.characters[num].hp/4
			if (self.characters[num].hp_real > self.characters[num].hp):
				self.characters[num].hp_real = self.characters[num].hp
			num = num + 1
		self.rondas = 1

	def update_stage(self):
		self.momment_stage = self.momment_stage + 1
		stg = str(self.print_current_stage())
		self.reset_stats()
		self.enemies = self.add_enemies()
		mon = str(self.print_monsters())
		return stg+mon

	def reset_dead_players(self, character):
		self.dead_characters[len(self.dead_characters) - 1].hp_real = self.dead_characters[len(self.dead_characters) - 1].hp
		if (character == "Bookworm"):
			self.dead_characters[len(self.dead_characters) - 1].special = BOOKWORM_SPECIAL
		elif (character == "Procrastinator"):
			self.dead_characters[len(self.dead_characters) - 1].special = PROCRASTINSTOR_SPECIAL
			self.dead_characters[len(self.dead_characters) - 1].uso_habilidad = 1
		else:
			self.dead_characters[len(self.dead_characters) - 1].special = 3

#funciones para añadir jugadores y enemigos además de controlar si mueren o no
	def add_player(self, eleccion, c_socket, name):
		if (eleccion == 1):
			self.characters.append(Bookworm())
		elif (eleccion == 2):
			self.characters.append(Worker())
		elif (eleccion == 3): 
			self.characters.append(Procrastinator())
		elif (eleccion == 4):
			self.characters.append(Whatsapper())
		self.sockets.append(c_socket)
		self.names.append(name)

	def add_enemies(self):
		num = 0
		while (num < self.monsters):
			enemy = random.randrange(1, 5)
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

	def character_dead(self, random_charac):
		dead = ""
		if (self.characters[random_charac].hp_real <= 0):
			name = str(type(self.characters[random_charac]).__name__)
			dead = str(name)+" ("+self.names[random_charac]+") has been defeated. It can not make any move until revived.\n"
			self.dead_characters.append(self.characters[random_charac])
			self.turnos_muertos.append(random_charac)
			self.reset_dead_players(name)
			self.characters.pop(random_charac)
		return dead

	def dead_monster(self, enemy_random):
		dead_monster = False
		dam = str("")
		if (self.enemies[enemy_random].hp <= 0):
			dam = (type(self.enemies[enemy_random]).__name__+ " has been defeated. It can not make any move.\n")
			self.enemies.pop(enemy_random)
			dead_monster = True
		return dead_monster, dam

#funciones de ataques especiales	
	def bookworm_revive(self, num):
		correct_option = False
		damage = 0
		while (not correct_option):
			election = random.randrange(1, len(self.dead_characters) + 1)
			election = int(election)
			if (election >= 1 and election <= (len(self.dead_characters))):
				election = election - 1
				self.characters.append(self.dead_characters[election])
				self.dead_characters.pop(election)
				self.turnos_muertos.pop(election)
				self.characters[num].special = BOOKWORM_SPECIAL
				correct_option = True
		return damage

	def worker_special_attack(self, num):
		damage = random.randrange(1, self.characters[num].dmg)
		damage = (damage + self.characters[num].dmg) * 1.5
		self.characters[num].special = WORKER_SPECIAL
		return damage
	
	def procrastinator_passive(self, num, damage):
		if (type(self.characters[num]).__name__ == "Procrastinator" and self.rondas >= 1):
			damage = damage + self.rondas - 1
		return damage

	def procrastinator_special_attack(self, num):
		damage = random.randrange(1, self.characters[num].dmg)
		damage = damage + self.characters[num].dmg + self.momment_stage
		self.characters[num].special = PROCRASTINSTOR_SPECIAL
		self.characters[num].uso_habilidad = 0
		return damage

	def whatsapper_heal(self, num):
		cura = self.characters[num].dmg * 2
		self.characters[num].special = WHATSAPPER_SPECIAL
		return cura
	
	def choose_heal(self, cura):
		correct_heal = False
		self.print_characters_hp()
		while (not correct_heal):
			random_charac = random.randrange(1, len(self.characters) + 1)
			random_charac = int(random_charac)
			if (self.characters[random_charac - 1].hp_real < self.characters[random_charac - 1].hp):
				correct_heal = True
				self.characters[random_charac - 1].hp_real = self.characters[random_charac - 1].hp_real + cura
				if (self.characters[random_charac - 1].hp_real > self.characters[random_charac - 1].hp):
					self.characters[random_charac - 1].hp_real = self.characters[random_charac - 1].hp
					return str(type(self.characters[random_charac - 1]).__name__)+" ("+self.names[random_charac - 1]+") has been completely restored. Hp = "+str(self.characters[random_charac - 1].hp_real)
				else:
					return str(type(self.characters[random_charac - 1]).__name__)+ " ("+self.names[random_charac - 1]+") has "+str(self.characters[random_charac - 1].hp_real)+" of "+str(self.characters[random_charac - 1].hp)+ " hp"

#funciones para golpear
	def hit_all_enemies(self, num, damage, name):
		enemy_random = 0
		dam_def = ""
		dam = ""
		while (enemy_random < len(self.enemies)):
			self.enemies[enemy_random].take_life(damage)
			if (self.enemies[enemy_random].hp < 0):
				self.enemies[enemy_random].hp = 0
			dam = self.print_damage(num, enemy_random, damage)	
			dead_monster, dead = self.dead_monster(enemy_random)
			if(not dead_monster):
				enemy_random = enemy_random + 1
			dam_def = dam_def+dam+"\n"+dead
		return dam_def

	def hit_an_enemy(self, num, damage, name):
		enemy_random =random.randrange(0, len(self.enemies))
		self.enemies[enemy_random].take_life(damage)
		if (self.enemies[enemy_random].hp < 0):
			self.enemies[enemy_random].hp = 0
		dam = self.print_damage(num, enemy_random, damage)
		dead_monster, dead = self.dead_monster(enemy_random)
		dam = str(dam)+str(dead)
		return str(dam)

#funciones para elegir el ataque
	def eleccion_attack(self, num, jugador, charac, name):
		cura = 0
		coldown = True
		damage = 0
		message = ""
			#charac = input((type(self.characters[num]).__name__+" (Player "+ str(jugador)+") .""What are you going to do?: "))
		if (charac == 'a'):
			damage = self.characters[num].get_damage()
			self.cooldown_reduction(num)
			damage = self.procrastinator_passive(num, damage)
		elif (charac == 's'):
			if (self.characters[num].special == 0):
				coldown = False
				if (type(self.characters[num]).__name__  == "Bookworm"):
					if(len(self.characters) < self.players):
						damage = self.bookworm_revive(num)
					else:
						message = "All players are alive. The skill can not used"
						coldown = True
				elif (type(self.characters[num]).__name__  == "Worker"):
					damage = self.worker_special_attack(num)
				elif (type(self.characters[num]).__name__  == "Procrastinator"):
					if ((self.characters[num].uso_habilidad == 1)):
						damage = self.procrastinator_special_attack(num)
					else:
						message ="You can not use more your special attack in this stage"
				elif (type(self.characters[num]).__name__  == "Whatsapper"):
					damage = 0
					cura = self.whatsapper_heal(num)
			elif (type(self.characters[num]).__name__  == "Procrastinator") and (self.characters[num].uso_habilidad == 0):
				message = "You can not use more your special attack in this stage"
				coldown = True
			else:
				message = "You can not use your special attack now"
				coldown = True
		elif (charac == 'm'):
			print("My character has "+str(self.characters[num].hp_real)+"/"+str(self.characters[num].hp)+" hp")
		return damage, cura, charac, coldown, message

#funciones para controlar el turno de los jugadores y enemigos
	def players_turn(self, charac, name):
		self.print_players_turn()
		next = True
		i = 0
		#if self.players > len(self.characters):
		#	i = self.players - len(self.characters)
		#while ((num < len(self.characters))and (len(self.enemies) > 0) and not finish_turn):
		damage, cura, charac, coldown, message = self.eleccion_attack(self.current_turn - i, self.current_turn + 1, charac, name)
		if (charac == 's' and (type(self.characters[self.current_turn - i]).__name__ == "Procrastinator") and not coldown):
			dam = self.hit_all_enemies(self.current_turn - i, damage, name)
		elif (damage > 0):
			dam = self.hit_an_enemy(self.current_turn - i, damage, name)
		elif (damage == 0 and cura == 0 and not coldown):
			dam = (type(self.characters[len(self.characters)-1]).__name__+" ("+self.names[len(self.characters)-1]+") has returned to the game")
		elif cura > 0 and not coldown:
			dam = self.choose_heal(cura)
		else:
			dam = ""
			next = False
		return str(dam), next, message
		#	num = num + 1
		#	jugador = jugador + 1

	def enemies_turn(self):
		num = 0
		dam_def = ""
		if(len(self.enemies) > 0):
			turn = self.print_monster_turn()
		while (num < len(self.enemies) and (len(self.characters) > 0)):
			random_charac = random.randrange(0, len(self.characters))
			damage = self.enemies[num].get_damage()
			if(type(self.enemies[num]).__name__ == "Theoretical_class"):
				damage = damage + self.momment_stage
			self.characters[random_charac].take_life(damage)
			if (self.characters[random_charac].hp_real < 0):
				self.characters[random_charac].hp_real = 0
			dam = str(type(self.enemies[num]).__name__)+" did "+ str(damage)+" damage to "+ str(type(self.characters[random_charac]).__name__)+" ("+self.names[random_charac]+")"+". "+ str(type(self.characters[random_charac]).__name__)+" ("+self.names[random_charac]+")"+" has "+ str(self.characters[random_charac].hp_real)+" hp left. \n"
			num = num + 1
			dead = str(self.character_dead(random_charac))
			dam_def = str(dam_def)+str(dam)+str(dead)
		dam_def = str(turn)+str(dam_def)
		return dam_def

#función para que enemigos y aliados peleen
	def fight(self):
		finish_fight = False
		dead_players = False
		finish_game = False
		self.update_stage()
		while (not finish_fight):
			self.players_turn()
			self.enemies_turn()
			self.rondas = self.rondas + 1
			if (len(self.enemies) == 0):
				finish_fight = True
			if (len(self.characters) == 0):
				finish_fight = True
				dead_players = True
		if (dead_players or self.stages == self.momment_stage):
			finish_game = True
			if (dead_players):
				print("You lost the game!!! Try again")
			else:
				print("You won the game!!! Congratulations")
		return finish_game