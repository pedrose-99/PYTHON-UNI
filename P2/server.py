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

def manage_msgsendgames(players, stages, c_socket, c_address):
	gme = ""
	game_vacio = 0
	for i in range(1, len(games)+ 1):
		if not games[i].lleno:
			game_vacio +=1
			print("game_vacio = ", game_vacio)
			gme = gme+str(i)+".- Players: "+str(len(games[i].characters))+"/"+str(games[i].players+"\n")
	if game_vacio != 0:
		msg = "Available games\n"+str(gme)+"\nChoose one option:"
		message = {"Type": protocols.MSG_SEND_GAMES, "Message": msg, "Options":list(range(1, game_vacio + 1))}
		c_socket.send(json.dumps(message).encode())
	else:
		print("pepe")
		create_game(players, stages, c_socket, c_address)

def manage_msgsendvalidgame(c_socket, joined):
	reply_msg = {"Type": protocols.MSG_SEND_VALID_GAME, "Joined": joined}
	c_socket.send(json.dumps(reply_msg).encode())

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
		manage_msgsendvalidgame(c_socket, False)
	else:
		#print("unirse al juego")
		print("(JOIN) ", str(name)," joined a game")
		client_game[c_address] = i
		manage_msgsendvalidgame(c_socket, True)
		manage_msgchoosecharacter(c_socket, c_address)

def join_game(players, stages, c_socket, c_address):
	global id
	global games
	global client_game
	if id == 0:
		create_game(players, stages, c_socket, c_address)
	else:
		manage_msgsendgames(players, stages, c_socket, c_address)

def delete_game(c_address):
	global id
	global games
	global client_game
	posicion_juego = client_game[c_address]
	del client_game[c_address]
	del games[posicion_juego]
	id -= 1
	

def game_main(c_socket, c_address):
	global games
	global client_game
	posicion_juego = client_game[c_address]
	player_game = games[posicion_juego]
	player_socket = player_game.sockets[player_game.current_turn]
	manage_yourturn(player_socket)


def send_damage(damage, player_game):
	for i in range (0, len(player_game.sockets)):
	#	if i != player_game.current_turn:
		msg = {"Type": protocols.MSG_SERVER_MSG, "Message": damage}
		cl_socket = player_game.sockets[i]
		cl_socket.send(json.dumps(msg).encode())

def send_update_stage(player_game):
	player_game.current_turn = 0
	mes = player_game.update_stage()
	for i in range (0, len(player_game.sockets)):
	#player_game.sockets[i].send(("Type": protocols.SERVER_MSG, "message": "a por otro game" #new_stage_info))
		msg = {"Type": protocols.MSG_SERVER_MSG, "Message": mes}
		cl_socket = player_game.sockets[i]
		cl_socket.send(json.dumps(msg).encode())
	player_socket = player_game.sockets[player_game.current_turn]
	manage_yourturn(player_socket)
#send_character_comand

def send_end_game(player_game, win):
	for i in range (0, len(player_game.sockets)):
		#player_game.sockets[i].send(("Type": protocols.END_GAME, "message": "GANASTE"))
		msg = {"Type": protocols.MSG_SEND_END_GAME, "Win": win}
		cl_socket = player_game.sockets[i]
		cl_socket.send(json.dumps(msg).encode())

def send_enemies_damage(player_game):
	dam = player_game.enemies_turn()
	print (dam)
	for i in range (0, len(player_game.sockets)):
		msg = {"Type": protocols.MSG_SERVER_MSG, "Message": dam}
		cl_socket = player_game.sockets[i]
		cl_socket.send(json.dumps(msg).encode())				
		player_game.current_turn = 0

def send_player_turn(player_game):
	dam = player_game.print_players_turn()
	print (dam)
	for i in range (0, len(player_game.sockets)):
		msg = {"Type": protocols.MSG_SERVER_MSG, "Message": dam}
		cl_socket = player_game.sockets[i]
		cl_socket.send(json.dumps(msg).encode())				
		player_game.current_turn = 0

def manage_msgsendcharactercommand(msg_client, c_socket, c_address):
	end = False
	posicion_juego = client_game[c_address]
	player_game = games[posicion_juego]
	player_socket = player_game.sockets[player_game.current_turn]
	command = msg_client['Option']#a o s
	damage = player_game.players_turn(command)
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
		if player_game.current_turn == len(player_game.characters):
			send_enemies_damage(player_game)
			if player_game.characters_dead():
				send_end_game(player_game, False)
				end = True
			else:
				send_player_turn(player_game)
				player_socket = player_game.sockets[player_game.current_turn]
				manage_yourturn(player_socket)
		else:
			player_socket = player_game.sockets[player_game.current_turn]
			manage_yourturn(player_socket)
	return end



