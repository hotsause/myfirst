import web
urls = (
        '/(.*)','dealb'
        # '','home'
            )
class dealb():
    def GET(self):
        rend = web.template.render('templ/').b()
        # return rend
        return 'b.py here'

class home():    
    def GET(self):
        raise web.seeother('/')

pageb = web.application(urls,locals())