import sys
from game import parse_args 

class ArgumentError(Exception):
	pass
class StagesErrorisimo(Exception):
	pass
class BadStagesError(Exception):
	pass
class BadPlayersError(Exception):
	pass

def parse_args ():
	import getopt, sys
	number_stages = 1
	number_players = 1
	opts, args = getopt.getopt(sys.argv[1:], "s:p:", ["stages=","players="])
	for o, a in opts:
		if o in ("-s", "--stages"):
			number_stages = a
		elif o in ("-p", "--players"):
			number_players = a
	return number_stages, number_players

stages, players = parse_args()

def check_args (stages, players):
	correct_stages = False
	correct_players = False
	bad_stages = False
	bad_players = False

	try:
		stages = int(stages)
		correct_stages = True
	except ValueError:
		print("The value given for -s or --stages must be an integer number.")
	
	try:
		players = int(players)
		correct_players = True
	except ValueError:
		print("The value given for -p or --players must be an integer number.")
	
	if stages >= 1 and stages <= 10:
		bad_stages = True

	if players >= 1 and players <= 4:
		bad_players = True
	
	if not bad_players and not bad_stages:
		raise BadPlayersError and BadStagesError
	elif not bad_players and bad_stages: 
		raise BadPlayersError
	elif bad_players and not bad_stages:
		raise BadStagesError

	if not correct_stages or not correct_players or not bad_stages or not bad_players:
		raise ArgumentError
	return correct_stages, correct_players, bad_stages, bad_players

n_stages, n_players = parse_args()
try:
	correct_stages, correct_players, bad_stages, bad_players = check_args(n_stages, n_players)	
except ArgumentError:
	print("Program finished due to bad arguments")
except BadPlayersError:
	print("The value given for -p or --players must be between 1 and 4. ")
except BadStagesError:
		print("The value given for -s or --stages must be between 1 and 10. ")







	print("********************************************************\n")
	funcion(print_personaje_stats)
	print("********************************************************\n")
	funcion(print_stage())
	active_stage = True
	while (active_stage):
		function(player_turn(Turn))
		function(enemies_turn(Turn))
		if (character.hp < 0)
			character.hp = 0



			from Characters import Bookworn, Worker, Whatsapper, Procrastinator

			from Enemies import Partial_exam, Final_Exam, theoretical_class, Teacher



		def print_personaje(self, players):
			num = 0
		while (num < players):
			if (self.personajes[num - 1] == "<class 'Characters.Bookworm'>"):
				


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



class Characters:
	def __init__(self, hp, dmg, special):
		self.hp = hp
		self.dmg = dmg
		self.hp_real = hp
	#	self.hability = ability
		self.__special = special

