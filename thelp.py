import pandas as pd
import numpy as np
import math

class Intrade:
    def __init__(self,qty,buyp,sellp, margin = 1):
        self.margin = margin
        self.qty = qty
        self.buyp = buyp
        self.sellp = sellp
        self.btotal = round(qty * buyp, 2)
        self.stotal = round(qty * sellp, 2)
        self.bbrokerage = round(min( 0.0001 * qty * buyp, 20),2)
        self.sbrokerage = round(min( 0.0001 * qty * sellp, 20),2)
        self.brokerage = round(self.bbrokerage + self.sbrokerage,2)
        self.stt = math.ceil(0.00025 * qty * sellp)
        self.xtch = round(0.00325 * 0.01 * qty * ( buyp + sellp ),2)
        self.gst = round(0.18 * (self.brokerage + self.xtch),2)
        self.sebich = round(0.0000015 * qty * (buyp + sellp),2)
        self.sd = round(0.00006 * qty*(buyp+sellp),2)
        self.totalcharges = round(self.brokerage + self.stt + self.xtch + self.gst + self.sebich + self.sd ,2)
        self.totalcost = round((qty * buyp)/margin + self.totalcharges,2)
        self.net_pl = round(qty * (sellp - buyp) - self.totalcharges,2)
        self.gross_pl =  round(qty * (sellp - buyp),2)
        
def long_pl(buyp,qty):    
    gross = []
    net = []
    sp = []
    for i in np.arange(buyp-10,buyp+10,0.05):
        sp.append(i)
        gross.append(Intrade(qty,buyp,i).gross_pl)
        net.append(Intrade(qty,buyp,i).net_pl)
    sp =  np.array(sp)
    gross = np.array(gross)
    net = np.array(net)
    bep = round(sp[np.argwhere(net >= 0)[0]][0],2)
    print("BEP\t:", bep, "\tNet : ",Intrade(qty,buyp,bep).net_pl)
    p10 = round(sp[np.argwhere(net >= 10)[0]][0],2)
    print("10 Rs\t:", p10, "\tNet : ",Intrade(qty,buyp,p10).net_pl)
    p20 = round(sp[np.argwhere(net >= 20)[0]][0],2)
    print("20 Rs\t:", p20, "\tNet : ",Intrade(qty,buyp,p20).net_pl)
    
def short_pl(sellp,qty):    
    gross = []
    net = []
    bp = []
    for i in np.arange(sellp-10,sellp+10,0.05):
        bp.append(i)
        gross.append(Intrade(qty,i,sellp).gross_pl)
        net.append(Intrade(qty,i,sellp).net_pl)
    bp =  np.array(bp)
    gross = np.array(gross)
    net = np.array(net)
    bep = round(bp[np.argwhere(net >= 0)[-1]][0],2)
    print("BEP\t:", bep, "\tNet : ",Intrade(qty,bep,sellp).net_pl)
    p10 = round(bp[np.argwhere(net >= 10)[-1]][0],2)
    print("10 Rs\t:", p10, "\tNet : ",Intrade(qty,p10,sellp).net_pl)
    p20 = round(bp[np.argwhere(net >= 20)[-1]][0],2)
    print("20 Rs\t:", p20, "\tNet : ",Intrade(qty,p20,sellp).net_pl)