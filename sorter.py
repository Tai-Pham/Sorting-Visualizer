import random
from matplotlib import pyplot as plt
import matplotlib.animation as animation

#bubble sort
def bubblesort(array):
	sortedArea = len(array) - 1; #last index
	for i in range(len(array)):
		swap = False
		for j in range(len(array) - i - 1):
			yield [(sortedArea, j),array] # j is the current index and sortedArea is the start of Area already sorted
			if array[j] > array[j + 1]:
				 (array[j], array[j + 1]) = (array[j + 1], array[j])
				 swap = True
				 yield [(sortedArea, j + 1),array]			 
		sortedArea = sortedArea - 1
		if(swap == False):
			break

#selection sort
def selectionsort(array):

	for i in range(len(array) - 1):
		min = i
		for j in range(i + 1, len(array)):
			yield [(i, j),array] 
			if(array[min] > array[j]):
				min = j
				
		yield [(i, min),array]
		(array[i], array[min]) = (array[min], array[i])
		yield [(i, min),array]

#insertion sort
def insertionsort(array):
	
	for i in range(len(array)):
		j = i
		
		while(j > 0 and array[j] < array[j-1]):
			(array[j], array[j-1]) = (array[j-1], array[j])
			j = j - 1
			yield [(j - 1, j), array]
		
		yield [(j, i), array]
				
#quick sort
def quicksort(array, start, end):
	if(start >= end):
		return
		
	wall = start
	for i in range(start, end - 1):
		yield [(wall , i), array]
		if (array[i] < array[end - 1]):
			array[wall], array[i] = array[i], array[wall]
			yield [(wall , i), array]
			wall = wall + 1
	array[wall], array[end - 1] = array[end - 1], array[wall]
	yield [(wall , wall), array]
	
	yield from quicksort(array, start, wall)
	yield from quicksort(array, wall + 1, end)

#merge sort
def mergesort(array, left, right):
	if(right <= left):
		return

	middle = (right + left)//2
	
	yield from mergesort(array, left, middle)
	yield from mergesort(array, middle + 1, right)
	yield from merge(array, left, middle, right)
	yield [(right, right), array]

def merge(original, left, middle, right):
	temp = []
	
	leftStart = left
	rightStart = middle + 1
	
	while(leftStart <= middle and rightStart <= right):
		if(array[leftStart] < array[rightStart]):
			temp.append(array[leftStart])
			leftStart += 1
		else:
			temp.append(array[rightStart])
			rightStart += 1
	
	while(leftStart <= middle):
		temp.append(array[leftStart])
		leftStart += 1
	
	while(rightStart <= right):
		temp.append(array[rightStart])
		rightStart += 1
	
	for i, value in enumerate(temp):
		array[left + i] = value
		yield [(left + i,left + i), array]


#used to update the graph
def update_graph(update_data, recOfBar):
	for r, val in zip(recOfBar,update_data[1]):
		r.set_height(val)
		r.set_color("b")
		
	recOfBar[update_data[0][0]].set_color('g')
	recOfBar[update_data[0][1]].set_color('r')

	

#generate a random array
size = int(input("Enter the size of the array: "))
array = [random.randint(1, 50) for _ in range(size)] #random number from 1 to 50 in the array

#select the algorithm to used
option = int(input("1 for Bubble Sort, 2 for Selection Sort, 3 for Insertion Sort, 4 for Quick Sort, or 5 for Merge Sort: "))
sorter = None

if(option == 1):
	sorter = bubblesort(array)
elif(option == 2):
	sorter = selectionsort(array)
elif(option == 3):
	sorter = insertionsort(array)
elif(option == 4):
	sorter = quicksort(array, 0, size)
elif(option == 5):
	sorter = mergesort(array, 0, size - 1)


#setup figure
fig, ax = plt.subplots()
recOfBar = ax.bar(range(len(array)), array) #(x axis, y axis)


ani = animation.FuncAnimation(fig, func = update_graph, fargs = (recOfBar,), frames=sorter, interval=1, repeat=False)
plt.show()




