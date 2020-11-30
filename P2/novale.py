	while not exit:
			user_text = input("What do you want to send: ")
			if user_text == "exit":
				exit = True
				client_socket.send(user_text.encode())
				answer = client_socket.recv(1024)
			else:
				client_socket.send(user_text.encode())
				answer = client_socket.recv(1024)
				print("Server answer: ", answer.decode())
		client_socket.close()


			while (not finish_fight):
			juego.players_turn()
		juego.enemies_turn()
		juego.rondas = juego.rondas + 1
		if (len(juego.enemies) == 0):
			finish_fight = True
		if (len(juego.characters) == 0):
			finish_fight = True
			dead_players = True
	if (dead_players or juego.stages == juego.momment_stage):
		finish_game = True
		if (dead_players):
			print("You lost the game!!! Try again")
		else:
			print("You won the game!!! Congratulations")
	return finish_game



	def players_turn(c_socket, c_address):
	global games
	global client_game
	posicion_juego = client_game[c_address]
	juego = games[posicion_juego]
	finish_turn = False
	juego.print_players_turn()
	jugador = 1
	num = 0
	while ((num < len(juego.characters))and (len(juego.enemies) > 0) and not finish_turn):
		message = (type(juego.characters[num]).__name__+" (Player "+ str(jugador)+") .""What are you going to do?: ")
		option = ['a', 's']
		msg = {"Type": protocols.MSG_YOUR_TURN, "Message": message, "Options": option}

		damage, cura, charac = juego.eleccion_attack(num, jugador)
		if (charac == 's' and (type(juego.characters[num]).__name__ == "Procrastinator")):
			juego.hit_all_enemies(num, damage)
		elif (damage > 0):
			juego.hit_an_enemy(num, damage)
		elif (damage == 0 and cura == 0):
			print(type(juego.characters[len(juego.characters)-1]).__name__+" has returned to the game")
		else:
			juego.choose_heal(cura)
		num = num + 1
		jugador = jugador + 1

def fight(c_socket, c_address):
	global games
	global client_game
	posicion_juego = client_game[c_address]
	juego = games[posicion_juego]
	finish_fight = False
	dead_players = False
	finish_game = False
	message = juego.update_stage()
	msg_tosend = {"Type": protocols.MSG_SERVER_MSG, "Message": message}
	c_socket.send(json.dumps(msg_tosend).encode())
	while (not finish_fight):
		juego.players_turn()
		juego.enemies_turn()
		juego.rondas = juego.rondas + 1
		if (len(juego.enemies) == 0):
			finish_fight = True
		if (len(juego.characters) == 0):
			finish_fight = True
			dead_players = True
	if (dead_players or juego.stages == juego.momment_stage):
		finish_game = True
		if (dead_players):
			print("You lost the game!!! Try again")
		else:
			print("You won the game!!! Congratulations")
	return finish_game




	game_instance = game.Game(players, stages)
	correct_key = False
	global id
	global games
	global client_game
	id = id + 1
	aux = id
	while not correct_key:
		if aux in games:
			aux -= 1
		else:
			correct_key = True
	games[aux] = game_instance
	games = sorted(games.items())
	client_game[c_address] = aux
	print(client_game)





		game_instance = game.Game(players, stages)
	global id
	global games
	global client_game
	id = id + 1
	games[id] = game_instance
	client_game[c_address] = id