import game
import getopt, sys
#funcion para recibir argumentos
def parse_args ():
	stages = 1
	players = 1
	opts, args = getopt.getopt(sys.argv[1:], "s:p:", ["stages=","players="])
	for o, a in opts:
		if o in ("-s", "--stages"):
			stages = a
		elif o in ("-p", "--players"):
			players = a
	return stages, players

#funcion para comprobar si los argumentos son erroneos
def check_args (stages, players):
	correct_stages = False
	correct_players = False
	start_game = False

	try:
		stages = int(stages)
		if (stages >= 1 and stages <= 10):
			correct_stages = True
		else:
			print("The value given for -s or --stages must be between 1 and 10. ")
	except ValueError:
		print("The value given for -s or --stages must be an integer number.")

	try:
		players = int(players)
		if (players >= 1 and players <= 4):
			correct_players = True
		else:
			print("The value given for -p or --players must be between 1 and 4. ")
	except ValueError:
		print("The value given for -p or --players must be an integer number.")
		
	if (correct_stages and correct_players):
		start_game = True
		return start_game

#funcion para seleccionar el personaje
def election_character(game_instance, num):
	correct_option = False
	while (not correct_option):
		election = input(("Player "+ str(num + 1)+". Please, choose a character (1-4): "))
		election = int(election)
		if (election >= 1 and election <= 4):
			game_instance.add_player(election)
			correct_option = True
		else:
			print("The option is not correct.")

#funcion para iniciar el juego
def init_game(players, stages, start_game):
	players = int(players)
	stages = int(stages)
	if (start_game):
		game_instance = game.Game(players, stages)
		game_instance.print_all_characters()
		for num in range (0, players):
			election_character(game_instance, num)
	return game_instance

#main del juego
try:
	stages, players = parse_args()
	start_game = check_args(stages, players)
	if (start_game):
		finish_game = False
		game_instance = init_game(players, stages, start_game)
		game_instance.print_characters()
		while (not finish_game):
			finish_game = game_instance.fight()
except:
	print("\nThe arguments given were wrong. Game has been stopped. Nobody wins.")
