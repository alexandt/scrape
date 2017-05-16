from lxml import html
import requests
import datetime
import csv

#import data
#Nasdaqpage = requests.get('http://www.nasdaq.com/markets/most-acive.aspx')
betpage = open("/home/trystan/BetTnt/betpagea.html", 'r', encoding='utf-8')
page = betpage.read()
tree = html.fromstring(page)
#companies = tree.xpath('//a[@class="mostactive"]/text()')

print(tree.xpath('//li'))
"""
companies = tree.xpath('//tr/td/b/a/text()')
price = tree.xpath('//tr/td[4]/text()')
print(len(companies))
print(len(price))


dictt={} 
for i in range(len(companies)):
    dictt[companies[i]]=price[i]
    py
#print(dictt)
dt=datetime.datetime.now()
dt=str(dt)
dtlist=["Date and Time", dt]
print(dtlist)
"""

#save in csv file
"""
with open("Excel-Stock-Prices/stocks.csv","a") as stocklist:
    stockwrite = csv.writer(stocklist)
    stockwrite.writerow(dtlist)
    stockwrite.writerow(companies)
    stockwrite.writerow(price)
    """ 