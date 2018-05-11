'''
Created on 2018-5-3

@author: kikita
'''
from scripting import *

# get a CityEngine instance
ce = CE()

def selectByAttribute(attr, value):
    objects = ce.getObjectsFrom(ce.scene)
    selection = []
    for o in objects:
        attrvalue = ce.getAttribute(o, attr)
        if attrvalue  ==  value:
            selection.append(o)
        
    ce.setSelection(selection)
    return selection


if __name__ == '__main__':
    selectByAttribute("connectionStart","JUNCTION")
    pass