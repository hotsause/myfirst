import web
import sys
import os
urls = ('/','hello')
# global port
# port = os.environ.get('PORT', 8080)
# webapp = web.application(urls, globals())
class hello():
    def GET(self):
        # print(os.environ.get('PORT', 8080))###debug      
        return os.environ, os.uname,sys.platform, os.name
        # return '<html>\n<body>\n<h1>Hello,there.</h1>\n<h2>this time the env port is '+ str(os.environ.get('PORT', 8080)) + '</h2>\n</body>\n</html>'
# if __name__ == '__main__':###################################older 
    # try:
        # webapp = web.application(urls, globals())
        # webapp.run()
    # except:
        # print(sys.exc_info())#################################older
class Myapp(web.application):
    def run(self,port=int(os.environ.get('PORT', 8080)),*filllater):#########os.environ.get(...),ensure your application makes use of the port assigned to the user environment,on heroku:fill port=int(os.environ.get(...)) instead for heroku dynamic assigned port every start
        func = self.wsgifunc(*filllater)##########must have ?
        # print(port)###debug
        return web.httpserver.runsimple(func,('0.0.0.0',port))#####wsgifunc is must filled for runsimple()
if __name__ == '__main__':
    try:
        webapp = Myapp(urls, globals())
        webapp.run()
    except:
        print(sys.exc_info())        