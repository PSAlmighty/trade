import nsetools
from time import sleep
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

filename = "syms.txt"
file = open(filename, "r")
symbols = []
for line in file:
   symbols.append(line.strip().upper())

print(symbols)

	
def quickquote(sym):
	quote = nse.get_quote(sym)
	scrip = sym+" "+"L52 : "+str(round(quote[L52],2))
	scrip = scrip+" H52 : "+str(round(quote[H52],2))
	scrip = scrip+" PC: "+str(round(quote[PC],2))
	scrip = scrip+" O: "+str(round(quote[O],2))
	scrip = scrip+" H: "+str(round(quote[H],2))
	scrip = scrip+" L: "+str(round(quote[L],2))
	scrip = scrip+" >> "+str(round(quote[LTP],2))
	print(scrip)
for sym in symbols:
	quickquote(sym)
	