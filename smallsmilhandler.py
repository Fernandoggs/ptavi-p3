#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):
        
        self.width = ""
        self.height = ""
        self.backgroundcolor = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.imgsrc = ""
        self.imgregion = ""
        self.imgbegin = ""
        self.imgdur = ""
        self.audiosrc = ""
        self.audiobegin = ""
        self.audiodur = ""
        self.textstreamsrc = ""
        self.textstreamregion = ""
        self.lista = []
        
    def startElement(self, name, attrs):
    
        if name == 'root-layout':
            self.width = attrs.get('width',"")
            self.height = attrs.get('height',"")
            self.backgroundcolor = attrs.get('backgroundcolor',"")
            atributes = {'width': self.width,
                         'height': self.height,
                         'backgroundcolor': self.backgroundcolor}
            atributes['tag'] = name
            self.lista.append(atributes)
        elif name == 'region':
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom',"")
            self.left = attrs.get('left',"")
            self.right = attrs.get('right',"")
            atributes = {'id': self.id,
                         'top': self.top,
                         'bottom':self.bottom,
                         'left': self.left,
                         'right': self.right}
            atributes['tag'] = name
            self.lista.append(atributes)

        elif name == 'img':
            self.imgsrc = attrs.get('img',"")
            self.imgregion = attrs.get('region',"")
            self.imgbegin = attrs.get('begin',"")
            self.imgdur = attrs.get('dur',"")
        elif name == 'audio':
        	self.audiosrc = attrs.get('src',"")
        	self.audiobegin = attrs.get('begin',"")
        	self.audiodur = attrs.get('dur',"")
        elif name == 'textstream':
        	self.textstreamsrc = attrs.get('src',"")
        	self.textstreamregion = attrs.get('region',"")

    def get_tags(self):
    		return self.lista

if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    Data = sHandler.get_tags()
    print(Data)        
            

