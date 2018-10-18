from vjoy import vj
import numpy as np
import select,socket,struct,time

server="192.168.0.22"
port=1964

buttons=0
stickX=0
stickY=0
dpadX=0
dpadY=0

def color(num):
	return ""
	
def sendUpdate():
	vj.update(vj.generateJoystickPosition( lButtons = buttons,  wAxisX = stickX + 16384, wAxisY = stickY + 16384, wAxisXRot = dpadX/2+16384, wAxisYRot = dpadY/2+16384 ))

vj.open()

while True:
	s = socket.socket()
	s.settimeout(10)
	
	isConnected = False
	try:
		s.connect((server, port))
		isConnected = True
		while isConnected:
			ready = select.select([s], [], [], 3)
			if ready[0]:
				try:
					event = s.recv(8)
					unpacked=struct.unpack("Ihbb",event)
					value=unpacked[1]
					type=unpacked[2]
					number=unpacked[3]
					if type == 1: #Button
						if value == 1:
							buttons=buttons + (1 << (number))
							if buttons < 0:
								buttons = 0
						else:
							buttons=buttons - (1 << (number))
							if buttons < 0:
								buttons = 0
					if type == 2: #Axis
						if number == 0:
							stickX = value
						if number == 1:
							stickY = value
						if number == 2:
							dpadX = value
						if number == 3:
							dpadY = value
					sendUpdate()
				except socket.timeout, exc:
					isConnected = False
				continue

	except socket.timeout, exc: 
		isConnected = False
	except socket.error, exc:
		isConnected = False
vj.close()