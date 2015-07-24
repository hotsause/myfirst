import web
# import app
import cla
import os
urls = (


        "",'dealb'  #########if '/(.*)' (from web.py official site) instead, response 404,and '(.*)' will catch anything begins with b 
            )
class dealb():
    def GET(self,*argvs):
        rend = web.template.render('templ/').b()
        return os.environ.get('PORT'),rend
        # return 'b.py here'

class home():    
    def GET(self):
        raise web.seeother('/')

pageb = cla.Myapp(urls,locals())##########port spacify needed??
# if __name__ == '__main__':
    # pageb.run()################for test