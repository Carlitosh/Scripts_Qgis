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
errores = var4 - var2

print ""
print "El R2 es de: ", np.corrcoef(var2,var4)[0][1]
print "El RMSE es de: " , np.sqrt(((var4 - var2) ** 2).mean())
print "El error aritmetico medio es de ",(var4 - var2).mean()
print "El Desvio Estandar de los errores es de ", np.std(errores)
print "Nombre de la columna predichos: ",Predichos
print "Nombre de la columna observados: ",Observados
print ""




