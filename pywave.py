#!/usr/bin/python
import cherrypy
import os
import simplejson
import sys
import serial
import json
from irtoy import IrToy

with open('AppleRemote.json', 'r') as inFile:
    codes = json.load(inFile)
device = serial.Serial('/dev/ttyACM0')

MEDIA_DIR = os.path.join(os.path.abspath('.'), 'media')

class AjaxApp(object):
    @cherrypy.expose
    def index(self):
        return open(os.path.join(MEDIA_DIR, 'pywave.html'))

    @cherrypy.expose
    def click(self, control):
        cherrypy.response.headers['Content-Type'] = 'application/json'

        toy = IrToy(device)
        toy.transmit(codes[control])
        print('code:', control, 'code length:', len(codes[control]), 'handshake:', toy.handshake, 'bytecount:', toy.byteCount, 'complete:', toy.complete)
        return simplejson.dumps(dict(response='Recieved and transmitted, %s' % control))

config = {'/icons':
                {'tools.staticdir.on': True,
                 'tools.staticdir.dir': os.path.join(MEDIA_DIR, 'icons')
                }
        }

print config

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080,
                       })

if hasattr(cherrypy.engine, 'signal_handler'):
    cherrypy.engine.signal_handler.subscribe()

cherrypy.tree.mount(AjaxApp(), '/', config=config)
cherrypy.engine.start()
cherrypy.engine.block()
device.close()
