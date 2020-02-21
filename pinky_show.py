#!/usr/bin/env python3

import subprocess
import sys
import pickle
import pprint

salida_comando = []
file_name = "~/Develop/pinky_list/salida.p"

try:
    salida = pickle.load( open( file_name, "rb" ) )
except:
    salida = {}

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(salida)

sys.exit(0)