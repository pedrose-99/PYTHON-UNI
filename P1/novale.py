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



			from Characters import Bookworn, Worker, Whatsapper, procrastinator

			from Enemies import Partial_exam, Final_Exam, theoretical_class, Teacher



		def print_personaje(self, players):
			num = 0
		while (num < players):
			if (self.personajes[num - 1] == "<class 'characters.bookworm'>"):
				


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



class Characters:
	def __init__(self, hp, dmg, special):
		self.hp = hp
		self.dmg = dmg
		self.hp_actual = hp
	#	self.hability = ability
		self.__special = special

class bookworm(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(BOOKWORM_HP, BOOKWORM_DMG, BOOKWORM_SPECIAL)
		#self.hability = bookworm_ability

class worker(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(WORKER_HP, WORKER_DMG, WORKER_SPECIAL)
		#self.hability = worker_ability

class procrastinator(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(PROCRASTINSTOR_HP, WORKER_DMG, PROCRASTINSTOR_SPECIAL)
	#	self.hability = ability

class whatsapper(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(WHATSAPPER_HP, WHATSAPPER_DMG, WHATSAPPER_SPECIAL)
	#	self.hability = ability




				else:
					if (game.characters.special == 0):
						if (game.characters[num] == bookworm):
							if(personajes_vivos < players):
								election = input()
								#preguntar
									add_player(self, game.muertos[int(election) - 1])
							else:
								print("All players are alive, so the skill will not used")

						elif (game.characters == worker):
							damage = damage = random.randrange(1, game.characters[num].dmg)
							damage = (damage + game.characters[num].dmg) * 1,5
							correct_election = True
							return damage
						elif (game.characters[num] == procrastinator):
							print("aun no lo hice")
						elif (game.characters[num] == whatsapper):
							cura = game.characters[num].dmg * 2
							return damage, cura

								def add_dead_player(self, character, game):
			if (character == bookworm):

		elif (character == worker):
			add_player(2)
		elif (character == procrastinator): 
			add_player(3)
		elif (character == whatsapper):
			add_player(4)





class Characters:
	def __init__(self, hp, dmg, special):
		self.hp = hp
		self.dmg = dmg
		self.hp_actual = hp
		self.vida = True
		self.special = special

class bookworm(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(BOOKWORM_HP, BOOKWORM_DMG, BOOKWORM_SPECIAL)
		self.type = 1

class worker(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(WORKER_HP, WORKER_DMG, WORKER_SPECIAL)
		self.type = 2

class procrastinator(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(PROCRASTINSTOR_HP,PROCRASTINSTOR_DMG, PROCRASTINSTOR_SPECIAL)
		self.type = 3
		self.uso_habilidad = 1


class whatsapper(Characters):
	def __init__(self, hp, dmg, special):
		super().__init__(WHATSAPPER_HP, WHATSAPPER_DMG, WHATSAPPER_SPECIAL)
		self.type = 4
