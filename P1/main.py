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
	num = 1
	actual_stage = 1
	enemigos_vivos = 3
	rondas = 1
	personajes_vivos = int(players)
	game_instance = game.Game(rondas, stages, actual_stage, personajes_vivos, enemigos_vivos)
	if (stages == 1 and players == 1):
		print("A game with one stage will be set up for one player.\n")
	game_instance.print_stats()
	while (num <= int(players)):
		print("Player", num, ". Please, choose a character (1-4): ")
		election = int(input())
		if (election >= 1 and election <= 4):
			game_instance.add_player(election)
			#hacer diccionario guardando los personajes
			print(game_instance.personajes)
			num = num + 1
			Finish_Game = False
	# AÑADIR FUNCION PARA QUE TE IMPRIMA LOS PERSONAJES Y SUS STATS

	while (actual_stage <= int(stages) and not Finish_Game):
		enemigos_vivos = 3
		num = 0
		game_instance.add_enemies(actual_stage)
		#while (num < int(players)):
			#game_instance.personajes[num].special = 1
			#num = num + 1
		game_instance.print_actual_stage(actual_stage)
		num = 0
		while (num < enemigos_vivos):
			print("			",game_instance.enemies[num])
			num = num + 1
		print("		 	  ++++++++++++++++++++++++++++++++++++++		")
		#hacer un print enemies stats
		game_instance.reset_stats(game_instance, personajes_vivos)
		while (personajes_vivos > 0 and enemigos_vivos > 0):
			game_instance.print_players_turn()
			num = 0
			cura = 0
			jugador = 1
			while (num < personajes_vivos and enemigos_vivos > 0):
				if (game_instance.personajes[num].hp_actual > 0 and enemigos_vivos > 0 and personajes_vivos > 0):
					print(game_instance.personajes[num],"Player", jugador,".")
					damage, cura = game_instance.eleccion_attack(game_instance, num, election, rondas, personajes_vivos, players)
					#Añadir que tiene que recibir 2 variables
					if (damage > 0):
						enemie_random =random.randrange(0, enemigos_vivos)
						game_instance.enemies[enemie_random].hp = game_instance.quitar_vida(game_instance.enemies[enemie_random].hp, damage)
						print(game_instance.personajes[num],"did", damage,"damage to ", game_instance.enemies[enemie_random],".", game_instance.enemies[enemie_random], "has", game_instance.enemies[enemie_random].hp,"hp left.")	
						if (game_instance.enemies[enemie_random].hp <= 0 and enemigos_vivos > 0):
							print("ENEMIGO", game_instance.enemies[enemie_random], "ESTA MUERTISIMO")
							game_instance.enemies.pop(enemie_random)
							enemigos_vivos = enemigos_vivos - 1
					else:
						random_charac = random.randrange(0, personajes_vivos)
						game_instance.personajes[random_charac].hp_actual = game_instance.personajes[random_charac].hp_actual + cura
						if (game_instance.personajes[random_charac].hp_actual > game_instance.personajes[random_charac].hp):
							game_instance.personajes[random_charac].hp_actual = game_instance.personajes[random_charac].hp
							print("The", game_instance.personajes[random_charac], "has been completely restored. Hp =", game_instance.personajes[random_charac].hp_actual)
						else:
							print("The", game_instance.personajes[random_charac], "has",game_instance.personajes[random_charac].hp_actual,"of",game_instance.personajes[random_charac].hp, "hp ")
					num = num + 1
					jugador = jugador + 1
				else:
					num = num + 1
			num = 0
			if (enemigos_vivos > 0 and personajes_vivos > 0):
				game_instance.print_monster_turn()
			while (num < enemigos_vivos and personajes_vivos > 0):
				random_charac = random.randrange(0, personajes_vivos)
				damage = game_instance.attack(game_instance.enemies[num].dmg)
				if (game_instance.enemies[num] == enemies.Teacher and damage == 7):
					damage = 14
				game_instance.personajes[random_charac].hp_actual = game_instance.quitar_vida(game_instance.personajes[random_charac].hp_actual, damage)
				print(game_instance.enemies[num],"did", damage,"damage to ", game_instance.personajes[random_charac],".", game_instance.personajes[random_charac], "has", game_instance.personajes[random_charac].hp_actual,"hp left.")
				num = num + 1
				if (game_instance.personajes[random_charac].hp_actual <= 0):
					print("EL PERSONAJE", game_instance.personajes[random_charac], "NECESITA QUE LE REVIVAN")
					game_instance.add_dead(game_instance.personajes[random_charac])
					game_instance.personajes.pop(random_charac)
					personajes_vivos = personajes_vivos - 1
			rondas = rondas + 1
			if (personajes_vivos == 0):
				print("HAS PERDIDO ")
				Finish_Game = True
			elif (enemigos_vivos == 0 and actual_stage == int(stages)):
				print("HAS GANADO")
				Finish_Game = True
			elif (enemigos_vivos == 0):
				actual_stage = actual_stage + 1
				rondas = 1


#Al terminar el programa comprobar las reglas de los enemigos
