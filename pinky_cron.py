#!/usr/bin/env python3

import subprocess
import sys
import pickle

salida_comando = []
file_name = "salida.p"

try:
    salida = pickle.load( open( file_name, "rb" ) )
except:
    salida = {}

try:
    p = subprocess.run(['pinky'], capture_output=True)
    salida_comando = p.stdout.decode().split()

    if p.returncode !=0:
        print(p.stderr.decode())
        sys.exit(1)
except:
    sys.exit(1)

salida_comando=salida_comando[6:]

for i in range(0,len(salida_comando)-1,7):
    print(i)
    login = salida_comando[i]
    fecha = salida_comando[i+4]
    hora = salida_comando[i+5]
    ip = salida_comando[i+6]
    fecha_hora = " ".join([fecha,hora])
    if ip in salida:
        salida[ip].add(fecha_hora)
    else:
        salida[ip]=set([fecha_hora])


pickle.dump( salida, open( file_name, "wb" ) )
sys.exit(0)