#!/usr/bin/env python
#coding=utf-8
# import sys
import web
import os
# import urllib2
class Myapp(web.application):
    def run(self,port=int(os.environ.get('PORT', 8080)),*filllater):#########os.environ.get(...),ensure your application makes use of the port assigned to the user environment,on heroku:fill port=int(os.environ.get(...)) instead for heroku dynamic assigned port every start
        func = self.wsgifunc(*filllater)##########must have ?
        # print(port)###debug
        return web.httpserver.runsimple(func,('0.0.0.0',port))#####wsgifunc is must filled for runsimple()