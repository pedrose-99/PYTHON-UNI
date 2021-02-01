#Práctica realizada por Pedro Serrano Marín. Ingenieria en Sistemas de Telecomunicación
import game
import getopt, sys, socket, protocols,json
import threading
import os
import signal
import doublylinkedlist

#Constantes y variables globales

MIN_OPTION = 1
MAX_OPTION = 4
MIN_CHARACTER = 1
MAX_CHARACTER = 5

game_finished = 0
cursor = doublylinkedlist.Cursor(doublylinkedlist.DoublyLinkedList())

#funcion para obtener argumentos
def parse_args ():
	port = 8080
	opts, args = getopt.getopt(sys.argv[1:],"p:", ["port="])
	for o, a in opts:
		if o in ("-p", "--port"):
			port = int(a)
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
	game_instance = game.Game(players, stages)
	game_instance.add_c_address(c_address)
	cursor.iterable.insert_last(game_instance)
	print("(CREATE) "+str(name)+" created a game.")
	send_choosecharacter(c_socket, c_address, game_instance)


#funcion unirse a juego
def join_game(players, stages, c_socket, c_address, name):
	cursor.first()
	game = cursor.empty()
	if game is None:
		create_game(players, stages, c_socket, c_address, name)
	else:
		send_sendgames(players, stages, c_socket, c_address, name)

#funcion borrar juego y clientes
def delete_clients_and_game(c_address, name):
	global game_finished
	try:
		game_finished +=1
		game = find_game(c_address)
		cursor.iterable.delete_node(game)
	except KeyError:
		pass
	
#funcion para iniciar el juego
def init_game(c_socket, c_address, juego):
	dam = ""
	for i in juego.client_info['client_names']:
		j = str(i)
		dam = dam+j+" "
	print("(START) "+dam+"started a game")
	player_socket = juego.client_info['client_sockets'][juego.current_turn]
	send_yourturn(player_socket)

#funcion para encontrar el juego

def find_game(c_address):
	cursor.first()
	aux_game = cursor.get()
	while aux_game != None:
		i = 0
		while i < len(aux_game.client_info['client_addresses']):
			if aux_game.client_info['client_addresses'][i] == c_address:
				return aux_game
			else:
				i+=1
		cursor.next()
		aux_game = cursor.get()

#funciones para ENVIAR mensajes SERVIDOR al CLIENTE

def send_welcome(c_socket, name):
	print("(WELCOME)", str(name), "joined the server")
	set_options = "Welcome to the server. Choose one of this options\n	1.- Create game\n	2.- Join game \n	3.- Exit\nYour Option: "
	message = {"Type": protocols.MSG_WELCOME, "Message": set_options, "Options": list(range(MIN_OPTION, MAX_OPTION))}
	msg_client = json.dumps(message).encode()
	protocols.send_one_message(c_socket, msg_client)

def send_choosecharacter(c_socket, c_address, juego):
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
	cursor.first()
	game_pointer = cursor.empty()
	game_vacio = 0
	i = 1
	while game_pointer:
		game = cursor.get()
		if not game.game_full and len(game.characters) > 0:
			game_vacio +=1
			gme = str(gme)+str(i)+".- Players: "+str(len(game.characters))+"/"+str(game.players)+"\n"
			i+=1
		cursor.next()
		game_pointer = cursor.empty()
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
	for i in range (0, len(player_game.client_info['client_sockets'])):
		msg = {"Type": protocols.MSG_SERVER_MSG, "Message": damage}
		cl_socket = player_game.client_info['client_sockets'][i]
		msg_client = json.dumps(msg).encode()
		protocols.send_one_message(cl_socket, msg_client)

def send_update_stage(player_game):
	player_game.current_turn = 0
	mes = player_game.update_stage()
	for i in range (0, len(player_game.client_info['client_sockets'])):
		msg = {"Type": protocols.MSG_SERVER_MSG, "Message": mes}
		cl_socket = player_game.client_info['client_sockets'][i]
		msg_client = json.dumps(msg).encode()
		protocols.send_one_message(cl_socket, msg_client)

