import random

print "Dice allowed: 4, 2d4, 6, 2d6, 8, 2d8, 10, 2d10, 100"

dice_number = raw_input("Dice Number?")

if (dice_number != "4") or (dice_number != "2d4") or (dice_number != "6") or (dice_number != "2d6") or (dice_number != "8") or (dice_number != "2d8") or (dice_number != "10") or (dice_number != "2d10") or (dice_number != "100"):
	print "Please choose from the list."
	print "Dice allowed: 4, 2d4, 6, 2d6, 8, 2d8, 10, 2d10, 100"
	dice_number = raw_input("Dice Number?")

#d4
if dice_number == "4":
	print "Rolling the dice"
	min = 1
	max = 4
	print "....."
	print "You Rolled"
	print "....."
	print random.randint(min, max)
	
#2d4
if dice_number == "2d4":
	print "Rolling the dice"
	min = 1
	max = 4
	print "....."
	print "You Rolled"
	print "....."
	a = random.randint(min, max)
	b = random.randint(min, max)
	c = a + b
	print c 

#d6
if dice_number == "6":
	print "Rolling the dice"
	min = 1
	max = 6
	print "....."
	print "You Rolled"
	print "....."
	print random.randint(min, max)

#2d6
if dice_number == "2d6":
	print "Rolling the dice"
	min = 1
	max = 6
	print "....."	
	print "You Rolled"
	print "....."
	a = random.randint(min, max)
	b = random.randint(min, max)
	c = a + b
	print c 
	
#d8
if dice_number == "8":
	print "Rolling the dice"
	min = 1
	max = 8
	print "....."
	print "You Rolled"
	print "....."
	print random.randint(min, max)
	
#2d8
if dice_number == "2d8":
	print "Rolling the dice"
	min = 1
	max = 8
	print "....."
	print "You Rolled"
	print "....."
	a = random.randint(min, max)
	b = random.randint(min, max)
	c = a + b
	print c 
	
#d10
if dice_number == "10":
	print "Rolling the dice"
	min = 1
	max = 10
	print "....."
	print "You Rolled"
	print "....."
	print random.randint(min, max)

#2d10
if dice_number == "10":
	print "Rolling the dice"
	min = 1
	max = 10
	print "....."
	print "You Rolled"
	print "....."
	a = random.randint(min, max)
	b = random.randint(min, max)
	c = a + b
	print c 

if dice_number == "100":
	print "Rolling the dice"
	min = 1
	max = 100
	print "....."
	print "You Rolled"
	print "....."
	print random.randint(min, max)	
