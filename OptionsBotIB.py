import logging # Import logging to save session results for further analysis
import time # Time is needed to send our bot in the waiting mode
import numpy as np # Faster calculations
import scipy as sp # Normal pdf for Black-Schoels
from ibapi.client import *
from ibapi.wrapper import *

class MyApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
    
    def contractDetails(self, reqId, contractDetails):
        print (f"Contract details: {contractDetails}")

    def contractDetailsEnd(self, reqId):
        print ("End of Contarct details")

def computeBSM(cp, spot_price, strike_price, t_to_exp, r, sigma):
    d1 = (np.log(spot_price/strike_price) + (r + (sigma**2)/2)*t_to_exp)/(sigma*np.sqrt(t_to_exp))
    d2 = d1 - sigma*np.sqrt(t_to_exp)
    if (cp == "CALL"):
        return 
    
#We will add some code here later with implementation of the Black-Schoels Model for Option trading


def main():
    app = MyApp()
    app.connect("127.0.0.1", 7497, clientId=0)
    app.run()

if __name__ == "__main__":
    main()

    
