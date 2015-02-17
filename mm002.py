__author__ = 'Anne'
import requests
from lxml import html
import inspect

class Response(object):
    def doc(self):
        if not hasattr(self, '_doc'):
            self._doc = html.fromstring(self.text)
        return self._doc

    def links(self):
        return self.doc().xpath('//a/@href')

    def images(self, filter_extensions=['jpg', 'jpeg', 'gif', 'png']):
        return [link for link in self.doc().xpath('//img/@src') if link.endswith(tuple(filter_extensions))]

    def title(self):
        title = self.doc().xpath('//title/text()')
        if len(title):
            return title[0].strip()
        else:
            return None
for method_name, method in inspect.getmembers(Response, inspect.ismethod):
    setattr(requests.models.Response, method_name, method.im_func)
r = requests.get('http://imgur.com/')
print "title\n",r.title()
print "links\n",r.links()
print "images\n",r.images(filter_extensions=['jpg'])
