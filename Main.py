#
from tkinter import Tk, Label, Button
import coinmarketcap
import json
import pandas as pd
import time


market = coinmarketcap.Market()
altcardano = market.ticker("cardano")
altethereum = market.ticker("ethereum")

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cardano (ADA) BasicTicker GUI")


        self.label = Label(master, text="Cardano (ADA) Price Ticker")
        self.label.pack()

        #This is the get price button

        self.getprice_button = Button(master, text="Get Price", command=self.getprice)
        self.getprice_button.pack()

        #Here is the close button

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    #This function prints ethereum value when called
    def getprice(self):
        print(altethereum)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()