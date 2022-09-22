# Exercice 1
#1
my_fav_numbers = {7,12,3,1,40}

#2
my_fav_numbers.add(11)
my_fav_numbers.add(13)
my_fav_numbers.add(15)
print(my_fav_numbers)

#3
my_fav_numbers.remove(15)
print(my_fav_numbers)

friend_fav_numbers = {22,23,120,10}

friend = friend_fav_numbers.union(my_fav_numbers)

print(friend)

# Exercice 2 

myTuple=(1,2,3,4,5,6,7,8,9,0)
print("values in my tuple are:\t" , end='')
for n in myTuple:
    print (n, ' ',end='')
print ('\n')
print('A tuple is a collection which is ordered and unchangeable.so no we can\'t add anything to it ')
print("selon le cours")

# Exercice 3

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove('Banana')

basket.remove('Blueberries')

basket.append("Kiwi")

basket.insert(0,"Apples")

count=0
for item in basket:
	if(item=="Apples"):
		print('an',item," is find")
		count=count+1
print(f'there are {count} Apples in my basket')

basket.clear()

print(basket)

# Exercice 4

# float est un type de donné qui prend les décimaux en compte négative comme positive.
#la différence est simple int ne prend pas des valeurs à virgule alors que c'est le cas pour float
var=1
j=1
thelist=[]
for i in range(10):
	if(j==1):
		thelist.append(int(var))
		var=var+0.5
		j=0
	else :
		thelist.append(var)
		var=var+0.5
		j=1
for item in thelist:
	print(item," ",end='')

# Exercice 5

for i in range (1,21):
    	print(i," ",end='')

print('\n')

print('display of even numbers from 1 to 20')
for i in range (1,21):
	if ((i%2)==0):
		print(i," ",end='')


# Exercice 6

myname='Ahldaïr'
yourname=''
while(yourname != myname) :
	print('Rule: i\'m Harold and your name must be equal to mine to left the loop ')
	yourname=input('input your name please:\t')

# Exercice 7

print('separate the fruits with a single space')
fruits=input('what are your favorites fruits :\t')
thelist=fruits.split(" ")
for item in thelist:
	print(item," ",end='')

print("\n")
choice=input("Enter a fruit:\n")
if choice in thelist:
	print("You chose one of your favorite fruits! Enjoy!")
else :
	print("You chose a new fruit. I hope you enjoy")

# Exercice 8

toppings=[]
topping=''
prize=10
while( topping !="quit"):
	topping=input('enter a topping or quit to quit : ')
	if(topping!='quit') :
		toppings.append(topping)
		print(f"We’ll add that {topping} to your pizza.")
		prize=prize+2.5
	else :
		print('Your troppings are :\t',end='')
		for i in toppings:
			print(i," ",end='')
		print('\n')
		print("Bill =",prize)


# Exercice 9


name=['Harold','Nicodeme','Mary', 'Jeanne']
number=int(input('how many are you ?'))
bill=0
for i in range(number):
	age=int(input((f'how old is the {i+1}e person ?')))
	if(age<3):
		bill=bill+0
	elif (age>=3 and age<=12) :
		bill=bill+10
	elif(age>12):
		bill=bill+15
	else:
		print('you are not repertoried')

print('Bill = ',bill)
final=[]
for i in name:
	age=int(input((f'how old is {i} ')))
	if(age>=16):
		final.append(i)
	else:
		print('you are not allowed to see watch this movie')

print('Those who are allow to see this movie are : ',end='')
for i in final:
	print(i," ",end='')

# Exercice 10

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches=[]
print("we are starting to prepare your sandwich")
for i in sandwich_orders :
	finished_sandwiches.append(i)
	print(f'I made your {i}')


# Exercice 11


sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

finished_sandwiches = []
print("the deli has run out of pastrami")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    
for sandwich in sandwich_orders:
    print("I made your {}".format(sandwich))
    finished_sandwiches.append(sandwich)
print("there is the list of your sandwitch made: ",finished_sandwiches)




