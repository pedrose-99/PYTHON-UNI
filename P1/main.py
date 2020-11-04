import sys
import characters
import enemies
import game

class BadStagesError(Exception):
	pass
class BadPlayersError(Exception):
	pass
class ArgumentError(Exception):
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
try:
	correct_stages, correct_players, bad_stages, bad_players = check_args (stages, players)
	if (correct_stages and correct_players and bad_stages and bad_players):
		Finish_Game = False
except BadPlayersError:
	print("The value given for -p or --players must be between 1 and 4. ")
except BadStagesError:
	print("The value given for -s or --stages must be between 1 and 10. ")


while (not Finish_Game):
	if (stages == 1 and players == 1):
		print("A game with one stage will be set up for one player.\n")
	print("*********** AVAILABLE CHARACTERS ***********\n")
	print("1.- The bookworn -> Stats: 25HP and 9DMG\n")
	print("Skill: Revives one player(4 rounds)\n")
	print("2.- The worker -> Stats: 40HP and 10DMG\n")
	print("Skill: 1.5 * (DMG + DMG roll) damage to one enemy (3 rounds)\n")
	print("3.- The whatsapper -> Stats: 20HP and 6DMG\n")
	print("Skill: Heals 2*DMG to one player (3 rounds)\n")
	print("4.- The procrastinator-> Stats: 30HP and 6DMG\n")
	print("Passive: Adds +1 DMG each round. Resets at the beginning of each level.\n")
	print("Skill: DMG + DMG roll + stage level to all the enemies\n after the third round of each stage and once per stage.\n")
	print("********************************************************\n")
	num = 1
	actual_stage = 1
	rondas = 0
	turno = 0
	movimiento = 0
	game_instance = game.Game(rondas, turno, stages, movimiento)
	while (num <= int(players)):
		print("Player", num, ". Please, choose a character (1-4): ")
		election = int(input())
		if (election >= 1 and election <= 4):
			game_instance.add_player(election)
			#hacer diccionario guardando los personajes
			print(game_instance.charactrs)
			num = num + 1
			Finish_Game = True
	# AÑADIR FUNCION PARA QUE TE IMPRIMA LOS PERSONAJES Y SUS STATS
	print("********************************************************")
	print("				************************					")
	print("				*		STAGE 1        *					")
	print("				---- CURRENT MONSTERS ----			")
	print("		++++++++++++++++++++++++++++++++++++++		")
	game_instance.add_enemies(actual_stage)
	print("AQUI VAN LOS ENEMIGOS")
	#hacer un print enemies stats

