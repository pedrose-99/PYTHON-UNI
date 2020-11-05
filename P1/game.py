from characters import bookworm, worker, procrastinator, whatsapper, Characters
from enemies import Teacher, Final_exam, Partial_exam, theoretical_class
import random
#Constantes de la vida y daño de los personajes
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
#Constantes de la vida y daño de los enemigos
PARTIAL_HP = 20
PARTIAL_DMG = 6
FINAL_HP = 40
FINAL_DMG = 12
THEORICAL_HP = 8
THEORICAL_DMG = 4
TEACHER_HP = 15
TEACHER_DMG = 7

class Game:
	def __init__(self, rondas, stages, actual_stage, personajes_vivos, enemigos_vivos):
		self.personajes = []
		self.enemies = []
		self.muertos = []

	def add_player(self, eleccion):
		if (eleccion == 1):
			self.personajes.append((bookworm(BOOKWORM_HP, BOOKWORM_DMG, BOOKWORM_SPECIAL)))
		elif (eleccion == 2):
			self.personajes.append((worker(WORKER_HP, WORKER_DMG, WORKER_SPECIAL)))
		elif (eleccion == 3): 
			self.personajes.append((procrastinator(PROCRASTINSTOR_HP,PROCRASTINSTOR_DMG, PROCRASTINSTOR_SPECIAL)))
		elif (eleccion == 4):
			self.personajes.append((whatsapper(WHATSAPPER_HP, WHATSAPPER_DMG, WHATSAPPER_SPECIAL)))

	def add_enemies(self, actual_stage):
		num = 0
		monsters = 3
		while (num < monsters):
			enemie = random.randrange(1, 4)
			if (enemie == 1):
				self.enemies.append((Partial_exam(PARTIAL_HP, PARTIAL_DMG)))
				num = num + 1
			elif (enemie == 2 and actual_stage >= 4):
				self.enemies.append((Final_exam(FINAL_HP, FINAL_DMG)))
				num = num + 1
			elif (enemie == 3):
				self.enemies.append((theoretical_class(THEORICAL_HP, THEORICAL_DMG + actual_stage)))
				num = num + 1
			elif (enemie == 4):
				self.enemies.append((Teacher(TEACHER_HP, TEACHER_DMG)))
				num = num + 1
	def add_dead(self, character):
		if (character == bookworm):
			self.muertos.append((bookworm(BOOKWORM_HP, BOOKWORM_DMG, BOOKWORM_SPECIAL)))
		elif (character == worker):
			self.muertos.append((worker(WORKER_HP, WORKER_DMG, WORKER_SPECIAL)))
		elif (character == procrastinator): 
			self.muertos.append((procrastinator(PROCRASTINSTOR_HP,PROCRASTINSTOR_DMG, PROCRASTINSTOR_SPECIAL)))
		elif (character == whatsapper):
			self.muertos.append((whatsapper(WHATSAPPER_HP, WHATSAPPER_DMG, WHATSAPPER_SPECIAL)))


	
	def eleccion_Character(self, num):
		correct_election = False
		while (not correct_election):
			print("Player", num, ". Please, choose a character (1-4):")
			charac = input()
			if (charac >= 1 and charac <= 4):
				print(charac,"\n")
				correct_election = True
				return charac

	def attack (self, dmg):
		damage = random.randrange(1, dmg)
		return damage

	def eleccion_attack(self, game ,num,  option, rondas, personajes_vivos, players):
		correct_election = False
		cura = 0
		players = int(players)
		while (not correct_election):
			print("What are you going to do?: ")
			charac = input()
			if (charac == 'a' or charac == 's'):
				if (charac == 'a'):
				#damage = attack(characters.dmg) (PREGUNTAR POR QUE NO FUNCIONA)
					damage = random.randrange(1, game.personajes[num].dmg)
					if (game.personajes[num].special > 0):
						game.personajes[num].special = game.personajes[num].special - 1
					correct_election = True
					return damage, cura
				else:
					if (game.personajes[num].special == 0):
						if (game.personajes[num].type == 1):
							if(personajes_vivos < players):
								election = input()
								#preguntar
							#		add_player(election)
								game.personajes[num].special = 4
							else:
								print("All players are alive, so the skill will not used")
						elif (game.personajes[num].type == 2):
							damage = damage = random.randrange(1, game.personajes[num].dmg)
							damage = (damage + game.personajes[num].dmg) * 1.5
							correct_election = True
							game.personajes[num].special = 3
							return damage, cura
						elif (game.personajes[num].type == 3 and game.personajes[num].uso_habilidad == 1):
							print("aun no lo hice")
							game.personajes[num].special = 3
							game.personajes[num].uso_habilidad = 0
						elif (game.personajes[num].type == 4):
							damage = 0
							cura = game.personajes[num].dmg * 2
							game.personajes[num].special = 3
							return damage, cura

#AÑADIR QUE RETURNEE 2 respuestas, 1 del dmg y otra de la habilidad especial 
	def reset_stats(self, game, personajes_vivos):
		num = 0
		while (num < personajes_vivos):
			if (game.personajes[num].type == 1):
				game.personajes[num].special = BOOKWORM_SPECIAL
			elif (game.personajes[num].type == 3):
				game.personajes[num].special = 3
				game.personajes[num].uso_habilidad = 1
			else:
				game.personajes[num].special = 3
			game.personajes[num].hp_actual = game.personajes[num].hp_actual + game.personajes[num].hp/4
			if (game.personajes[num].hp_actual > game.personajes[num].hp):
				game.personajes[num].hp_actual = game.personajes[num].hp
			num = num + 1
	def quitar_vida(self, hp, damage):
		hp = hp - damage
		return hp
	
	def print_stats(self):
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
	
	def print_actual_stage(self, actual_stage):
		print("********************************************************")
		print("				************************					")
		print("				*        STAGE", actual_stage,"      *	")
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
#comentraio para ver si me funciona bien git hub

