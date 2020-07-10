import pyautogui as py
from src import zona
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
	# xmin xmax, ymin, ymax 
	zo = zona.Zona([(coordonate[0], coordonate[2]), (coordonate[1], coordonate[3])])

	while True:
		print('Hover zone \n' + str(zo))
		x, y = py.position()
		
		cond = zo.onButton(x, y)
		if cond == True:
			return


def getActions():
	#botName = input('Numele botului: ')
	botName = 'sda'
	file = open('boti/' + botName + '.csv', 'r')
	
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


py.alert('Bot running')
while py.FAILSAFE:
	getActions()