def send_end_game(player_game, win):
	dam = ""
	for i in player_game.client_info['client_names']:
		dam = dam+i+" "
	if win:
		print("(GAMEEND)"+dam+"game ended. They won.")
	else:
		print("(GAMEEND)"+dam+"game ended. They lost.")
	for i in range (0, len(player_game.client_info['client_sockets'])):
		msg = {"Type": protocols.MSG_SEND_END_GAME, "Win": win}
		cl_socket = player_game.client_info['client_sockets'][i]
		msg_client = json.dumps(msg).encode()
		protocols.send_one_message(cl_socket, msg_client)

def send_enemies_damage(player_game):
	dam = player_game.enemies_turn()
	for i in range (0, len(player_game.client_info['client_sockets'])):
		msg = {"Type": protocols.MSG_SERVER_MSG, "Message": dam}
		cl_socket = player_game.client_info['client_sockets'][i]
		msg_client = json.dumps(msg).encode()
		protocols.send_one_message(cl_socket, msg_client)				
	player_game.current_turn = 0

def send_player_turn(player_game):
	dam = player_game.print_players_turn()
	for i in range (0, len(player_game.client_info['client_sockets'])):
		msg = {"Type": protocols.MSG_SERVER_MSG, "Message": dam}
		cl_socket = player_game.client_info['client_sockets'][i]
		msg_client = json.dumps(msg).encode()
		protocols.send_one_message(cl_socket, msg_client)	
		player_game.current_turn = 0

def send_dc_server_exit(c_socket, mg):
	msg = {"Type": protocols.MSG_SEND_DC_SERVER, "Reason": mg}
	msg_client = json.dumps(msg).encode()
	protocols.send_one_message(c_socket, msg_client)

def send_dc_server_dc():
	mg = "The server has been shut down. The game finished. Nobody wins."
	msg = {"Type": protocols.MSG_SEND_DC_SERVER, "Reason": mg}
	msg_client = json.dumps(msg).encode()
	cursor.first()
	game = cursor.get()
	while game != None:
		data_game = game.data
		for socket in data_game.client_info['client_sockets']:
			protocols.send_one_message(socket, msg_client)
		cursor.next()
		game = cursor.get()

#mensajes que el cliente envia al servidor

def manage_msgjoin(msg_client, c_socket):
	name = msg_client["Nick"]
	send_welcome(c_socket, name)
	return name

def	manage_msgsendserveroption(msg_client, c_socket, c_address, name):
	option = msg_client["Option"]
	end = False
	option = int(option)
	players = msg_client["Players"]
	stages = msg_client["Stages"]
	if option == 1:
		create_game(players, stages, c_socket, c_address, name)
	elif option == 2:
		join_game(players, stages, c_socket, c_address, name)
	elif option == 3:
		print("(EXIT)", name, " disconnected.")
		send_dc_server_exit(c_socket, "You ended the conexion.")
		end = True
	return end

def manage_msgsendcharacter(msg_client, c_socket, c_address, name):
	option = int(msg_client["Option"])
	juego = find_game(c_address)
	if not juego.game_full:
		if len(juego.characters) > 0:
			print("(JOIN) "+str(name)+" joined a game")
		juego.add_player(option, c_socket, name)
		if int(juego.players) != len(juego.characters):
			message = "Waiting for other players to join the game"
			send_servermsg(message, c_socket, c_address)
		else:
			juego.game_full = True
			mon = str(juego.update_stage())
			man = str(juego.print_players_turn())
			mon = str(mon+"\n"+man)
			for i in juego.client_info['client_sockets']:
				msg = {"Type": protocols.MSG_SERVER_MSG, "Message": mon}
				cl_socket = i
				msg_client = json.dumps(msg).encode()
				protocols.send_one_message(cl_socket, msg_client)
			init_game(c_socket, c_address, juego)
	else:
		print(name,"could not join the game.")
		send_sendvalidgame(c_socket, False)

def manage_msgsendcharactercommand(msg_client, c_socket, c_address, name):
	end = False
	player_game = find_game(c_address)
	command = msg_client["Option"]
	damage, next, message = player_game.players_turn(command, name)
	if not next:
		send_servermsg(message,c_socket,c_address)
		send_yourturn(c_socket)
	else:
		send_damage(damage, player_game)
		if player_game.monsters_dead():
			if int(player_game.momment_stage) != int(player_game.stages):
				send_update_stage(player_game)
				send_player_turn(player_game)
				dead_player_turn(player_game)
				send_yourturn(player_game.client_info['client_sockets'][player_game.current_turn])
			else:
				send_end_game(player_game, True)
				end = True
				delete_clients_and_game(c_address, name)
		else:
			player_game.next_turn()
			dead_player_turn(player_game)
			if player_game.current_turn >= len(player_game.characters):
				send_enemies_damage(player_game)
				if player_game.characters_dead():
					send_end_game(player_game, False)
					end = True
					delete_clients_and_game(c_address, name)
				else:
					send_player_turn(player_game)
					dead_player_turn(player_game)
					send_yourturn(player_game.client_info['client_sockets'][player_game.current_turn])
			else:
				dead_player_turn(player_game)
				send_yourturn(player_game.client_info['client_sockets'][player_game.current_turn])
	return end

