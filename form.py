import web
import cla
import httplib
# import urllib2
import sys
# import os
urls = (
        '','fun1'
        # '/(.*)','fun'
        )
HC = httplib.HTTPConnection     
heaD = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept encoding':'gzip, deflate',
        'Accept language':'en-US,en;q=0.5',
        'Connection':'keep-alive',
        'Referer':'https://www.google.com',
        'DNT':'1',
        'Cache-Control':'max-age=0'
        }  

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
class fun1():
    def GET(self):
        addr = str(web.input().addr)
        if len(addr) < 1:
            addr = 'www.z.cn'
        if addr.startswith('http://'):
            addr = addrresp = addr[7:]
        try:
            conn = HC(addr,timeout=100)
            conn.request('GET','/',headers = heaD)
            resp = conn.getresponse() 
            rend = web.template.render('templ/').form
            cla.gloresp = (resp.getheaders(),resp.read(),resp.version,resp.status,resp.reason)########baidu return badstatusline
            return rend(cla.gloresp[0],cla.gloresp[1],cla.gloresp[2],cla.gloresp[3],cla.gloresp[4])###########global response, transfer to showresp.py
        except:    
            return sys.exc_info(),addr
        finally:
            conn.close()
pageform = cla.Myapp(urls,locals())      