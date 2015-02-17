"""__author__ = 'AX'
   scrape from reddit TIL
   """
from lxml import html
import requests

def openPage(s)
    return tree

def readPage(docTree,s):
    myList = docTree.xpath(s)
    return myList



page = requests.get('http://localhost:8000/001/til.htm')
tree = html.fromstring(page.text)

title = readPage(tree,'//p[@class="title"]/a/text()')
domain = readPage(tree,'//span[@class="domain"]/a/text()')
submitter = readPage(tree,'//p[@class="tagline"]/a/text()')
liFirst = readPage(tree,'//li[@class="first"]/a/text()')
FullName = readPage(tree,'//@data-fullname')
datetime = readPage(tree,'//@datetime')

nextprev = tree.xpath('//span[@class="nextprev"]/a/@href')

lenList = [len(title),len(domain),len(submitter),len(liFirst),len(FullName),len(datetime)]
minLen = min(lenList)

i = 0
while i < minLen:
    print i,title[i],domain[i],submitter[i],liFirst[i],FullName[i],datetime[i],'\n'
    i = i + 1



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
print '\nlenList: ', lenList
print '\nminList: ', minLen
#print 'Prices: ', prices