def dead_player_turn(player_game):
	i = 0
	while i < len(player_game.dead_turns):
		if player_game.dead_turns[i] == (player_game.current_turn):
			player_game.next_turn()
			i = 0
		else:
			i+=1

def manage_msgsendgamechoice(msg_client, c_socket, c_address, name):
	option = int(msg_client["Option"])
	cursor.first()
	game = cursor.get()
	game_pointer = cursor.empty()
	gme = 1
	correct_game = False
	while (not correct_game and game_pointer != None):
		if (game.game_full):
			cursor.next()
			game_pointer = cursor.empty()
			if game_pointer:
				game = cursor.get()
		else:
			if gme == option:
				correct_game = True
			else:
				cursor.next()
				game = cursor.get()
				game_pointer = cursor.empty()
				gme +=1
	if game_pointer == None:
		send_sendvalidgame(c_socket, False)
	else:
		send_sendvalidgame(c_socket, True)
		game.add_c_address(c_address)
		send_choosecharacter(c_socket, c_address, game)

def manage_msgsenddcme(msg_client, c_socket, c_address, name):
	try:
		player_game = find_game(c_address)
		mon = name+" disconnected. The game can not continue."
		print("(EXIT) "+name+" disconnected.")
		for i in range (0, len(player_game.client_info['client_sockets'])):
			msg = {"Type": protocols.MSG_SEND_DC_SERVER, "Reason": mon}
			cl_socket = player_game.client_info['client_sockets'][i]
			msg_client = json.dumps(msg).encode()
			if cl_socket != c_socket:
				print("(DC) "+player_game.client_info['client_names'][i]+ " was disconnected.")
				protocols.send_one_message(cl_socket, msg_client)
		delete_clients_and_game(c_address, name)
		return True
	except KeyError:
		return True

#funciones para el servidor
def number_games():
	n_games = 0
	cursor.first()
	game_pointer = cursor.empty()
	while game_pointer != None:
		game = cursor.get()
		if game.game_full:
			n_games +=1
		cursor.next()
		game_pointer = cursor.empty()
	return n_games

def ngames():
	global game_finished
	n_games = number_games()
	print("Active games:",n_games)
	print("Finished games:",game_finished)

def games_info():
	global cursor
	cursor.last()
	game_pointer = cursor.empty()
	while game_pointer != None:
		game = cursor.get()
		if game.game_full:
			game.print_game_stats()
		cursor.prev()
		game_pointer = cursor.empty()

def server_command(msg, exit):
	if msg == "shutdown":
		print("The server has been closed by the admin.")
		exit = True
		os.kill(pid, signal.SIGTERM)
	elif msg == "gamesinfo":
		games_info()
	elif msg == "ngames":
		ngames()
	else:
		print("The command you have requested does not exist. The existing commands are ngames, gamesinfo and shutdown")

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
		while not self.end:
			try:
				message = protocols.recv_one_message(self.client_socket)
				if message:
					msg_client = json.loads(message.decode())
					self.manage_msg(msg_client, self.client_socket)
				else:
					self.end = True
			except :
				self.end = True
		

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
			client_socket, client_address = self.server_socket.accept()
			client_thread = ClientThread(client_socket, client_address)
			client_thread.start()

try:
	pid = os.getpid()
	port = parse_args()
	start_game = check_args(port)
	port = int(port)
	exit = False
	if (start_game):
		server_socket_thread = ServerSocketThread(port)
		server_socket_thread.start()
		print("The socket is listening.")
		while not exit:
			msg = input()
			server_command(msg, exit)
except KeyboardInterrupt:
	os.kill(pid,signal.SIGTERM)
except:
	send_dc_server_dc()