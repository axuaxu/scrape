__author__ = 'Anne'
from lxml import html
import requests
page = requests.get('http://localhost:8000/001/til.htm')

tree = html.fromstring(page.text)
title = tree.xpath('//p[@class="title"]/a/text()')
tl = len(title)
domain = tree.xpath('//span[@class="domain"]/a/text()')
dl = len(domain)
submitter = tree.xpath('//p[@class="tagline"]/a/text()')
sl = len(submitter)
liFirst = tree.xpath('//li[@class="first"]/a/text()')
ll = len(liFirst)
FullName = tree.xpath('//@data-fullname')
fl = len(FullName)
datetime = tree.xpath('//@datetime')
dtl = len(datetime)
nextprev = tree.xpath('//span[@class="nextprev"]/a/@href')
nl = len(nextprev)
#lin = nextprev[0].text
#code = tree.findtext('thing id-')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')
print '\ntitle: ', title
print '\ndomain: ', domain
print '\nsubmitter: ', submitter
print '\ndatetime: ', datetime
print '\nliFirst: ', liFirst
print '\nFullName: ', FullName
print '\nnextprev: ', nextprev
print tl,dl,ll,fl,dtl,nl
#print 'Prices: ', prices
