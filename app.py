import web
import sys
urls = ('/','hello')
# webapp = web.application(urls, globals())
class hello():
    def GET(self):
        return '<html>\n<body>\n<h1>Hello,there.</h1>\n</body>\n</html>'
if __name__ == '__main__':
    try:
        webapp = web.application(urls, globals())
        webapp.run()
    except:
        print(sys.exc_info())