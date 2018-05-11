'''
Created on 2018-5-3

@author: kikita
'''
from scripting import *

# get a CityEngine instance
ce = CE()

''' increment the street width parameter of all selected street segments'''
# @noUIupdate
def incrementStreetWidths(increment):
    selectedSegments = ce.getObjectsFrom(ce.selection, ce.isGraphSegment)
    for segment in selectedSegments:
        oldWidth = ce.getAttribute(segment, "/ce/street/streetWidth")
        newWidth = oldWidth+increment
        ce.setAttribute(segment, "/ce/street/streetWidth", newWidth)

if __name__ == '__main__':
    incrementStreetWidths(10)


