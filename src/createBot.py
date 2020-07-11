import pyautogui as py
from zona import Zona
import keyboard
import time

def afisareMeniu():
	print(' 1 - Adauga punct pentru click')
	print(' 2 - Click dreapta')
	print(' 3 - Adauga text (prima interogare va fi unde sa dea click pt a scrie')
	print(' Eventuri:')
	print(' 4 - Adauga zona de verificat hover')
	print(' 5 - Adauga pauza pana la keypress')

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
	return Zona(coordonate)

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

def adaugaText():
	return input('Text de adaugat: ')

def main(numeBot=""):
	
	if numeBot == "":
		numeBot = input('Cum se numeste bot-ul?\n')
	
	file = open('boti\\' + numeBot + '.csv', 'w+')

	while True:
		afisareMeniu()
		
		x = input('Alege actiune: ')
		if x not in ['1', '2', '3', '4', '5', 'q']:
			print('\nInput incorect!\n')
			continue

		if x == '1' or x == '3':# x == '3' pentru a stii unde sa introduc text
			pos = adaugaPunctClick()
			file.write('c,{},{}\n'.format(pos[0], pos[1]))
		
		if x == '2':
			pos = adaugaPunctClick()
			file.write('d,{},{}\n'.format(pos[0], pos[1]))

		if x == '3':
			file.write('s,{}\n'.format(adaugaText()))

		if x == '4':
			zo = adaugaZona()
			file.write('z,{},{},{},{}\n'.format(zo.xmin, zo.ymin, zo.xmax, zo.ymax))

		if x == '5':
			file.write('k,{}\n'.format(adaugaKeypress()))

		if x == 'q':
			break

	file.close()
	print("Bot creeat!")

#main()