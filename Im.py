import cv2
import time

nome = input('Name of the Image? .png or .jpg included\n')
while nome[-4:] != '.png' and nome[-4:] != '.jpg':
	nome = input('Name of a valid Image? .png or .jpg included\n')

img = cv2.imread(nome)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

Dim = input("Use Photo Dimentions? Y/N (You will probably have to zoom out on CMD)")
while Dim.lower() != 'n' and Dim.lower() != 'y':
	Dim = input("Unvalid Response, Use Photo Dimentions? Y/N (You will probably have to zoom out on CMD)")

if Dim.lower() == 'n':
	DiX  = float(input('X Multiplication Dimention (0.5  = Half the X)= '))
	while DiX < 0:
		DiX  = float(input('X Multiplication Valid Dimention = '))

	DiY  = float(input('Y Multiplication Dimention (0.5  = Half the Y)= '))
	while DiY <0:
		DiY  = float(input('Y MultiplicationValid Dimention = '))

	grayX , grayY = gray.shape
	grayX , grayY = int(DiX*grayX), int(DiY*grayY)
	gray = cv2.resize(gray, (grayX, grayY))

else:
	grayX , grayY = gray.shape
	gray = cv2.resize(gray, (int(grayX),int(grayY)))

def PrintF(inp):
	if inp >= 0 and inp <= 10:
		print(' ', end='')
	elif inp > 10 and inp <= 50:
		print('.',end='')
	elif inp > 50 and inp <= 100:
		print(':',end='')
	elif inp > 100 and inp <= 150:
		print('C',end='')
	elif inp > 150 and inp <= 200:
		print('O',end='')
	elif inp > 200 and inp <= 250:
		print('#',end='')
	elif inp > 250:
		print('@',end='')

for i in range(len(gray)):
	for x in gray[i]:
		PrintF(x)
	print('\n',end='')