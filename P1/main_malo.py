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

def check_args (stages, players):
	correct_stages = False
	correct_players = False
	bad_players = False

	try:
		stages = int(stages)
		if stages >= 1 and stages <= 10:
			correct_stages = True
		#quitar las variables del bad_stages..
	except ValueError:
		print("The value given for -s or --stages must be an integer number.")
	
	try:
		players = int(players)
		correct_players = True
	except ValueError:
		print("The value given for -p or --players must be an integer number.")
	

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

stages, players = parse_args()

try:
	correct_stages, correct_players, bad_stages, bad_players = check_args (stages, players)
	if (correct_stages and correct_players and bad_stages and bad_players):
		Finish_Game = False
except BadPlayersError:
	print("The value given for -p or --players must be between 1 and 4. ")
except BadStagesError:
	print("The value given for -s or --stages must be between 1 and 10. ")
except ArgumentError:
	print("Program finished due to bad arguments")

while (not Finish_Game):
	num = 1
	actual_stage = 1
	enemigos_totales = 3
	rondas = 1
	#declarar en el game.
	personajes_vivos = int(players)
	personajes_totales = int(players)
	game_instance = game.Game(rondas, stages, actual_stage, personajes_vivos, enemigos_totales,personajes_totales)
	#hacerlo en una funcion
	if (stages == 1 and players == 1):
		print("A game with one stage will be set up for one player.\n")
	game_instance.print_stats()#print_characters
	while (num <= int(players)):
		election = input(("Player",num,". Please, choose a character (1-4):" ))
		election = int(election)
		if (election >= 1 and election <= 4):
			game_instance.add_player(election)
			game_instance.print_characters(game_instance, num - 1)
			num = num + 1
			Finish_Game = False

	while (game_instance.actual_stage <= int(stages) and not Finish_Game):
		num = 0
		game_instance.enemigos_vivos = enemigos_totales
		game_instance.add_enemies(game_instance.enemigos_vivos)
		game_instance.print_actual_stage(game_instance)
		num = 0
		#for ()
		while (num < game_instance.enemigos_vivos):
			if (game_instance.enemies[num].type == 1):
				print("			  Partial exam: Stats: 20HP and 6DMG")
			elif (game_instance.enemies[num].type == 2):
				print("		   	  Final exam: Stats: 40P and 12DMG")
			elif (game_instance.enemies[num].type == 3):
				print("			  Theoretical: Stats: 8HP and 4DMG")
			elif (game_instance.enemies[num].type == 4):
				print("			  Teacher: Stats: 15HP and 7DMG")
			num = num + 1
		print("		 	  ++++++++++++++++++++++++++++++++++++++		")
		game_instance.reset_stats(game_instance, game_instance.personajes_vivos)
		while (game_instance.personajes_vivos > 0 and game_instance.enemigos_vivos > 0):
			game_instance.print_players_turn()
			num = 0
			cura = 0
			jugador = 1
			while (num < game_instance.personajes_vivos and game_instance.enemigos_vivos > 0):
				if (game_instance.personajes[num].hp_real > 0 and game_instance.enemigos_vivos > 0 and game_instance.personajes_vivos > 0):
				#	print(type(game_instance.personajes[num]).__name__,"Player", jugador,".")
					damage, cura, charac = game_instance.eleccion_attack(game_instance, num, election, jugador)
					if (charac == 's' and game_instance.personajes[num].type == 3):
						golpe = 0
						#for ()
						while (golpe < game_instance.enemigos_vivos):
							enemie_random =random.randrange(0, game_instance.enemigos_vivos)
							game_instance.enemies[golpe].hp = game_instance.quitar_vida(game_instance.enemies[golpe].hp, damage)
							print(type(game_instance.personajes[num]).__name__,"did", damage,"damage to ", type(game_instance.enemies[golpe]).__name__,".", type(game_instance.enemies[enemie_random]).__name__, "has", game_instance.enemies[enemie_random].hp,"hp left.")	
							if (game_instance.enemies[golpe].hp <= 0 and game_instance.enemigos_vivos > 0):
								print("ENEMIGO", type(game_instance.enemies[golpe]).__name__, "ESTA MUERTISIMO")
								game_instance.enemies.pop(golpe)
								game_instance.enemigos_vivos = game_instance.enemigos_vivos - 1
							else:
								golpe = golpe + 1
					elif (damage > 0):
						enemie_random =random.randrange(0, game_instance.enemigos_vivos)
						game_instance.enemies[enemie_random].hp = game_instance.quitar_vida(game_instance.enemies[enemie_random].hp, damage)
						print(type(game_instance.personajes[num]).__name__,"did", damage,"damage to ", type(game_instance.enemies[enemie_random]).__name__,".", type(game_instance.enemies[enemie_random]).__name__, "has", game_instance.enemies[enemie_random].hp,"hp left.")	
						if (game_instance.enemies[enemie_random].hp <= 0 and game_instance.enemigos_vivos > 0):
							print("ENEMIGO", type(game_instance.enemies[enemie_random]).__name__, "ESTA MUERTISIMO")
							game_instance.enemies.pop(enemie_random)
							game_instance.enemigos_vivos = game_instance.enemigos_vivos - 1
					elif (damage == 0 and cura == 0):
						print("El jugador ha sido revivido")
					else:
						correct_heal = False
						while (not correct_heal):
							random_charac = input("Which character do you want to heal:")
							random_charac = int(random_charac)
							if (random_charac > game_instance.personajes_vivos):
								print("Incorrect value")
							elif (game_instance.personajes[random_charac].hp_real < game_instance.personajes[random_charac].hp):
								correct_heal = True
								game_instance.personajes[random_charac].hp_real = game_instance.personajes[random_charac].hp_real + cura
								if (game_instance.personajes[random_charac].hp_real > game_instance.personajes[random_charac].hp):
									game_instance.personajes[random_charac].hp_real = game_instance.personajes[random_charac].hp
									print(type(game_instance.personajes[random_charac]).__name__, "has been completely restored. Hp =", game_instance.personajes[random_charac].hp_real)
								else:
									print(type(game_instance.personajes[random_charac]).__name__, "has",game_instance.personajes[random_charac].hp_real,"of",game_instance.personajes[random_charac].hp, "hp ")
							else:
								print(type(game_instance.personajes[random_charac]).__name__ ,"can not be heal" )		
					num = num + 1
					jugador = jugador + 1
				else:
					num = num + 1
			num = 0
			if (game_instance.enemigos_vivos > 0 and game_instance.personajes_vivos > 0):
				game_instance.print_monster_turn()
			while (num < game_instance.enemigos_vivos and game_instance.personajes_vivos > 0):
				random_charac = random.randrange(0, game_instance.personajes_vivos)
				damage = game_instance.attack(game_instance.enemies[num].dmg)
				if (game_instance.enemies[num] == enemies.Teacher and damage == 7):
					damage = 14
				game_instance.personajes[random_charac].hp_real = game_instance.quitar_vida(game_instance.personajes[random_charac].hp_real, damage)
				print(type(game_instance.enemies[num]).__name__,"did", damage,"damage to ", type(game_instance.personajes[random_charac]).__name__,".", type(game_instance.personajes[random_charac]).__name__, "has", game_instance.personajes[random_charac].hp_real,"hp left.")
				num = num + 1
				if (game_instance.personajes[random_charac].hp_real <= 0):
					print("EL PERSONAJE", type(game_instance.personajes[random_charac]).__name__, "NECESITA QUE LE REVIVAN")
					game_instance.add_dead(game_instance.personajes[random_charac])
					game_instance.personajes.pop(random_charac)
					game_instance.personajes_vivos = game_instance.personajes_vivos - 1
			game_instance.rondas = game_instance.rondas + 1
			print(game_instance.rondas)
			if (game_instance.personajes_vivos == 0):
				print("HAS PERDIDO ")
				game_instance.actual_stage = game_instance.actual_stage + 1
				Finish_Game = True
			elif (game_instance.enemigos_vivos == 0 and game_instance.actual_stage == int(stages)):
				print("HAS GANADO")
				game_instance.actual_stage = game_instance.actual_stage + 1
				Finish_Game = True
			elif (game_instance.enemigos_vivos == 0):
				game_instance.actual_stage = game_instance.actual_stage + 1


#Al terminar el programa comprobar las reglas de los enemigos
