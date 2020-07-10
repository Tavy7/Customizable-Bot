import pyautogui as py
from src import zona
import keyboard
import time

def afisareMeniu():
	print(' 1 - Adauga punct pentru click')
	print('~ Eventuri:')
	print(' 2 - Adauga zona de verificat hover')
	print(' 3 - Adauga pauza pana la keypress')

	print('\nApasa q pentru iesire.')

def adaugaZona():
	coordonate = []
	print('Selecteaza coltul din NW si cel din SE.')
	print('Apasa f cand mouse-ul e in pozitie pentru a memora coordonata.')

	#memoreaza coltul NW, ce contine (xmin, ymin) si coltul SE (xmax, ymax)
	while len(coordonate) < 2:
		pos = py.position()

		if keyboard.is_pressed('f'):
			time.sleep(0.5)# sleep pentru a nu da append de mai multe ori
			coordonate.append(pos)
			continue

	print('\n\nZona memorata.')
	return zona.Zona(coordonate)

def adaugaPunctClick():
	print('Apasa f cand mouse-ul e in pozitie pentru a memora coordonata.')

	while True:
		pos = py.position()
		print(pos)

		if keyboard.is_pressed('f'):
			print('\n\nZona memorata')
			return pos

def adaugaKeypress():
	return input('Key: ')

def main():
	numeBot = input('Cum se numeste bot-ul?\n')
	file = open('boti\\' + numeBot + '.csv', 'a+')

	while True:
		afisareMeniu()
		
		x = input('Alege actiune: ')
		if x not in ['1', '2', '3', 'q']:
			print('\nInput incorect!\n')
			continue

		if x == '1':
			print("12")
			pos = adaugaPunctClick()
			file.write('c,{},{}\n'.format(pos[0], pos[1]))

		if x == '2':
			zo = adaugaZona()
			file.write('z,{},{},{},{}\n'.format(zo.xmin, zo.xmax, zo.ymin, zo.ymax))

		if x == '3':
			file.write('k,{}\n'.format(adaugaKeypress()))

		if x == 'q':
			break

	file.close()
	print("Bot creeat!")

main()