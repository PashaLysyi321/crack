from PIL import Image, ImageDraw
from random import randint 
import matplotlib.pyplot as plt


def random_with_N_digits(n): 

 	range_start = 10**(n-1) 
 	range_end = (10**n)-1 
 	return randint(range_start, range_end) 

def centre_k(x_string, size):

	length = len(x_string)
	k = length % 6

	if k == 0:
		center = (size/2, size/2)
	elif k == 1:
		center = (size/2 + int(x_string[0]), size/2)
	elif k == 2:
		center = (size/2, size/2 + int(x_string[0:2]))
	elif k == 3:
		center = (size/2 + int(x_string[0:2]), size/2 + int(x_string[3]))
	elif k == 4:
		center = (size/2 - int(x_string[0:2]), size/2 + int(x_string[2:4]))	
	else:
		center = (size/2 + int(x_string[0:3]), size/2 - int(x_string[3:5]))

	return [k,center]

def crack(x):

	#розмір вікна
	size = 1000
	x_string = str(x) #строковий тип
	
	[k, center] = centre_k(x_string, size)

	part = []

	for i in range(k,len(x_string),3):
		part.append(x_string[i:i+3])


	part = [int(i) for i in part] #конвертація в інт

	print('part is')
	print( part)

	image = Image.new('RGB', (size,size), 'white')
	draw = ImageDraw.Draw(image)

	center = (size/2, size/2)

	#малюємо лінії
	for i in range(0,len(part)-1,2):

		draw.line((center, part[i], part[i+1]), fill="black", width = int(i/2))
		print(part[i], part[i+1])

	image.show()

	#збереженя
	image.save("C:/Users/lysyi/Desktop/work/glass/test.ets",  "EPS")
	image.save("C:/Users/lysyi/Desktop/work/glass/test.pdf",  "PDF")

def check():

	size = 1000
	for i in range(0, 1000):

		print(i)
		#center = (size/2, size/2)
		center = (size/2 + random_with_N_digits(1), size/2)
		plt.scatter(center[0],center[1], s=10, c='yellow')

		center = (size/2, size/2 + random_with_N_digits(2))
		plt.scatter(center[0],center[1], s=10, c='black')

		center = (size/2 + random_with_N_digits(2), size/2 + random_with_N_digits(1))
		plt.scatter(center[0],center[1], s=10, c='blue')

		center = (size/2 - random_with_N_digits(2), size/2 + random_with_N_digits(2))	
		plt.scatter(center[0],center[1], s=10, c='red')

		center = (random_with_N_digits(3), size - 300 - random_with_N_digits(2))
		plt.scatter(center[0],center[1], s=10, c='cyan')


	plt.show()


if __name__ == "__main__":

    #x = 2**128 - 1
    x =  random_with_N_digits(30) 
    print('x is ' + str(x))
    crack(x)