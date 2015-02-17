__author__ = 'Anne'
from lxml import html
import requests
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.text)
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')
print 'Buyers: ', buyers
print 'Prices: ', prices
