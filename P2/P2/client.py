import game
import getopt, sys, socket, protocols, json

#utilizamos -o para el puerto

#funcion para obtener argumentos por pantalla

def parse_args ():
	stages = 1
	players = 1
	port = 8080
	name = "Pedro"
	ip = '127.0.0.1'
	opts, args = getopt.getopt(sys.argv[1:], "s:p:n:o:i:", ["stages=","players=","name=", "name=", "port=", "ip="])
	for o, a in opts:
		if o in ("-s", "--stages"):
			stages = a
		elif o in ("-p", "--players"):
			players = a
		elif o in ("--name", "-n"):
			name = a
		elif o in ("--port", "-o"):
			port = a
		elif o in ("--ip", "-i"):
			ip = a
	return stages, players, name, port, ip

#funcion para comprobar si los argumentos son erroneos
def check_args (stages, players):
	correct_stages = False
	correct_players = False
	start_client = False

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
		start_client= True
		return start_client

#funciones que envia el CLIENTE al SERVIDOR

def send_join(client_socket, name):
	message = {"Type": protocols.MSG_JOIN, "Nick": name}
	msg_client = json.dumps(message).encode()
	protocols.send_one_message(client_socket, msg_client)

def send_serveroption(option, players, stages, client_socket):
	message = {"Type": protocols.MSG_SEND_SERVER_OPTION, "Option": int(option), "Players": int(players), "Stages": int(stages)}
	msg_client = json.dumps(message).encode()
	protocols.send_one_message(client_socket, msg_client)

def send_character(option, client_socket):
	message = {"Type": protocols.MSG_SEND_CHARACTER, "Option": option}
	msg_client = json.dumps(message).encode()
	protocols.send_one_message(client_socket, msg_client)

def send_charactercommand(option, client_socket):
	message = {"Type": protocols.MSG_SEND_CHARACTER_COMMAND, "Option": option}
	msg_client = json.dumps(message).encode()
	protocols.send_one_message(client_socket, msg_client)

def send_gamechoice(option, client_socket):
	message = {"Type": protocols.MSG_SEND_GAME_CHOICE, "Option": option}
	msg_client = json.dumps(message).encode()
	protocols.send_one_message(client_socket, msg_client)

def send_dc_me(client_socket):
	message = {"Type": protocols.MSG_SEND_DC_ME}
	msg_client = json.dumps(message).encode()
	protocols.send_one_message(client_socket, msg_client)

#funciones que RECIBIMOS del SERVIDOR

def manage_msgwelcome(msg_server, client_socket, name, players, stages):
	options = msg_server["Options"]
	correct_option = False
	while not correct_option :
		option = input(msg_server["Message"])
		for i in options:
			if option == str(i):
				correct_option = True
	send_serveroption(option, players, stages, client_socket)

#	msg_server = json.loads(answer.decode())

def manage_msgchoose_character(msg_server, client_socket):
	options = msg_server["Options"]
	correct_option = False
	while not correct_option :
		option = input(msg_server["Message"])
		for i in options:
			if str(option) == str(i):
				correct_option = True
	option = int(option)
	print(option)
	send_character(option, client_socket)

def manage_msgyourturn(msg_server, client_socket):
	options = msg_server["Options"]
	correct_option = False
	while not correct_option :
		option = input(msg_server["Message"])
		option = option.lower()
		for i in options:
			if str(option) == str(i):
				correct_option = True
	send_charactercommand(option, client_socket)
	

def manage_msgservermsg(msg_server, client_socket):
	message = msg_server["Message"]
	print(message)

	
def manage_msgsendgames(msg_server, client_socket):
	options = msg_server["Options"]
	correct_option = False
	while not correct_option :
		option = input(msg_server["Message"])
		for i in options:
			if int(option) == int(i):
				correct_option = True
	send_gamechoice(option, client_socket)
	#lista de opciones disponibles

def manage_msgsendvalidgame(msg_server, client_socket):
	joined = msg_server["Joined"]
	if joined:
		#hacer que se quede en espera
		print("joined")
		return False
	else:
		#cerrar el cliente
		print("not joined")
		return True

def manage_msgsendendgame(msg_server, client_socket):
	win = msg_server["Win"]
	if win:
		print("Has ganado")
	else:
		print("has perdido")
	send_dc_me(client_socket)


def manage_msgsenddcserver(msg_server, client_socket):
	reason = msg_server["Reason"]
	print(reason)
	return True

try:
	stages, players, name, port, ip = parse_args()
	start_client = check_args(stages, players)
	port = int(port)
	if (start_client):
		exit = False
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client_socket.connect((socket.gethostname(), port))
		send_join(client_socket, name)
		while not exit:
			#answer = client_socket.recv(1024)
			answer = protocols.recv_one_message(client_socket)
			msg_server = json.loads(answer.decode())
			if msg_server["Type"] == protocols.MSG_WELCOME:
					manage_msgwelcome(msg_server, client_socket, name, players, stages)
			elif msg_server["Type"] == protocols.MSG_CHOOSE_CHARACTER:
				manage_msgchoose_character(msg_server, client_socket)
			elif msg_server["Type"] == protocols.MSG_SERVER_MSG:
				manage_msgservermsg(msg_server, client_socket)
			elif msg_server["Type"] == protocols.MSG_YOUR_TURN:
				manage_msgyourturn(msg_server, client_socket)
			elif msg_server["Type"] == protocols.MSG_SEND_GAMES:
				manage_msgsendgames(msg_server, client_socket)
			elif msg_server["Type"] == protocols.MSG_SEND_VALID_GAME:
				exit = manage_msgsendvalidgame(msg_server, client_socket)
			elif msg_server["Type"] == protocols.MSG_SEND_END_GAME:
				manage_msgsendendgame(msg_server, client_socket)
				exit = True
			elif msg_server["Type"] == protocols.MSG_SEND_DC_SERVER:
				exit = manage_msgsenddcserver(msg_server, client_socket)
except:
	send_dc_me(client_socket)