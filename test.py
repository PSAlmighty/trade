import sys
from math import ceil as ceiling
print("Zerodha BEP Calculator")

buyp = float(sys.argv[1])
qty = float(sys.argv[2])
iord = str(sys.argv[3]).upper()
sellp = float(sys.argv[4])
try:
	margin = float(sys.argv[5])
except:
	margin = 1.00
print("Margin = ",margin)

print(buyp, qty, iord, sellp)
turnover = 2*qty

def calc_brokerage(iord, qty, buyp, sellp):
	if iord == "I":
		bbrokerage = min( 0.0001 * qty * buyp, 20)
		sbrokerage = min( 0.0001 * qty * sellp, 20)
		brokerage = bbrokerage + sbrokerage
	else:
		brokerage = 0
	return(round(brokerage,2))
brokerage = calc_brokerage(iord, qty, buyp, sellp)

def calc_stt(iord, qty, buyp, sellp):
	if iord == "I":
		stt = 0.00025 * qty * sellp
	else:
		stt = 0.001 * qty * ( buyp + sellp )
	return(ceiling(stt))
stt = calc_stt(iord, qty, buyp, sellp)
	
def calc_xtch(qty, buyp, sellp):
	xtch = 0.00325 * 0.01 * qty * ( buyp + sellp )
	return(round(xtch,2))
xtch = calc_xtch(qty, buyp, sellp)
	
def calc_gst(brokerage, xtch):
	gst = 0.18 * (brokerage + xtch)
	return(round(gst,2))
gst = calc_gst(brokerage, xtch)

def calc_sebich(qty, buyp, sellp):
	sebich = 0.0000015 * qty * (buyp + sellp)
	return(round(sebich,2))
	
sebich = calc_sebich(qty, buyp, sellp)
	
def calc_sd(qty, buyp, sellp):
	sd = 0.00006 * qty*(buyp+sellp)
	return(round(sd,2))
sd = calc_sd(qty, buyp, sellp)

print("BROK\t: ",brokerage)
print("XTCh\t: ",xtch)
print("GST\t: ",gst)
print("STT\t: ",stt)
print("SEBI\t: ", sebich)
print("SD\t: ", sd)
totalTnC = round(brokerage + stt + xtch + gst + sebich + sd ,2)

print("Charges : ",totalTnC)
print("COST\t: Rs.",round((qty * buyp)/margin + totalTnC), 2)
net = qty * (sellp - buyp) - totalTnC
print("GROSS\t: Rs.",round(qty * (sellp - buyp),2))
if net < 0:
	print("LOSS\t: Rs.", round(net,2))
	print("LP\t: ",round(net/( (qty * buyp)/margin + totalTnC) * 100, 2),"%")
elif net > 0:
	print("PROFIT\t: Rs.", round(net,2))
	print("PP\t: ",round(net/( (qty * buyp)/margin + totalTnC) * 100, 2),"%")
else:
	print("BROKE EVEN!")


