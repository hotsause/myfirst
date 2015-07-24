import web
import cla
urls = (
        '','deala'
        )
class deala():
    def GET(self,*name):
        rend = web.template.render('templ/').a()
        return rend
pagea = cla.Myapp(urls,locals())        