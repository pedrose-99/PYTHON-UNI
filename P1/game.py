from characters import bookworm, worker, procrastinator, whatsapper, Characters
import enemies
import random
BOOKWORM_HP = 25
BOOKWORM_DMG = 9
WORKER_HP = 40
WORKER_DMG = 10
PROCRASTINSTOR_HP = 30
PROCRASTINSTOR_DMG = 6
WHATSAPPER_HP = 20
WHATSAPPER_DMG = 6
class Game:
	def __init__(self, rondas, turnos, niveles, movimiento):
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
				self.enemies.append((enemies.Partial_exam))
				num = num + 1
			elif (enemie == 2 and actual_stage == 4):
				#aañdir condicion de que solo sale en el stage 4
				self.enemies.append((enemies.Final_exam))
				num = num + 1
			elif (enemie == 3):
				self.enemies.append((enemies.theoretical_class))
				num = num + 1
			elif (enemie == 4):
				self.enemies.append((enemies.Teacher))
				num = num + 1

	
def eleccion_Character(num):
	correct_election = False
	while (not correct_election):
		print("Player", num, ". Please, choose a character (1-4):")
		charac = input()
		if (charac >= 1 and charac <= 4):
			print(charac,"\n")
			correct_election = True
			return charac

#def atack (self)
#	danio = random.randrange(1, charac.dmg)

def eleccion_atack(option):
	correct_election = False
	while (not correct_election):
		print("What are you going to do?: ")
		charac = input()
		if (charac == 'a' or charac == 's'):
			if (charac == 'a'):
				atack()
			correct_election = True
			return charac


