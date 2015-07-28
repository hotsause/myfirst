import web
import cla
urls = (
        '','dealshow'
        )
class dealshow():
    def GET(self,*name):
        rend = web.template.render('templ/').showresp(cla.gloresp[1])
        return rend
show = cla.Myapp(urls,locals())        