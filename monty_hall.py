#Daxal Hemendrakumar Mehta(2013033)
import numpy as np
import random
wins=0
switch='Yes'
N=1000
chosen_door='a' #Choose the door in lower indices
doors=['a','b','c']
M=N
for i in range(N):
	ran=random.randint(0,1) 			# ran=0 for Q1, ran=1 for Q2 and this current version for Q3.
	if ran==0:
		door_to_open=['a','b','c']		#The doors the host will open.
		unchosen_door=['a','b','c']		#The door, which will remain closed till the end.
		unchosen_door.remove(chosen_door)	#Removing the door we chose from the unchosen doors (By definition).
		car_door=np.random.choice(doors,1)	#The door with the prize car.
		if chosen_door==car_door:		# If the car is behind our chosen door, the host can open any doors but ours.
			door_to_open.remove(car_door)
		else:					#If the car is not behind our chosen door, the host can only open the door without the car.
			door_to_open.remove(car_door)
			door_to_open.remove(chosen_door)
		door_open=np.random.choice(door_to_open,1) #From the remaining doors, the host will open one.
		unchosen_door.remove(door_open)		# We remove the opened door from the unchosen opens, giving us one door to switch to.
		if switch=='No':			# The probabilities if we switch or not.
			if chosen_door==car_door:
				wins+=1
		if switch=='Yes':
			if unchosen_door[0]==car_door:
				wins+=1	
	else:
		unchosen_door=['a','b','c']
		unchosen_door.remove(chosen_door)
		car_door=np.random.choice(doors,1)
		door_open=np.random.choice(unchosen_door,1)
		unchosen_door.remove(door_open)
		if door_open!=car_door: 
			if switch=='No':
				if chosen_door==car_door:
					wins+=1
			if switch=='Yes':
				if unchosen_door[0]==car_door:
					wins+=1
		if door_open==car_door:
			M-=1
		
print(wins/M)
#print(wins1/M)
