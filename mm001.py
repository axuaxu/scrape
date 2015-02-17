__author__ = 'Anne'
import lxml.html
import csv

sheet = []
url = 'https://s3.amazonaws.com/codecave/tut1.html'
page = requests.get(url)
document_tree = lxml.html.fromstring(page.text)
i = 1
while 1:
    row = document_tree.xpath('//tr[%d]/td/text()' % i)
    if not row:
        break
    else:
        i += 1
        sheet.append(row)