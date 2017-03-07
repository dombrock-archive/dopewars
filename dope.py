# coding: utf-8
# Python 2.7
import random
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Item:
	def __init__(self,name,cat,price,info):
		self.name = name
		self.cat = cat
		self.price = price
		self.info = info

class City:
	def __init__(self,name,info):
		self.name = name
		self.info = info

class Player:
	def __init__(self,name):
		self.name = name
	cash = 150
	
	_Wheeze = 1
	_Stimpak = 0
	_Jet = 0
	_Kram = 0
	_LSX = 0

	def check_inv(self):
		print " "
		print color.RED+"I N V E N T O R Y :"+color.END
		print " "
		print "Cash:    ", self.cash
		print " "
		print "Wheeze:  ", self._Wheeze
		print "Stimpak: ", self._Stimpak
		print "Jet:     ", self._Jet
		print "Kram:    ", self._Kram
		print "LSX:     ", self._LSX
		print " "
		print "----"
		print " "

class Map:
	cities = []
	upper = 1.000
	downer = 1.000
	painkiller = 1.000

	def __init__(self,location,city1,city2,city3):
		self.location = location
		self.cities.append(city1)
		self.cities.append(city2)
		self.cities.append(city3)

	def travel(self, city):
		self.location = city
		print " "
		print color.GREEN+"You Have arrived at ", self.location.name+color.END
		print " "
		#set new rates
		self.upper = round(random.uniform(0.1,2.7),3)
		self.downer = round(random.uniform(0.1,2.7),3)
		self.painkiller = round(random.uniform(0.1,2.7),3)
	
	def check_demand(self):
		print " "
		print color.RED+"D E M A N D :"+color.END
		print "Current Location: ", self.location.name
		print " "
		print "Uppers: ",self.upper,"X"
		print "Downers: ",self.downer,"X"
		print "PainKillers: ",self.painkiller,"X"
		print " "
		print "Wheeze: ",float(Wheeze.price)*float(self.downer),"$"
		print "Stimpak: ",float(Stimpak.price)*float(self.painkiller),"$"
		print "Jet: ",float(Jet.price)*float(self.upper),"$"
		print "----"
		print " "

	def check_location(self):
		print " "
		print color.RED+"L O C A T I O N :"+color.END
		print "Current Location: ", self.location.name
		print " "
		print "Location Information: "
		print self.location.info
		print " "
		print "----"
		print " "

	def check_map(self):
		print " "
		print color.RED+"M A P :"+color.END
		print " "
		print "Current Location: ", self.location.name
		print " "
		print self.cities[0].name
		print self.cities[1].name
		print self.cities[2].name
		print " "
		print "----"
		print " "

def Travel():
	cost = round(random.uniform(0.1,20.0),3)
	destination = raw_input("Where to?: ")
	destination = destination.title()
	found = False
	if (p1.cash >= cost):
		for x in range(0,len(m1.cities)):
			if (destination == m1.cities[x].name):
				print "Found ",m1.cities[x].name," on the map..."
				found = True
				city = m1.cities[x]
		if(found == False):
			print "I can't find this place."
			print " "
		else:
			print "Traveling to ", destination," for",cost,"$";
			print " "
			p1.cash = p1.cash - cost
			m1.travel(city)
	else:
		print "you are too broke to travel! Try again later..."
		print " "

def Sell():
	found = False
	item = raw_input("Sell what?: ")
	item = item.title()
	amt = raw_input("Ok, how much do you want to sell?: ")
	if(amt.isdigit()==True):
		print "Selling",amt,"",item,"."
		print " "
	else:
		print "Please enter an integer for the amount."
		print " "

	if (item == "Wheeze"):
		found = True
		if(p1._Wheeze >= int(amt)):
			price = (float(Wheeze.price)*m1.downer)*float(amt)
			p1._Wheeze = p1._Wheeze -int(amt)
			p1.cash = p1.cash + (price)
			print "Sold",item,"for",price
			print " "
		else:
			print "You don't have enough of that!"
			print " "

	elif (item == "Jet"):
		found = True
		if(p1._Jet >= int(amt)):
			price = (float(Jet.price)*m1.upper)*float(amt)
			p1._Jet = p1._Jet -int(amt)
			p1.cash = p1.cash + (price)
			print "Sold",item,"for",price
		else:
			print "You don't have enough of that!"
			print " "

	elif (item == "Stimpak"):
		found = True
		if(p1._Stimpak >= int(amt)):
			price = (float(Stimpak.price)*m1.painkiller)*float(amt)
			p1._Stimpak = p1._Stimpak -int(amt)
			p1.cash = p1.cash + (price)
			print "Sold",item,"for",price
		else:
			print "You don't have enough of that!"
			print " "

	else:
		print "I can't find this item."


def Buy():
	found = False
	item = raw_input("Buy what?: ")
	item = item.title()
	amt = raw_input("Ok, how much do you want to buy?: ")
	if(amt.isdigit()==True):
		print "Buying",float(amt),"",item,"."
		print " "
	else:
		print "Please enter an integer for the amount."
		print " "

	if (item == "Wheeze"):
		found = True
		price = (float(Wheeze.price)*m1.downer)*float(amt)
		if(p1.cash >= price):
			p1._Wheeze = p1._Wheeze +int(amt)
			p1.cash = p1.cash - (price)
			print "Bought",item,"for",price
			print " "
		else:
			print "You don't have enough cash to buy that!"
			print " "

	elif (item == "Jet"):
		found = True
		price = (float(Jet.price)*m1.upper)*float(amt)
		if(p1.cash >= price):
			p1._Jet = p1._Jet +int(amt)
			p1.cash = p1.cash - (price)
			print "Bought",item,"for",price
		else:
			print "You don't have enough cash to buy that!"
			print " "

	elif (item == "Stimpak"):
		found = True
		price = (float(Stimpak.price)*m1.painkiller)*float(amt)
		if(p1.cash >= price):
			p1._Stimpak = p1._Stimpak +int(amt)
			p1.cash = p1.cash - (price)
			print "Bought",item,"for",price
		else:
			print "You don't have enough cash to buy that!"
			print " "

	else:
		print "I can't find this item."
	
