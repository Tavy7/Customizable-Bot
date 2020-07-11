import pyautogui as py
from zona import Zona
import keyboard

py.FAILSAFE = True
py.PAUSE = 0.1

# functie de pauza pana la apasare de buton
def pauza(key):
	print('Asteptam keypress ' + key)
	while True:
		if keyboard.is_pressed(key):
			break

def hoverZone(coordonate):
	coordonate = list(map(int, coordonate))# toate elementele sunt int
	# xmin ymin, xmax, ymax 
	zo = Zona([(coordonate[0], coordonate[1]), (coordonate[2], coordonate[3])])

	while True:
		print('Hover zone \n' + str(zo))
		x, y = py.position()
		
		cond = zo.onButton(x, y)
		if cond == True:
			return

def getBot():
	import os
	bots = os.listdir('boti/')

	if len(bots) == 0:
		print('Nu exista boti')
		quit()
	
	print('Alege bot')
	cnt = 1
	for bot in bots:
		print(' {} - {}'.format(cnt, bot))
		cnt += 1

	choice = input("\n")
	
	try:
		choice = int(choice) - 1
		if choice < cnt - 1:
			return bots[choice]
		return getBot()
	except:
		print('Valoarea trebuie sa fie int')


def getActions(botName):
	file = open('boti/' + botName, 'r')
	actions = file.readlines()

	for action in actions:
		action = action.split(',')
	
		action[-1] = str(action[-1][:-1]) # stergem \n de la final

		if action[0] == 'k':# wait pana la keypress
			pauza(action[1])

		if action[0] == 'z':# wait pana la hover pe o anumita zona
			hoverZone(action[1:])

		if action[0] == 'c': # click
			print('Efectuam click la {}, {}'.format(action[1], action[2]))
			py.click(int(action[1]), int(action[2]))
		
		if action[0] == 'd': # click dr
			print('Efectuam click dreapta la {}, {}'.format(action[1], action[2]))
			py.click(int(action[1]), int(action[2]), button = 'right')
			
		if action[0] == 's': #text
			py.write(action[1])

def main():	
	py.alert('Bot running')
	botName = getBot()

	while py.FAILSAFE:
		getActions(botName)