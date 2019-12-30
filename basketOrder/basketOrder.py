###############################################################################
### Creator         : Pradhamesh Akkiraju                                   ###
### Date            : December 23/2019                                      ###
### Project Name    : basketOrder.py                                        ###
### Description     : This program is used to help calculate the            ###
###                     appropriate basket size for EU/TSX/NYSE MOC Trades  ###
### Last Edited     : December 29/2019                                      ###
###############################################################################

# Imports
import requests
from tkinter import *
from bs4 import BeautifulSoup
import re


def calculate():
    bpPerStock = round(buyingPower.get() / numberOfStocks.get(), 2)
    Label(window, text=bpPerStock).grid(row=2, column=1)

    tickerOneURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerOne.get()))
    tickerOneSoup = BeautifulSoup(tickerOneURL.text, 'html.parser')
    tickerOneScrape = tickerOneSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerOneSplit = re.split('-|\+', tickerOneScrape)
    Label(window, text=tickerOneSplit[0]).grid(row=4, column=1)
    tickerOnePrice = tickerOneSplit[0]
    shareSizeOne = bpPerStock/tickerOnePrice
    Label(window, text=shareSizeOne).grid(row=4, column=2)
    investedBPOne = shareSizeOne * tickerOneSplit
    Label(window, text=investedBPOne).grid(row=4, column=3)

    tickerTwoURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerTwo.get()))
    tickerTwoSoup = BeautifulSoup(tickerTwoURL.text, 'html.parser')
    tickerTwoScrape = tickerTwoSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerTwoSplit = re.split('-|\+', tickerTwoScrape)
    Label(window, text=tickerTwoSplit[0]).grid(row=5, column=1)
    shareSizeTwo = round(bpPerStock / tickerTwoSplit[0], -2)
    Label(window, text=shareSizeTwo).grid(row=5, column=2)
    investedBPTwo = shareSizeTwo * tickerTwoSplit
    Label(window, text=investedBPTwo).grid(row=5, column=3)

    tickerThreeURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerThree.get()))
    tickerThreeSoup = BeautifulSoup(tickerThreeURL.text, 'html.parser')
    tickerThreeScrape = tickerThreeSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerThreeSplit = re.split('-|\+', tickerThreeScrape)
    Label(window, text=tickerThreeSplit[0]).grid(row=6, column=1)
    shareSizeThree = round(bpPerStock / tickerThreeSplit[0], -2)
    Label(window, text=shareSizeThree).grid(row=6, column=2)
    investedBPThree = shareSizeThree * tickerThreeSplit
    Label(window, text=investedBPThree).grid(row=6, column=3)

    tickerFourURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerFour.get()))
    tickerFourSoup = BeautifulSoup(tickerFourURL.text, 'html.parser')
    tickerFourScrape = tickerFourSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerFourSplit = re.split('-|\+', tickerFourScrape)
    Label(window, text=tickerFourSplit[0]).grid(row=7, column=1)
    shareSizeFour = round(bpPerStock / tickerFourSplit[0], -2)
    Label(window, text=shareSizeFour).grid(row=7, column=2)
    investedBPFour = shareSizeFour * tickerFourSplit
    Label(window, text=investedBPFour).grid(row=7, column=3)

    tickerFiveURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerFive.get()))
    tickerFiveSoup = BeautifulSoup(tickerFiveURL.text, 'html.parser')
    tickerFiveScrape = tickerFiveSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerFiveSplit = re.split('-|\+', tickerFiveScrape)
    Label(window, text=tickerFiveSplit[0]).grid(row=8, column=1)
    shareSizeFive = round(bpPerStock / tickerFiveSplit[0], -2)
    Label(window, text=shareSizeFive).grid(row=8, column=2)
    investedBPFive = shareSizeFive * tickerFiveSplit
    Label(window, text=investedBPFive).grid(row=8, column=3)

    tickerSixURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerSix.get()))
    tickerSixSoup = BeautifulSoup(tickerSixURL.text, 'html.parser')
    tickerSixScrape = tickerSixSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerSixSplit = re.split('-|\+', tickerSixScrape)
    Label(window, text=tickerSixSplit[0]).grid(row=9, column=1)
    shareSizeSix = round(bpPerStock / tickerSixSplit[0], -2)
    Label(window, text=shareSizeSix).grid(row=9, column=2)
    investedBPSix = shareSizeSix * tickerSixSplit
    Label(window, text=investedBPSix).grid(row=9, column=3)

    tickerSevenURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerSeven.get()))
    tickerSevenSoup = BeautifulSoup(tickerSevenURL.text, 'html.parser')
    tickerSevenScrape = tickerSevenSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerSevenSplit = re.split('-|\+', tickerSevenScrape)
    Label(window, text=tickerSevenSplit[0]).grid(row=10, column=1)
    shareSizeSeven = round(bpPerStock / tickerSevenSplit[0], -2)
    Label(window, text=shareSizeSeven).grid(row=10, column=2)
    investedBPSeven = shareSizeSeven * tickerSevenSplit
    Label(window, text=investedBPSeven).grid(row=10, column=3)

    tickerEightURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerEight.get()))
    tickerEightSoup = BeautifulSoup(tickerEightURL.text, 'html.parser')
    tickerEightScrape = tickerEightSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerEightSplit = re.split('-|\+', tickerEightScrape)
    Label(window, text=tickerEightSplit[0]).grid(row=11, column=1)
    shareSizeEight = round(bpPerStock / tickerEightSplit[0], -2)
    Label(window, text=shareSizeEight).grid(row=11, column=2)
    investedBPEight = shareSizeEight * tickerEightSplit
    Label(window, text=investedBPEight).grid(row=11, column=3)

    tickerNineURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerNine.get()))
    tickerNineSoup = BeautifulSoup(tickerNineURL.text, 'html.parser')
    tickerNineScrape = tickerNineSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerNineSplit = re.split('-|\+', tickerNineScrape)
    Label(window, text=tickerNineSplit[0]).grid(row=12, column=1)
    shareSizeNine = round(bpPerStock / tickerNineSplit[0], -2)
    Label(window, text=shareSizeNine).grid(row=12, column=2)
    investedBPNine = shareSizeNine * tickerNineSplit
    Label(window, text=investedBPNine).grid(row=12, column=3)

    tickerTenURL = requests.get("https://ca.finance.yahoo.com/quote/{}".format(tickerTen.get()))
    tickerTenSoup = BeautifulSoup(tickerTenURL.text, 'html.parser')
    tickerTenScrape = tickerTenSoup.find_all("div", {"My(6px) Pos(r) smartphone_Mt(6px)"})[0].text
    tickerTenSplit = re.split('-|\+', tickerTenScrape)
    Label(window, text=tickerTenSplit[0]).grid(row=13, column=1)
    shareSizeTen = round(bpPerStock / tickerTenSplit[0], -2)
    Label(window, text=shareSizeTen).grid(row=13, column=2)
    investedBPTen = shareSizeTen * tickerTenSplit
    Label(window, text=investedBPTen).grid(row=13, column=3)

