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
class fun():
    def GET(self):
      if web.input():
        addr = str(web.input().addr)
        try:
            conn = HC(addr,timeout=100)
            conn.request('get','/')
            resp = conn.getresponse()
            return 'header is %s \n\n\n\nresponse is \n%s' % (resp.getheaders(), resp.read())
        except:    
            return sys.exc_info()
        finally:
            conn.close()
        # return str(web.input().addr)
      else:
        return 'None'
pageform = cla.Myapp(urls,locals())      