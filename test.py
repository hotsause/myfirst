import web
import b
urls = (
  "/b", b.pageb,
  "/(.*)", "index"
)

class index:
    def GET(self, path):
        return "hello " + path

app = web.application(urls, locals())

if __name__ == "__main__":
    app.run()