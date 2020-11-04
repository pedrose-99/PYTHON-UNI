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
		self.charactrs = []
		self.enemies = []

	def add_player(self, eleccion):
		if (eleccion == 1):
			self.charactrs.append((bookworm(BOOKWORM_HP, BOOKWORM_DMG)))
		elif (eleccion == 2):
			self.charactrs.append((worker(WORKER_HP, WORKER_DMG)))
		elif (eleccion == 3): 
			self.charactrs.append((procrastinator(PROCRASTINSTOR_HP,PROCRASTINSTOR_DMG)))
		elif (eleccion == 4):
			self.charactrs.append((whatsapper(WHATSAPPER_HP, WHATSAPPER_DMG)))

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
				self.enemies.append((theoretical_class(THEORICAL_HP, THEORICAL_DMG)))
				num = num + 1
			elif (enemie == 4):
				self.enemies.append((Teacher(TEACHER_HP, TEACHER_DMG)))
				num = num + 1

	
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

	def eleccion_attack(self, characters , option):
		correct_election = False
		while (not correct_election):
			print("What are you going to do?: ")
			charac = input()
			if (charac == 'a' or charac == 's'):
				if (charac == 'a'):
				#damage = attack(characters.dmg) (PREGUNTAR POR QUE NO FUNCIONA)
					damage = random.randrange(1, characters.dmg)
					correct_election = True
					return damage
#AÑADIR QUE RETURNEE 2 respuestas, 1 del dmg y otra de la habilidad especial 

	def quitar_vida(self, hp, damage):
		hp = hp - damage
		return hp



#comentraio para ver si me funciona bien git hub

