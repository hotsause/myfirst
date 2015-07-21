import web
import sys
urls = ('/','hello')
# webapp = web.application(urls, globals())
class hello():
    def GET(self):
        return '<html>\n<body>\n<h1>Hello,there.</h1>\n</body>\n</html>'
class Myapp(web.application):
    def run(self,port=80,*filllater):
        func = self.wsgifunc(*filllater)##########must have ?
        return web.httpserver.runsimple(func,('0.0.0.0',port))#####wsgifunc is must filled for runsimple()
if __name__ == '__main__':
    try:
        webapp = Myapp(urls, globals())
        webapp.run(port=8888)
    except:
        print(sys.exc_info())