def create_game(players, stages, c_socket, c_address):
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
	#games = sorted(games.items())
	client_game[c_address] = aux
	print(client_game)
	manage_msgchoosecharacter(c_socket, c_address)

#
#
#
#
#mensajes que el cliente envia al servidor
def manage_msgjoin(msg_client, c_socket):
	name = msg_client["Nick"]
	print("WELCOME ", str(name), "joined the server")
	manage_msgwelcome(c_socket)
	return name

def	manage_msgsendserveroption(msg_client, c_socket, c_address, name):
	option = msg_client["Option"]
	option = int(option)
	players = msg_client["Players"]
	stages = msg_client["Stages"]
	if option == 1:
		print("(CREATE) ", str(name), " created a game.") 
		create_game(players, stages, c_socket, c_address)
	elif option == 2:
		#join a game
		join_game(players, stages, c_socket, c_address)
	elif option == 3:
		print("exit")

def manage_msgsendcharacter(msg_client, c_socket, c_address):
	option = int(msg_client["Option"])
	global games
	global client_game
	posicion_juego = client_game[c_address]
	juego = games[posicion_juego]
	juego.add_player(option, c_socket)
	if int(juego.players) != len(juego.characters):
		message = "Waiting for other players to join the game"
		manage_msgservermsg(message, c_socket, c_address)
	else:
		juego.lleno = True
		mon = juego.update_stage()
		man = juego.print_players_turn()
		mon = mon+"\n"+man
		for i in range (0, len(juego.sockets)):
			msg = {"Type": protocols.MSG_SERVER_MSG, "Message": mon}
			cl_socket = juego.sockets[i]
			cl_socket.send(json.dumps(msg).encode())
		game_main(c_socket, c_address)


def manage_msgsenddcme(msg_client, c_socket):
	print("hay q apagar eto")
#
#
#
#
#mensajes que envia el servidor al cliente
def manage_msgwelcome(c_socket):
	set_options = "Welcome to the server. Choose one of this options\n	1.- Create game\n	2.- Join game \n	3.- Exit\n   Your Option: "
	reply_msg = {"Type": protocols.MSG_WELCOME, "Message": set_options, "Options": list(range(MIN_OPTION, MAX_OPTION))}
	c_socket.send(json.dumps(reply_msg).encode())

def manage_msgchoosecharacter(c_socket, c_address):
	global games
	global client_game
	posicion_juego = client_game[c_address]
	juego = games[posicion_juego]
	datos = juego.print_all_characters()
	message = {"Type": protocols.MSG_CHOOSE_CHARACTER,"Message": datos+"\nchoose a character:", "Options": list(range(MIN_CHARACTER, MAX_CHARACTER))}
	c_socket.send(json.dumps(message).encode())


def manage_yourturn(c_socket):
	lista = ['a', 's']
	reply_msg = {"Type": protocols.MSG_YOUR_TURN, "Message": "What are you going to do?: ", "Options": lista}
	c_socket.send(json.dumps(reply_msg).encode())

def manage_msgservermsg(message, c_socket, c_address):
	reply_msg = {"Type": protocols.MSG_SERVER_MSG, "Message": message}
	c_socket.send(json.dumps(reply_msg).encode())





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
			manage_msgsendserveroption(msg_client, c_socket, self.client_address, self.name)
		elif msg_client["Type"] == protocols.MSG_SEND_CHARACTER:
			manage_msgsendcharacter(msg_client, c_socket, self.client_address)
		elif msg_client["Type"] == protocols.MSG_SEND_CHARACTER_COMMAND:
			self.end = manage_msgsendcharactercommand(msg_client, c_socket, self.client_address)
		elif msg_client["Type"] == protocols.MSG_SEND_GAME_CHOICE:
			manage_msgsendgamechoice(msg_client, c_socket, self.client_address, self.name)
		elif msg_client["Type"] == protocols.MSG_SEND_DC_ME:
			manage_msgsenddcme(msg_client, c_socket)
	
	def run(self):
		#print("\nConection established: ", self.client_address)
		while not self.end:
			try:
				message = self.client_socket.recv(1024)
				msg_client = json.loads(message.decode())
				#print("Message received: ", message.decode())
				#reply = "holaholacaracola"
				self.manage_msg(msg_client, self.client_socket)
			#	self.client_socket.send(reply.encode())
			except ConnectionAbortedError:
				print("connection closed by the user")
				self.end = True
		delete_game(self.client_address)
		#print(games)
		#print(client_game)

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