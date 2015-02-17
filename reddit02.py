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

datetime = tree.xpath('//@datetime')

nextprev = tree.xpath('//span[@class="nextprev"]/a/@href')

#lin = nextprev[0].text
#code = tree.findtext('thing id-')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')
tl = len(title)
dl = len(domain)
sl = len(submitter)
ll = len(liFirst)
fl = len(FullName)
dtl = len(datetime)
nl = len(nextprev)
print '\ntitle: ', title
print '\ndomain: ', domain
print '\nsubmitter: ', submitter
print '\ndatetime: ', datetime
print '\nliFirst: ', liFirst
print '\nFullName: ', FullName
print '\nnextprev: ', nextprev
print tl,dl,ll,fl,dtl,nl
#print 'Prices: ', prices
