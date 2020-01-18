###############################################################################
### Creator         : Pradhamesh Akkiraju                                   ###
### Date            : December 23/2019                                      ###
### Project Name    : basketOrder.py                                        ###
### Description     : This program is used to help calculate the            ###
###                     appropriate basket size for EU/TSX/NYSE MOC Trades  ###
### Last Edited     : December 29/2019                                      ###
###############################################################################

# Imports
import math

import requests
from tkinter import *
from bs4 import BeautifulSoup
import re


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def calculate():
    bpPerStock = round(buyingPower.get() / numberOfStocks.get(), 2)
    Label(window, text=bpPerStock).grid(row=2, column=1, padx=5, pady=5)

    tickerOneURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerOne.get()))
    tickerOneSoup = BeautifulSoup(tickerOneURL.text, 'html.parser')
    tickerOneScrape = tickerOneSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerOneSplit = re.split('-|\+', tickerOneScrape)
    Label(window, text=tickerOneSplit[0]).grid(row=4, column=1, padx=5, pady=5)
    shareSizeOne = round_down(bpPerStock / float(tickerOneSplit[0]), -2)
    Label(window, text=shareSizeOne).grid(row=4, column=2, padx=5, pady=5)
    investedBPOne = shareSizeOne * float(tickerOneSplit[0])
    Label(window, text=investedBPOne).grid(row=4, column=3, padx=5, pady=5)

    tickerTwoURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerTwo.get()))
    tickerTwoSoup = BeautifulSoup(tickerTwoURL.text, 'html.parser')
    tickerTwoScrape = tickerTwoSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerTwoSplit = re.split('-|\+', tickerTwoScrape)
    Label(window, text=tickerTwoSplit[0]).grid(row=5, column=1, padx=5, pady=5)
    shareSizeTwo = round_down(bpPerStock / float(tickerTwoSplit[0]), -2)
    Label(window, text=shareSizeTwo).grid(row=5, column=2, padx=5, pady=5)
    investedBPTwo = shareSizeTwo * float(tickerTwoSplit[0])
    Label(window, text=investedBPTwo).grid(row=5, column=3, padx=5, pady=5)

    tickerThreeURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerThree.get()))
    tickerThreeSoup = BeautifulSoup(tickerThreeURL.text, 'html.parser')
    tickerThreeScrape = tickerThreeSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerThreeSplit = re.split('-|\+', tickerThreeScrape)
    Label(window, text=tickerThreeSplit[0]).grid(row=6, column=1, padx=5, pady=5)
    shareSizeThree = round_down(bpPerStock / float(tickerThreeSplit[0]), -2)
    Label(window, text=shareSizeThree).grid(row=6, column=2, padx=5, pady=5)
    investedBPThree = shareSizeThree * float(tickerThreeSplit[0])
    Label(window, text=investedBPThree).grid(row=6, column=3, padx=5, pady=5)

    tickerFourURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerFour.get()))
    tickerFourSoup = BeautifulSoup(tickerFourURL.text, 'html.parser')
    tickerFourScrape = tickerFourSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerFourSplit = re.split('-|\+', tickerFourScrape)
    Label(window, text=tickerFourSplit[0]).grid(row=7, column=1, padx=5, pady=5)
    shareSizeFour = round_down(bpPerStock / float(tickerFourSplit[0]), -2)
    Label(window, text=shareSizeFour).grid(row=7, column=2, padx=5, pady=5)
    investedBPFour = shareSizeFour * float(tickerFourSplit[0])
    Label(window, text=investedBPFour).grid(row=7, column=3, padx=5, pady=5)

    tickerFiveURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerFive.get()))
    tickerFiveSoup = BeautifulSoup(tickerFiveURL.text, 'html.parser')
    tickerFiveScrape = tickerFiveSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerFiveSplit = re.split('-|\+', tickerFiveScrape)
    Label(window, text=tickerFiveSplit[0]).grid(row=8, column=1, padx=5, pady=5)
    shareSizeFive = round_down(bpPerStock / float(tickerFiveSplit[0]), -2)
    Label(window, text=shareSizeFive).grid(row=8, column=2, padx=5, pady=5)
    investedBPFive = shareSizeFive * float(tickerFiveSplit[0])
    Label(window, text=investedBPFive).grid(row=8, column=3, padx=5, pady=5)

    tickerSixURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerSix.get()))
    tickerSixSoup = BeautifulSoup(tickerSixURL.text, 'html.parser')
    tickerSixScrape = tickerSixSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerSixSplit = re.split('-|\+', tickerSixScrape)
    Label(window, text=tickerSixSplit[0]).grid(row=9, column=1, padx=5, pady=5)
    shareSizeSix = round_down(bpPerStock / float(tickerSixSplit[0]), -2)
    Label(window, text=shareSizeSix).grid(row=9, column=2, padx=5, pady=5)
    investedBPSix = shareSizeSix * float(tickerSixSplit[0])
    Label(window, text=investedBPSix).grid(row=9, column=3, padx=5, pady=5)

    tickerSevenURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerSeven.get()))
    tickerSevenSoup = BeautifulSoup(tickerSevenURL.text, 'html.parser')
    tickerSevenScrape = tickerSevenSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerSevenSplit = re.split('-|\+', tickerSevenScrape)
    Label(window, text=tickerSevenSplit[0]).grid(row=10, column=1, padx=5, pady=5)
    shareSizeSeven = round_down(bpPerStock / float(tickerSevenSplit[0]), -2)
    Label(window, text=shareSizeSeven).grid(row=10, column=2, padx=5, pady=5)
    investedBPSeven = shareSizeSeven * float(tickerSevenSplit[0])
    Label(window, text=investedBPSeven).grid(row=10, column=3, padx=5, pady=5)

    tickerEightURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerEight.get()))
    tickerEightSoup = BeautifulSoup(tickerEightURL.text, 'html.parser')
    tickerEightScrape = tickerEightSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerEightSplit = re.split('-|\+', tickerEightScrape)
    Label(window, text=tickerEightSplit[0]).grid(row=11, column=1, padx=5, pady=5)
    shareSizeEight = round_down(bpPerStock / float(tickerEightSplit[0]), -2)
    Label(window, text=shareSizeEight).grid(row=11, column=2, padx=5, pady=5)
    investedBPEight = shareSizeEight * float(tickerEightSplit[0])
    Label(window, text=investedBPEight).grid(row=11, column=3, padx=5, pady=5)

    tickerNineURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerNine.get()))
    tickerNineSoup = BeautifulSoup(tickerNineURL.text, 'html.parser')
    tickerNineScrape = tickerNineSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerNineSplit = re.split('-|\+', tickerNineScrape)
    Label(window, text=tickerNineSplit[0]).grid(row=12, column=1, padx=5, pady=5)
    shareSizeNine = round_down(bpPerStock / float(tickerNineSplit[0]), -2)
    Label(window, text=shareSizeNine).grid(row=12, column=2, padx=5, pady=5)
    investedBPNine = shareSizeNine * float(tickerNineSplit[0])
    Label(window, text=investedBPNine).grid(row=12, column=3, padx=5, pady=5)

    tickerTenURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerTen.get()))
    tickerTenSoup = BeautifulSoup(tickerTenURL.text, 'html.parser')
    tickerTenScrape = tickerTenSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerTenSplit = re.split('-|\+', tickerTenScrape)
    Label(window, text=tickerTenSplit[0]).grid(row=13, column=1, padx=5, pady=5)
    shareSizeTen = round_down(bpPerStock / float(tickerTenSplit[0]), -2)
    Label(window, text=shareSizeTen).grid(row=13, column=2, padx=5, pady=5)
    investedBPTen = shareSizeTen * float(tickerTenSplit[0])
    Label(window, text=investedBPTen).grid(row=13, column=3, padx=5, pady=5)

    totalBP = format(investedBPOne + investedBPTwo + investedBPThree + investedBPFour + investedBPFive + investedBPSix + investedBPSeven + investedBPEight + investedBPNine + investedBPTen, ",")
    Label(window, text=totalBP).grid(row=14, column=3, padx=5, pady=5)