class Bookworm(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(Bookworm_HP, Bookworm_DMG, Bookworm_SPECIAL)
		#self.hability = Bookworm_ability

class Worker(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(Worker_HP, Worker_DMG, Worker_SPECIAL)
		#self.hability = Worker_ability

class Procrastinator(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(PROCRASTINSTOR_HP, Worker_DMG, PROCRASTINSTOR_SPECIAL)
	#	self.hability = ability

class Whatsapper(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(Whatsapper_HP, Whatsapper_DMG, Whatsapper_SPECIAL)
	#	self.hability = ability




				else:
					if (game.Characters.special == 0):
						if (game.Characters[num] == Bookworm):
							if(personajes_vivos < players):
								election = input()
								#preguntar
									add_player(self, game.muertos[int(election) - 1])
							else:
								print("All players are alive, so the skill will not used")

						elif (game.Characters == Worker):
							damage = damage = random.randrange(1, game.Characters[num].dmg)
							damage = (damage + game.Characters[num].dmg) * 1,5
							correct_election = True
							return damage
						elif (game.Characters[num] == Procrastinator):
							print("aun no lo hice")
						elif (game.Characters[num] == Whatsapper):
							cura = game.Characters[num].dmg * 2
							return damage, cura

								def add_dead_player(self, character, game):
			if (character == Bookworm):

		elif (character == Worker):
			add_player(2)
		elif (character == Procrastinator): 
			add_player(3)
		elif (character == Whatsapper):
			add_player(4)





class Characters:
	def __init__(self, hp, dmg, special):
		self.hp = hp
		self.dmg = dmg
		self.hp_real = hp
		self.vida = True
		self.special = special

class Bookworm(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(Bookworm_HP, Bookworm_DMG, Bookworm_SPECIAL)
		self.type = 1

class Worker(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(Worker_HP, Worker_DMG, Worker_SPECIAL)
		self.type = 2

class Procrastinator(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(PROCRASTINSTOR_HP,PROCRASTINSTOR_DMG, PROCRASTINSTOR_SPECIAL)
		self.type = 3
		self.uso_habilidad = 1


class Whatsapper(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(Whatsapper_HP, Whatsapper_DMG, Whatsapper_SPECIAL)
		self.type = 4



[15:35] David Roldán Álvarez
    
for e in game_instance.enemigos_vivos:
         e.print_stats()
​[15:37] David Roldán Álvarez
    
print(e.get_stats_str())
​[15:38] David Roldán Álvarez
    
return "HP" + str(self.hp) + "DMG" + str(self.dmg)
​[15:48] David Roldán Álvarez
    
for e in self.enemies:
      print(e._class._name_)
​[15:49] David Roldán Álvarez
    
self.enemies[2]


			if (game_instance.enemies[num].type == 1):
				print("			  Partial exam: Stats: 20HP and 6DMG")
			elif (game_instance.enemies[num].type == 2):
				print("		   	  Final exam: Stats: 40P and 12DMG")
			elif (game_instance.enemies[num].type == 3):
				print("			  Theoretical: Stats: 8HP and 4DMG")
			elif (game_instance.enemies[num].type == 4):
				print("			  Teacher: Stats: 15HP and 7DMG")
			num = num + 1



				def eleccion_Character(self, num):
			correct_election = False
		while (not correct_election):
			charac = input(("Player", num, ". Please, choose a character (1-4):"))
			charac = int(charac)
			if (charac >= 1 and charac <= 4):
				print(charac,"\n")
				correct_election = True
		self.add_player(charac)



class Characters:
	def __init__(self, hp, dmg, special):
		self.hp = hp
		self.dmg = dmg
		self.hp_real = hp
		self.special = special
	
	def get_stats(self):
		pass

	def get_damage(self):
		pass

class Bookworm(Characters):
	def __init__(self, special):
		super().__init__(Bookworm_HP, Bookworm_DMG, special)
	
	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)
	
	def get_damage(self):
		damage = random.randrange(1, Bookworm_DMG)
		return damage

class Worker(Characters):
	def __init__(self, special):
		super().__init__(Worker_HP, Worker_DMG, special)
	
	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)
	
	def get_damage(self):
		damage = random.randrange(1, Worker_DMG)
		return damage

class Procrastinator(Characters):
	def __init__(self, special):
		super().__init__(PROCRASTINSTOR_HP,PROCRASTINSTOR_DMG, special)
		self.uso_habilidad = 1

	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)

	def get_damage(self):
		damage = random.randrange(1, PROCRASTINSTOR_DMG)
		return damage

class Whatsapper(Characters):
	def __init__(self, special):
		super().__init__(Whatsapper_HP, Whatsapper_DMG, special)
	
	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)

	def get_damage(self):
		damage = random.randrange(1, Whatsapper_DMG)
		return damage



class Enemies:
	def __init__(self, hp, dmg):
		self.hp = hp
		self.dmg = dmg
	
	def get_stats(self):
		pass

	def get_damage(self):
		pass


class Partial_exam(Enemies):
	def __init__(self):
		super().__init__(PARTIAL_HP, PARTIAL_DMG)

	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)
	
	def get_damage(self):
		damage = random.randrange(1, PARTIAL_DMG)
		return damage

# type(class.__name__)

class Final_exam(Enemies):
	def __init__(self):
		super().__init__(FINAL_HP, FINAL_DMG)

	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)

	def get_damage(self):
		damage = random.randrange(1, FINAL_DMG)
		return damage

class theoretical_class(Enemies):
	def __init__(self):
		super().__init__(THEORICAL_HP, THEORICAL_DMG)
	
	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)

	def get_damage(self):
		damage = random.randrange(1, THEORICAL_DMG)
		return damage

class Teacher(Enemies):
	def __init__(self):
		super().__init__(TEACHER_HP, TEACHER_DMG)

	def get_stats(self):
		return "HP" + str(self.hp) + "DMG" + str(self.dmg)

	def get_damage(self):
		damage = random.randrange(1, TEACHER_DMG)
		if (damage == 7):
			damage = 14
		return damage



class Partial_exam(Enemies):
	def __init__(self):
		super().__init__( hp, dmg)

	def get_stats(self):
		return ("HP"+str(self.hp)+"DMG"+str(self.dmg))
	
	def get_damage(self):
		damage = random.randrange(1, PARTIAL_DMG)
		return damage

# type(class.__name__)

class Final_exam(Enemies):
	def __init__(self, hp, dmg):
		super().__init__( hp, dmg)

	def get_stats(self):
		return ("HP"+str(self.hp)+"DMG"+str(self.dmg))

	def get_damage(self):
		damage = random.randrange(1, FINAL_DMG)
		return damage

class theoretical_class(Enemies):
	def __init__(self, hp, dmg):
		super().__init__( hp, dmg)
	
	def get_stats(self):
		return ("HP"+str(self.hp)+"DMG"+str(self.dmg))

	def get_damage(self):
		damage = random.randrange(1, THEORICAL_DMG)
		return damage

class Teacher(Enemies):
	def __init__(self, hp, dmg):
		super().__init__(hp, dmg)

	def get_stats(self):
		return ("HP"+str(self.hp)+"DMG"+str(self.dmg))

	def get_damage(self):
		damage = random.randrange(1, TEACHER_DMG)
		if (damage == 7):
			damage = 14
		return damage