import sys
import nsetools
import pickle
nse = nsetools.Nse()
PC = "previousClose"
O = "open"
H = "dayHigh"
L = "dayLow"
C = "closePrice"
LTP = "lastPrice"
H52 = "high52"
L52 = "low52"
NAME = "companyName"
# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep
 
# define our clear function
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

# now call function we defined above
clear()
quote = nse.get_quote(sys.argv[1])
pp_dict = {"P":quote[LTP]}
pickle.dump( pp_dict, open( "save.p", "wb" ) )
#pretty(quote)

def getohlc(quote, last):
	print("++++++++++++++++++++++++++++++++++++++++++++++\n")
	print(quote[NAME],"\n")
	print("L52 : ",round(quote[L52],2),"\tH52 : ",round(quote[H52],2),"\n")
	if(quote[O] == quote[PC]):
		print("Opened as Closed","\n")
	elif(quote[O] > quote[PC]):
		print("Opened High\t: +",round(quote[O]-quote[PC],2),"\n")
	else:
		print("Opened Low\t: -",round(quote[PC]-quote[O],2),"\n")
	print("LTP\t: ",round(quote[LTP],2))
	if(quote[LTP] == last):
		print("CHANGE = ",round(quote[LTP]-last,2))
	elif(quote[LTP] >= last):
		print("CHANGE = +",round(quote[LTP]-last,2))
	else:
		print("CHANGE = ",round(quote[LTP]-last,2))
	print("PClose\t: ",round(quote[PC],2))
	print("Open\t: ",round(quote[O],2))
	print("High\t: ",round(quote[H],2))
	print("Low\t: ",round(quote[L],2))
	print("Close\t: ",round(quote[C],2))
	print("++++++++++++++++++++++++++++++++++++++++++++++\n")
	
for i in range(1000):
	last_time = pickle.load( open( "save.p", "rb" ) )
	getohlc(quote, last_time["P"])
	pp_dict = {"P":quote[LTP]}
	pickle.dump( pp_dict, open( "save.p", "wb" ) )
	sleep(5)
	clear()