import web
urls = ('/','hello')
webapp = web.application(urls, globals())
class hello():
    def GET(self):
        return '<html>\n<body>\n<h1>Hello,there.</h1>\n<td><a href="myfirst/">test</a></td>\n</body>\n</html>'
if __name__ == '__main__':
    webapp.run()