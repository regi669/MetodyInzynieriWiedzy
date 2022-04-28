def srednia(list1):
	sum = 0
	for x in list1:
		sum += x
	return x / len(list1)

def warjancja(list1):
	mean_avg = srednia(list1)
	sum = 0
	for x in list1:
		sum += pow((x-mean_avg),2)
	return sum / len(list1)

def odchylenie(list1):
	return pow(warjancja(list1), 1/2)