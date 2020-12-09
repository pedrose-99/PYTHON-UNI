import game
import getopt, sys, socket, protocols,json
import threading
import os

MIN_OPTION = 1
MAX_OPTION = 4
MIN_CHARACTER = 1
MAX_CHARACTER = 5

id = 0
#Game = {1 : Game(), 2: Game()}
games = {}
#client_game = {(127.0.0.1, 6123): 1, (127.0.0.1, 6124): 2}
client_game = {}

#funcion para obtener argumentos

def parse_args ():
	port = 8080
	opts, args = getopt.getopt(sys.argv[1:],"port:", ["port="])
	for o, a in opts:
		if o in ("-port", "--port"):
			port = a
	return port

#funcion para comprobar si los argumentos son erroneos

def check_args (port):
	start_game = False
	try:
		port = int(port)
		start_game = True
	except ValueError:
		print("The value given must be an integer number.")
	return start_game

#funcion crear juego

def create_game(players, stages, c_socket, c_address, name):
	global id
	global games
	global client_game
	game_instance = game.Game(players, stages)
	id = id + 1
	games[id] = game_instance
	client_game[c_address] = id
	print(client_game)
	print(games)
	send_choosecharacter(c_socket, c_address)

#funcion unirse a juego

def join_game(players, stages, c_socket, c_address, name):
	global id
	global games
	global client_game
	if id == 0:
		create_game(players, stages, c_socket, c_address, name)
	else:
		send_sendgames(players, stages, c_socket, c_address, name)

#funcion borrar juego

def delete_game(c_address, name):
	global id
	global games
	global client_game
	try:
		juego = client_game[c_address]
		for i in client_game.copy():
			if client_game[i] == juego:
				del client_game[i]
		del games[juego]
		id -= 1
		juego_copy = juego + 1
		for i in client_game.copy():
			if client_game[i] == juego_copy:
				client_game[i] = juego_copy - 1
				juego_copy+= 1
		for i in games.copy():
			print(i)
			if i == juego + 1:
				print("pasa por aqui")
				games[juego] = games[i]
				del games[i]
				juego +=1
	except KeyError:
		print("The player ",name, " ended the conexion.")
	
#funcion para iniciar el juego

def game_main(c_socket, c_address):
	global games
	global client_game
	posicion_juego = client_game[c_address]
	player_game = games[posicion_juego]
	player_socket = player_game.sockets[player_game.current_turn]
	send_yourturn(player_socket)


#funciones para ENVIAR mensajes SERVIDOR al CLIENTE

def send_welcome(c_socket):
	set_options = "Welcome to the server. Choose one of this options\n	1.- Create game\n	2.- Join game \n	3.- Exit\n   Your Option: "
	message = {"Type": protocols.MSG_WELCOME, "Message": set_options, "Options": list(range(MIN_OPTION, MAX_OPTION))}
	msg_client = json.dumps(message).encode()
	protocols.send_one_message(c_socket, msg_client)

def send_choosecharacter(c_socket, c_address):
	global games
	global client_game
	posicion_juego = client_game[c_address]
	juego = games[posicion_juego]
	datos = juego.print_all_characters()
	message = {"Type": protocols.MSG_CHOOSE_CHARACTER,"Message": datos+"\nchoose a character:", "Options": list(range(MIN_CHARACTER, MAX_CHARACTER))}
	msg_client = json.dumps(message).encode()
	protocols.send_one_message(c_socket, msg_client)

def send_yourturn(c_socket):
	lista = ['a', 's']
	message = {"Type": protocols.MSG_YOUR_TURN, "Message": "What are you going to do?: ", "Options": lista}
	msg_client = json.dumps(message).encode()
	protocols.send_one_message(c_socket, msg_client)

def send_servermsg(message, c_socket, c_address):
	message = {"Type": protocols.MSG_SERVER_MSG, "Message": message}
	msg_client = json.dumps(message).encode()
	protocols.send_one_message(c_socket, msg_client)

def send_sendgames(players, stages, c_socket, c_address, name):
	gme = ""
	game_vacio = 0
	for i in range(1, len(games)+ 1):
		if not games[i].lleno:
			game_vacio +=1
			gme = str(gme)+str(i)+".- Players: "+str(len(games[i].characters))+"/"+str(games[i].players)+"\n"
	if game_vacio != 0:
		msg = "Available games\n"+str(gme)+"\nChoose one option:"
		message = {"Type": protocols.MSG_SEND_GAMES, "Message": msg, "Options":list(range(1, game_vacio + 1))}
		msg_client = json.dumps(message).encode()
		protocols.send_one_message(c_socket, msg_client)	
	else:
		create_game(players, stages, c_socket, c_address, name)

def send_sendvalidgame(c_socket, joined):
	message = {"Type": protocols.MSG_SEND_VALID_GAME, "Joined": joined}
	msg_client = json.dumps(message).encode()
	protocols.send_one_message(c_socket, msg_client)

