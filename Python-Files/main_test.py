# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 10:21:10 2018

@author: salman.nazir
"""
import os
from lyngspice import NgSpice

ng = NgSpice()

with open(os.path.normpath(os.getcwd() + '\\Step-Netlist\\netlist.cir')) as f:
    netlist = f.readlines()
    

results = []
for i in range(100):
    print('simulation # {}'.format(i+1))
    data, units = ng.bg_run(netlist)
    results.append((data, units))
