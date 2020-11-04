import sys
import characters
import enemies
import game
import random

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

#no se si empezar el bucle aqui (creo que no)
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
	personajes_vivos = int(players)
	enemigos_vivos = 3
	game_instance = game.Game(rondas, stages, actual_stage, personajes_vivos, enemigos_vivos)
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
	while (actual_stage < int(stages) or Finish_Game):
		game_instance.add_enemies(actual_stage)
		print("AQUI VAN LOS ENEMIGOS")
		#hacer un print enemies stats
		while (personajes_vivos > 0 and enemigos_vivos > 0):
			num = 0
			while (num < personajes_vivos):
				if (game_instance.charactrs[num].hp_actual > 0 and enemigos_vivos > 0):
					damage = game_instance.eleccion_attack(game_instance.charactrs[num], election)
					#Añadir que tiene que recibir 2 variables
					enemie_random =random.randrange(0, enemigos_vivos)
					print("Daño realizado a ", game_instance.enemies[enemie_random] ,damage)
					print("VIDA ANTES DE QUE LE ZURRE ", game_instance.enemies[enemie_random], game_instance.enemies[enemie_random].hp)
					game_instance.enemies[enemie_random].hp = game_instance.quitar_vida(game_instance.enemies[enemie_random].hp, damage)
					print("VIDA DESPUES DE QUE LE ZURRE", game_instance.enemies[enemie_random], game_instance.enemies[enemie_random].hp)
					num = num + 1
				else:
					num = num + 1
				if (game_instance.enemies[enemie_random].hp <= 0):
					print("ENEMIGO", game_instance.enemies[enemie_random], "ESTA MUERTISIMO")
					game_instance.enemies.pop(enemie_random)
					enemigos_vivos = enemigos_vivos - 1
			num = 0
			while (num < enemigos_vivos):
				random_charac = random.randrange(0, personajes_vivos)
				damage = game_instance.attack(game_instance.enemies[num].dmg)
				print("DAÑO QUE VOY A RECIBIR", damage)
				print("VIDA ANTES DE RECIBIR UN BOFETON", game_instance.charactrs[random_charac], game_instance.charactrs[random_charac].hp ,"/", game_instance.charactrs[random_charac].hp_actual, )
				game_instance.charactrs[random_charac].hp_actual = game_instance.quitar_vida(game_instance.charactrs[random_charac].hp_actual, damage)
				print("VIDA DESPUES DE RECIBIR UN BOFETON ", game_instance.charactrs[random_charac], game_instance.charactrs[random_charac].hp ,"/", game_instance.charactrs[random_charac].hp_actual)
				num = num + 1
				if (game_instance.charactrs[random_charac].hp_actual <= 0):
					game_instance.charactrs[random_charac].hp_actual = 0
					print("EL PERSONAJE", game_instance.charactrs[random_charac], "NECESITA QUE LE REVIVAN")
					personajes_vivos = personajes_vivos - 1
			rondas = rondas + 1
			if (personajes_vivos == 0):
				Finish_Game = True
				print("HAS PERDIDO ")
			elif (enemigos_vivos == 0 and actual_stage == int(stages)):
				print("HAS GANADO")
				Finish_Game = True
			elif (enemigos_vivos == 0):
				actual_stage = actual_stage + 1
				rondas = 0