window = Tk()
window.geometry("400x400")
window.title("Basket Order Calculator")

Label(window, text="Enter Buying Power").grid(row=0, column=0)
buyingPower = DoubleVar()
buyingPower_inputBox = Entry(window, textvariable=buyingPower).grid(row=0, column=1)

Label(window, text="Enter # of Stocks").grid(row=1, column=0)
numberOfStocks = DoubleVar()
numberOfStocks_inputBox = Entry(window, textvariable=numberOfStocks).grid(row=1, column=1)

Label(window, text="BP Per Stock =").grid(row=2, column=0)

Label(window, text="Ticker(s)").grid(row=3, column=0)
Label(window, text="Stock Price").grid(row=3, column=1)
Label(window, text="Share Size").grid(row=3, column=2)
Label(window, text="BP Invested").grid(row=3, column=3)

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
tickerOne_IB = Entry(window, textvariable=tickerOne).grid(row=4, column=0)
tickerTwo_IB = Entry(window, textvariable=tickerTwo).grid(row=5, column=0)
tickerThree_IB = Entry(window, textvariable=tickerThree).grid(row=6, column=0)
tickerFour_IB = Entry(window, textvariable=tickerFour).grid(row=7, column=0)
tickerFive_IB = Entry(window, textvariable=tickerFive).grid(row=8, column=0)
tickerSix_IB = Entry(window, textvariable=tickerSix).grid(row=9, column=0)
tickerSeven_IB = Entry(window, textvariable=tickerSeven).grid(row=10, column=0)
tickerEight_IB = Entry(window, textvariable=tickerEight).grid(row=11, column=0)
tickerNine_IB = Entry(window, textvariable=tickerNine).grid(row=12, column=0)
tickerTen_IB = Entry(window, textvariable=tickerTen).grid(row=13, column=0)

calculateButton = Button(window, text="Calculate", command=calculate).grid(row=14, column=0)

window.mainloop()