def send_damage(damage, player_game):
	for i in range (0, len(player_game.sockets)):
	#	if i != player_game.current_turn:
		msg = {"Type": protocols.MSG_SERVER_MSG, "Message": damage}
		cl_socket = player_game.sockets[i]
		msg_client = json.dumps(msg).encode()
		protocols.send_one_message(cl_socket, msg_client)

def send_update_stage(player_game):
	player_game.current_turn = 0
	mes = player_game.update_stage()
	for i in range (0, len(player_game.sockets)):
	#player_game.sockets[i].send(("Type": protocols.SERVER_MSG, "message": "a por otro game" #new_stage_info))
		msg = {"Type": protocols.MSG_SERVER_MSG, "Message": mes}
		cl_socket = player_game.sockets[i]
		msg_client = json.dumps(msg).encode()
		protocols.send_one_message(cl_socket, msg_client)
	player_socket = player_game.sockets[player_game.current_turn]
	send_yourturn(player_socket)
#send_character_comand

def send_end_game(player_game, win):
	for i in range (0, len(player_game.sockets)):
		#player_game.sockets[i].send(("Type": protocols.END_GAME, "message": "GANASTE"))
		msg = {"Type": protocols.MSG_SEND_END_GAME, "Win": win}
		cl_socket = player_game.sockets[i]
		msg_client = json.dumps(msg).encode()
		protocols.send_one_message(cl_socket, msg_client)

def send_enemies_damage(player_game):
	dam = player_game.enemies_turn()
	for i in range (0, len(player_game.sockets)):
		msg = {"Type": protocols.MSG_SERVER_MSG, "Message": dam}
		cl_socket = player_game.sockets[i]
		msg_client = json.dumps(msg).encode()
		protocols.send_one_message(cl_socket, msg_client)				
	player_game.current_turn = 0

def send_player_turn(player_game):
	dam = player_game.print_players_turn()
	for i in range (0, len(player_game.sockets)):
		msg = {"Type": protocols.MSG_SERVER_MSG, "Message": dam}
		cl_socket = player_game.sockets[i]
		msg_client = json.dumps(msg).encode()
		protocols.send_one_message(cl_socket, msg_client)
		player_game.current_turn = 0


#mensajes que el cliente envia al servidor

def manage_msgjoin(msg_client, c_socket):
	name = msg_client["Nick"]
	print("WELCOME ", str(name), "joined the server")
	send_welcome(c_socket)
	return name

def	manage_msgsendserveroption(msg_client, c_socket, c_address, name):
	option = msg_client["Option"]
	end = False
	option = int(option)
	players = msg_client["Players"]
	stages = msg_client["Stages"]
	if option == 1:
		print("(CREATE) ", str(name), " created a game.") 
		create_game(players, stages, c_socket, c_address, name)
	elif option == 2:
		#join a game
		join_game(players, stages, c_socket, c_address, name)
	elif option == 3:
		print("exit")
		send_dc_server_exit(c_socket, "You ended the conexion.")
		end = True
	return end

def manage_msgsendcharacter(msg_client, c_socket, c_address, name):
	option = int(msg_client["Option"])
	global games
	global client_game
	posicion_juego = client_game[c_address]
	juego = games[posicion_juego]
	if not juego.lleno:
		juego.add_player(option, c_socket, name)
		print(len(juego.characters))
		if int(juego.players) != len(juego.characters):
			message = "Waiting for other players to join the game"
			send_servermsg(message, c_socket, c_address)
		else:
			juego.lleno = True
			mon = str(juego.update_stage())
			man = str(juego.print_players_turn())
			mon = str(mon+"\n"+man)
			for i in range (0, len(juego.sockets)):
				msg = {"Type": protocols.MSG_SERVER_MSG, "Message": mon}
				cl_socket = juego.sockets[i]
				msg_client = json.dumps(msg).encode()
				protocols.send_one_message(cl_socket, msg_client)
			game_main(c_socket, c_address)
	else:
		print("No se pudo unir")
		send_sendvalidgame(c_socket, False)

def manage_msgsendcharactercommand(msg_client, c_socket, c_address, name):
	end = False
	correct_turn = False
	posicion_juego = client_game[c_address]
	player_game = games[posicion_juego]
	player_socket = player_game.sockets[player_game.current_turn]
	command = msg_client["Option"]#a o s
	print("al principio el turno es:", player_game.current_turn)
	damage, next, message = player_game.players_turn(command, name)
	if not next:
		send_servermsg(message,c_socket,c_address)
		send_yourturn(c_socket)
	else:
		send_damage(damage, player_game)
		if player_game.monsters_dead():
			#print(player_game.print_players_turn())
			if int(player_game.momment_stage) != int(player_game.stages):
				send_update_stage(player_game)
			else:
				send_end_game(player_game, True)
				end = True
		else:
			player_game.next_turn()
			print("El turno antes de cambairlo es:", player_game.current_turn)
			hay_turno_muerto(player_game)
			print("Despues de hay turno muerto el turno es de:", player_game.current_turn)
			if player_game.current_turn >= len(player_game.characters):
				send_enemies_damage(player_game)
				if player_game.characters_dead():
					send_end_game(player_game, False)
					end = True
				else:
					send_player_turn(player_game)
					print("Despues del send playerel turno es de:", player_game.current_turn)
					hay_turno_muerto(player_game)
					print("Despues de hay turno muerto 2 el turno es de:", player_game.current_turn)
					print("***************************")
					send_yourturn(player_game.sockets[player_game.current_turn])
			else:
				send_yourturn(player_game.sockets[player_game.current_turn])
				print("el turno es el ",player_game.current_turn)
	return end


