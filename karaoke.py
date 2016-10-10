#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


if __name__ == "__main__":
    try:
        file = open(sys.argv[1])
    except ValueError:
        sys.exit('Usage: python3 karaoke.py file.smil')

    parser = make_parser()
    kHandler = SmallSMILHandler()
    parser.setContentHandler(kHandler)
    parser.parse(file)

    data = kHandler.get_tags()
    my_string = ''
    for line in data:
        if my_string != "":
            my_string = my_string + "\n"
        my_string = my_string + line[0]
        for tag in line[1]:
            if line[1][tag] != '':
                my_string = my_string + '\t' + tag +'=' + '"'+line[1][tag] + '"'
            
    print(my_string)
    cadena = sys.argv[1]
    fichero_nombre = cadena.split(".")[0]+".json"
    json.dump(data,open(fichero_nombre,'w'))