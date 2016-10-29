#!/usr/bin/env python3
 
import skilstak.colors as c
import urllib.request
import json

with urllib.request.urlopen('https://raw.githubusercontent.com/colevahey/miniature-enigma/master/letters.json') as response:
       html = response.read()
       data = json.loads(html.decode("utf-8"))
       print(data)