window = Tk()
window.geometry("500x500")
window.title("Basket Order Calculator")

Label(window, text="Enter Buying Power").grid(row=0, column=0, padx=5, pady=5)
buyingPower = DoubleVar()
buyingPower_inputBox = Entry(window, textvariable=buyingPower).grid(row=0, column=1, padx=5, pady=5)

Label(window, text="Enter # of Stocks").grid(row=1, column=0, padx=5, pady=5)
numberOfStocks = DoubleVar()
numberOfStocks_inputBox = Entry(window, textvariable=numberOfStocks).grid(row=1, column=1, padx=5, pady=5)

Label(window, text="BP Per Stock =").grid(row=2, column=0, padx=5, pady=5)

Label(window, text="Ticker(s)").grid(row=3, column=0, padx=5, pady=5)
Label(window, text="Stock Price").grid(row=3, column=1, padx=5, pady=5)
Label(window, text="Share Size").grid(row=3, column=2, padx=5, pady=5)
Label(window, text="BP Invested").grid(row=3, column=3, padx=5, pady=5)

tickerOne = StringVar()
tickerTwo = StringVar()
tickerThree = StringVar()
tickerFour = StringVar()
tickerFive = StringVar()
tickerSix = StringVar()
tickerSeven = StringVar()
tickerEight = StringVar()
tickerNine = StringVar()
tickerTen = StringVar()
tickerOne_IB = Entry(window, textvariable=tickerOne).grid(row=4, column=0, padx=5, pady=5)
tickerTwo_IB = Entry(window, textvariable=tickerTwo).grid(row=5, column=0, padx=5, pady=5)
tickerThree_IB = Entry(window, textvariable=tickerThree).grid(row=6, column=0, padx=5, pady=5)
tickerFour_IB = Entry(window, textvariable=tickerFour).grid(row=7, column=0, padx=5, pady=5)
tickerFive_IB = Entry(window, textvariable=tickerFive).grid(row=8, column=0, padx=5, pady=5)
tickerSix_IB = Entry(window, textvariable=tickerSix).grid(row=9, column=0, padx=5, pady=5)
tickerSeven_IB = Entry(window, textvariable=tickerSeven).grid(row=10, column=0, padx=5, pady=5)
tickerEight_IB = Entry(window, textvariable=tickerEight).grid(row=11, column=0, padx=5, pady=5)
tickerNine_IB = Entry(window, textvariable=tickerNine).grid(row=12, column=0, padx=5, pady=5)
tickerTen_IB = Entry(window, textvariable=tickerTen).grid(row=13, column=0, padx=5, pady=5)

calculateButton = Button(window, text="Calculate", command=calculate).grid(row=14, column=0, padx=5, pady=5)

window.mainloop()