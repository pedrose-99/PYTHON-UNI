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
	funcion(print_character_stats)
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



		def print_character(self, players):
			num = 0
		while (num < players):
			if (self.charactrs[num - 1] == "<class 'characters.bookworm'>"):
				