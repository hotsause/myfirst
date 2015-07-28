import web
import cla
import httplib
# import urllib2
import sys
# import os
urls = (
        '','fun'
        # '/(.*)','fun'
        )
HC = httplib.HTTPConnection     
heaD = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'}   
class fun():
    def GET(self):
      if web.input():
        addr = str(web.input().addr)
        try:
            conn = HC(addr,timeout=100)
            conn.request('get','/',headers = heaD)
            resp = conn.getresponse()
            return 'header is %s \n\n\n\nresponse is \n\n%s' % ([(str(i[0])+' -> '+str(i[1])) for i in resp.getheaders()], resp.read())
        except:    
            return sys.exc_info()
        finally:
            conn.close()
        # return str(web.input().addr)
      else:
        return 'None'
pageform = cla.Myapp(urls,locals())      