def hay_turno_muerto(player_game):
	i = 0
	while i < len(player_game.turnos_muertos):
		print(i)
		if player_game.turnos_muertos[i] == (player_game.current_turn):
			player_game.next_turn()
			i = 0
		else:
			i+=1

def manage_msgsendgamechoice(msg_client, c_socket, c_address, name):
	option = int(msg_client["Option"])
	gme = 1
	i = 1
	correct_game = False
	while (correct_game and i <= len(games)):
		if (games[i].lleno):
			i +=1
		else:
			if gme == option:
				print("coso")
				correct_game = True
			else:
				i +=1
				gme +=1
	if i > len(games):
		print("No se pudo unir")
		send_sendvalidgame(c_socket, False)
	else:
		#print("unirse al juego")
		print("(JOIN) ", str(name)," joined a game")
		client_game[c_address] = i
		send_sendvalidgame(c_socket, True)
		send_choosecharacter(c_socket, c_address)


def send_dc_server_exit(c_socket, msg):
	msg = {"Type": protocols.MSG_SEND_DC_SERVER, "Reason": msg}
	msg_client = json.dumps(msg).encode()
	protocols.send_one_message(c_socket, msg_client)


def manage_msgsenddcme(msg_client, c_socket, c_address, name):
	print("hay q apagar eto")
	posicion_juego = client_game[c_address]
	player_game = games[posicion_juego]
	mon = name+" disconnected. The game can not continue."
	for i in range (0, len(player_game.sockets)):
		msg = {"Type": protocols.MSG_SEND_DC_SERVER, "Reason": mon}
		cl_socket = player_game.sockets[i]
		msg_client = json.dumps(msg).encode()
		if cl_socket != c_socket:
			protocols.send_one_message(cl_socket, msg_client)
	return True
#
#
#
#

class ClientThread(threading.Thread):
	def __init__(self, client_socket, client_address):
		threading.Thread.__init__(self)
		self.client_socket = client_socket
		self.client_address = client_address
		self.end = False
		self.name = ""

	def manage_msg(self, msg_client, c_socket):
		if msg_client["Type"] == protocols.MSG_JOIN:
			self.name = manage_msgjoin(msg_client, c_socket)
		elif msg_client["Type"] == protocols.MSG_SEND_SERVER_OPTION:
			self.end = manage_msgsendserveroption(msg_client, c_socket, self.client_address, self.name)
		elif msg_client["Type"] == protocols.MSG_SEND_CHARACTER:
			manage_msgsendcharacter(msg_client, c_socket, self.client_address, self.name)
		elif msg_client["Type"] == protocols.MSG_SEND_CHARACTER_COMMAND:
			self.end = manage_msgsendcharactercommand(msg_client, c_socket, self.client_address, self.name)
		elif msg_client["Type"] == protocols.MSG_SEND_GAME_CHOICE:
			manage_msgsendgamechoice(msg_client, c_socket, self.client_address, self.name)
		elif msg_client["Type"] == protocols.MSG_SEND_DC_ME:
			self.end = manage_msgsenddcme(msg_client, c_socket, self.client_address, self.name)
	
	def run(self):
		#print("\nConection established: ", self.client_address)
		while not self.end:
			try:
				#message = self.client_socket.recv(1024)
				message = protocols.recv_one_message(self.client_socket)
				msg_client = json.loads(message.decode())
				#print("Message received: ", message.decode())
				#reply = "holaholacaracola"
				self.manage_msg(msg_client, self.client_socket)
			#	self.client_socket.send(reply.encode())
			except ConnectionAbortedError:
				print("connection closed by the user")
				self.end = True
		delete_game(self.client_address, self.name)

class ServerSocketThread(threading.Thread):
	def __init__(self, port):
		threading.Thread.__init__(self)
		self.stop = False
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_socket.bind((socket.gethostname(), port))
		self.server_socket.listen(20)

	def run(self):
		print("Server starter at 127.0.0.1:", port)
		while True:
			#print("Waiting connection ...")
			client_socket, client_address = self.server_socket.accept()
			client_thread = ClientThread(client_socket, client_address)
			client_thread.start()

try:
	pid = os.getpid()
	port = parse_args()
	start_game = check_args(port)
	port = int(port)
	if (start_game):
		server_socket_thread = ServerSocketThread(port)
		server_socket_thread.start()
		input("socket is listening. Press enter to exit")
		os.kill(pid, -9)
except:
	print("adios don pepito")