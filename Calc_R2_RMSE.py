#!/usr/bin/python
# -*- coding: utf-8 -*-

##Points=group
##Mapa_de_puntos=vector
##Observados=field Mapa_de_puntos
##Predichos=field Mapa_de_puntos


from qgis.utils import *
from qgis.core import *
from PyQt4.QtCore import * 
import numpy as np


vector = processing.getObject(Mapa_de_puntos)
var = []
var3 = []
iter = vector.getFeatures()
 
#adicion de valores de columna a lista y conversion de lista a array 
for feature in iter:
    idx = vector.fieldNameIndex(str(Observados))
    var.append(feature.attributes()[idx])
    idxi = vector.fieldNameIndex(str(Predichos))
    var3.append(feature.attributes()[idxi])
    
var2 = np.asarray([var])
var4 = np.asarray([var3])
print ""
print "El R2 es de: ", np.corrcoef(var2,var4)[0][1]
print ""
print "El RMSE es de: " , np.sqrt(((var4 - var2) ** 2).mean())


