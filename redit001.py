__author__ = 'Anne'
from lxml import html
import requests
page = requests.get('http://localhost:8000/001/til.htm')
tree = html.fromstring(page.text)
title = tree.xpath('//p[@class="title"]/a/text()')
domain = tree.xpath('//span[@class="domain"]/a/text()')
submitter = tree.xpath('//p[@class="tagline"]/a/text()')
liFirst = tree.xpath('//li[@class="first"]/a/text()')
FullName = tree.xpath('//@data-fullname')
#code = tree.findtext('thing id-')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')
print '\ntitle: ', title
print '\ndomain: ', domain
print '\nsubmitter: ', submitter
print '\nliFirst: ', liFirst
print '\nFullName: ', FullName
#print 'Prices: ', prices
