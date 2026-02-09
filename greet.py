def greet(array,i = 0):
	if i == len(array):
		return ""
	return f"Hello {array[i]}\n{greet(array,i+1)}"
	
persons = ['majed','fahmida','sayem','bushra','ruamana']
print(greet(persons))	

