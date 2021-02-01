#Práctica realizada por Pedro Serrano Marín. Ingenieria en Sistemas de Telecomunicación
import struct

MSG_JOIN = "MSG_JOIN"
MSG_WELCOME = "MSG_WELCOME"
MSG_SEND_SERVER_OPTION = "MSG_SEND_SERVER_OPTION"
MSG_CHOOSE_CHARACTER = "MSG_CHOOSE_CHARACTER"
MSG_SEND_CHARACTER = "MSG_SEND_CHARACTER"
MSG_SERVER_MSG = "MSG_SERVER_MSG"
MSG_YOUR_TURN = "MSG_YOUR_TURN"
MSG_SEND_CHARACTER_COMMAND = "MSG_SEND_CHARACTER_COMMAND"
MSG_SEND_GAMES = "MSG_SEND_GAMES"
MSG_SEND_GAME_CHOICE = "MSG_SEND_GAME_CHOICE"
MSG_SEND_VALID_GAME = "MSG_SEND_VALID_GAME"
MSG_SEND_END_GAME = "MSG_SEND_END_GAME"
MSG_SEND_DC_ME = "MSG_SEND_DC_ME"
MSG_SEND_DC_SERVER = "MSG_SEND_DC_SERVER"

PROTOCOLS = [MSG_JOIN, MSG_WELCOME,MSG_SEND_SERVER_OPTION, MSG_CHOOSE_CHARACTER, MSG_SEND_CHARACTER, MSG_SERVER_MSG, 
			MSG_YOUR_TURN, MSG_SEND_CHARACTER_COMMAND, MSG_SEND_GAMES, MSG_SEND_GAME_CHOICE, MSG_SEND_VALID_GAME, MSG_SEND_END_GAME, 
			MSG_SEND_DC_ME, MSG_SEND_DC_SERVER]

def recvall(sock, count):
	buffer = b''
	while count:
		buffer_aux = sock.recv(count)
		if not buffer_aux:
			return None
		buffer = buffer + buffer_aux
		count = count - len(buffer_aux)
	return buffer

def send_one_message(sock, encoded_data):
	length = len(encoded_data)
	sock.sendall(struct.pack('!I', length))
	sock.sendall(encoded_data)

def recv_one_message(sock):
	length_buffer = recvall(sock, 4)
	length, = struct.unpack('!I', length_buffer)
	return recvall(sock, length)
