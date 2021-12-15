
import contextlib
from __future__ import with_statement
try:
  from urllib.parse import urlencode
  except ImportError:
    from urllib import urlencode
    try:
      from urllib.request import urlopen
      except ImportError:
        from urllib2 import urlopen
import sys



def make_shorten(url):
    request_url = ('http://tinyurl.com/api-create.php?' + 
    urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


#The main function to receive user inputs    
def main():
    for shortyurl in map(make_shorten, sys.argv[1:]):
        print(shortyurl)
