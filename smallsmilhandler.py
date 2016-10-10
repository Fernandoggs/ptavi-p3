#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):
        
        self.width = ""
        self.height = ""
        self.background-color = ""
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
        
    def startElement(self, name, attrs):
    
        if name == 'root-layout'
            self.width = attrs.get('width',"")
            self.height = attrs.get('height',"")
            self.background-color = attrs.get('background-color',"")
        elif name == 'region'
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom',"")
            self.left = attrs.get('left',"")
            self.right = attrs.get('right',"")
        elif name == 'img'
            self.imgsrc = attrs.get('img',"")
            self.imgregion = attrs.get('region',"")
            self.imgbegin =
            
            

