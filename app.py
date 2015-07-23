import web
import sys
import os
import random
import urllib2
import b
urls = (
        # '/a(.+)','pagea1'#########something wrong
        '/a','pagea',
        '/b',b.pageb,
        '/(.*)','hello')
# global port
# port = os.environ.get('PORT', 8080)
# webapp = web.application(urls, globals())
getur = ['http://www.baidu.com','http://www.sogou.com','http://wap.17wo.cn/404.html']
resp = urllib2.urlopen(random.choice(getur)).read()
with open('files/test.html','w') as fil:#########just test files storage in heroku
    fil.write(resp)
class hello():
    def GET(self,name):
        try:    
            self.count = open('files/count','r')#########just test files storage in heroku
            self.countNum = self.count.read()
        except:
            print(sys.exc_info())
        finally:
            self.count.close()
        try:    
            self.count = open('files/count','w')  
            if self.countNum:
                self.nUm = int(self.countNum) + 1
                self.count.write(str(self.nUm))
            else:
                self.count.write('0')
        except:
            print(sys.exc_info())
        finally:
            self.count.close()
        # print(os.environ.get('PORT', 8080))###debug      
        # return '<html>\n<body>\n<h1>Hello,there.</h1>\n<h2>this time the env port is '+ str(os.environ.get('PORT', 8080)) + '</h2>\n<h3>' +str((os.environ,os.uname(),sys.platform, os.name)) +'<h3>\n</body>\n</html>'
        # return '<html>\n<body>\n<h1>Hello,there.</h1>\n<h2>this time the env port is '+ str(os.environ.get('PORT', 8080)) + '</h2>\n</body>\n</html>'
        # return web.template.render('templ/').a()
        choi = random.choice((web.template.render('templ/').a,web.template.render('templ/').b))
        return '%{1} %{0} %{2}'.format(choi(),self.nUm,name)
        # return sys.stdout.write(urllib2.urlopen('http://wap.17wo.cn/404.html').read())###crash except for ie
# if __name__ == '__main__':###################################older 
    # try:
        # webapp = web.application(urls, globals())
        # webapp.run()
    # except:
        # print(sys.exc_info())#################################older
class pagea():
    def GET(self):
        rend = web.template.render('templ/').a()
        return rend
class pagea1():
    def GET(self,*name):
        return name
class pageb():
    def GET(self):
        raise web.seeother('/a')##################code 303
class Myapp(web.application):
    def run(self,port=int(os.environ.get('PORT', 8080)),*filllater):#########os.environ.get(...),ensure your application makes use of the port assigned to the user environment,on heroku:fill port=int(os.environ.get(...)) instead for heroku dynamic assigned port every start
        func = self.wsgifunc(*filllater)##########must have ?
        # print(port)###debug
        return web.httpserver.runsimple(func,('0.0.0.0',port))#####wsgifunc is must filled for runsimple()
if __name__ == '__main__':
        webapp = Myapp(urls, globals())
        webapp.run()

      