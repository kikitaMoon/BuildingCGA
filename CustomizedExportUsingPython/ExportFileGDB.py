# -*- coding: utf-8 -*-
__author__ = 'kikita'

from scripting import *

# Get a CityEngine instance
ce = CE()

# To get the shape from a selection with shape
SelectedShapes = ce.getObjectsFrom(ce.selection(), ce.isShape)
for shape in SelectedShapes:
    ce.setStartRule(shape, ce.getName(shape))
    ce.setAttributeSource(shape, "ABC", "ArchEntityID")