def Help():
	print color.BOLD + color.GREEN + "BASIC COMMANDS: \ntravel - Go to a new place (costs some money)\nmap - Check your map\nlocation - Info about your current location\ninv - Check your stock\ndemand - Check the price of drugs in your current location\nbuy - Buy drugs\nsell - Sell Drugs " +color.END

def GameLoop():
	running = True
	waiting = True
	cmd = ""
	while (running == True):
		cmd = raw_input("Cmd: ")
		cmd = cmd.lower()
		if (cmd == "map" or cmd == "check map"):
			m1.check_map()
		elif (cmd == "location"):
			m1.check_location()
		elif(cmd == "inv" or cmd == "inventory" or cmd == "drugs" or cmd == "stock"):
			p1.check_inv()
		elif(cmd == "go" or cmd == "travel"):
			Travel()
		elif(cmd == "demand"):
			m1.check_demand();
		elif(cmd == "sell"):
			Sell()
		elif(cmd == "buy"):
			Buy()
		#utility
		elif(cmd == "help"):
			Help()
		elif(cmd == "exit" or cmd == "quit"):
			running = False	
		elif (cmd == "clear"):
			for x in range(0, 300):
				print "\n"	
		#unknown command
		else:
			print "Unknown Command!"
			print " "

		#print (i)
#ITEMS
Wheeze = Item('Wheeze','Downer','20','The chronic, the good shit. Classic. Smoked or eaten for a relaxing effect that lasts a few hours.')
Stimpak = Item('Stimpak','Pain-Killer','50','Keeps you going through the show, but not much longer.')
Jet = Item('Jet','Upper','25','Jibbidajibbidajibbida')

#CITY
Victory = City("Victory","Victory is an arcology that was built recently to deal with overcrowding within the \“old cities\”. The arcology presents a patently false illusion of idyllic country life to appease their jaded residents. \n \nThe city is controlled by a Chairman who is selected by a democratically elected \"Council\". The current Chairman, Gotthold, accepts bribes from Kenshiro CyberSystems and is focused on staying in power, no matter what. Gotthold is a Bored Bureaucrat.\n \nArmed vigilante gangs make up the core of law enforcement of Victory. These gangs are very unprofessional, but are highly dedicated to protecting \“law and order\”. The police is focused on suppressing the growing \"anti-globalization\" movement, which has been implicated in assassinations. The leader of the movement is Li Wu, an Useless Boss. According to police records, Li Wu is being funded by Psychobank.\n \nThe education system in Victory focuses on economic dogma; employees can parrot meaningless slogans and recite corporate creeds by heart.\n \nVictory has a booming industrial sector, but its environmental record is horrible.")
Arrival = City("Arrival", "Arrival is a first-generation \“floating city\”, built by libertarian political activists. The ship generally resides in international waters to avoid unwarranted government regulations and only docks at the \“old cities\” for resupply.\n \nThe city is controlled by a Chairman who is selected by a democratically elected \"Council\". The current Chairman, Osamu, accepts bribes from Kenshiro CyberSystems and is focused on treating the city as a personal fiefdom. The city rots away while Osamu enjoys a life of decadence. Osamu is a Dismal Enigma.\n \nLaw enforcement in Arrival has been outsourced to mercenaries. These corporate agents are highly professional, but are extremely corrupt and are only loyal to their paycheck. The police is battling a group of white-collar criminals called the Embezzlers that are harming corporate profits. The leader of this group is Bronislav, an Ideological Crusader. According to police records, Bronislav is being funded by The Unguided.\n \nThe education system in Arrival specializes in the humanities; employees are experts in philosophy and ethical decision-making, but lack basic math and science skills.\n \nArrival is proud of its reputation as a source of cheap labor. The labor, on the other hand, agitates to be a bit more expensive.")
Boost = City("Boost", "Boost is a Russian \“old city\” that has gained increased prominence due to neoliberal reforms and a favorable corporate environment.\n \nThe city has declared a \“state of emergency\” and places all real power into the hands of law enforcement. The current Police Commissioner, Falk, accepts bribes from Solar of Brussels and is focused on \"keeping the peace\". Falk seeks to peacefully resolve disputes between corporations before they turn violent. Falk is an Evangelist \“Team Player\”.\n \nLaw enforcement in Boost is handled by a traditional and obsolete police department. Their agents focuses on community outreach efforts, making them very popular with civilians. The police is battling a group of white-collar criminals called the Invisible Hand that are harming corporate profits. The leader of this group is Kiku, a Corporate Suit. According to police records, Kiku is being funded by Hamilton Fabridigital.\n \nThe education system in Boost focuses on economic dogma; employees can parrot meaningless slogans and recite corporate creeds by heart.\n \nBoost attracts a lot of skilled and unskilled migrants. Overcrowding is common in the residential units.")

p1 = Player('eric0')
m1 = Map(Arrival,Victory,Arrival,Boost)



print color.BOLD + color.CYAN + "W E L C O M E  T O  C Y B E R - D O P E - W A R S  A L P H A" +color.END
print color.BOLD + color.YELLOW + "A Cyber-Punk Drug Dealing Sim By Mathieu Dombrock" +color.END
Help()
print " "
print " "
GameLoop()
