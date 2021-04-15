import cv2
import time

nome = input('Nome da foto? .png ou .jpg incluido')
img = cv2.imread(nome)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayX , grayY = gray.shape
gray = cv2.resize(gray, (int(grayX),int(grayY/3)))

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