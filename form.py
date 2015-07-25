import web
import cla
# import os
urls = (
        '','fun'
        # '/(.*)','fun'
        )
class fun():
    def GET(self):
      if web.input():
        return str(web.input().first),str(web.input().second)
      else:
        return 'None'
pageform = cla.Myapp(urls,locals())      