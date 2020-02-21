#!/usr/bin/env python3

import subprocess
import sys
import pickle

salida_comando = []

try:
    salida = pickle.load( open( "salida.p", "rb" ) )
except:
    salida = {}

print(salida)

try:
    p = subprocess.run(['pinky'], capture_output=True)
    salida_comando = p.stdout.decode().split()

    if p.returncode !=0:
        print(p.stderr.decode())
        sys.exit(1)
except:
    sys.exit(1)

salida_comando=salida_comando[6:]

salida_comando.extend(salida_comando)
salida_comando[11] = salida_comando[11][:-1] +"5"

print(len(salida_comando),salida_comando)



for i in range(0,len(salida_comando)-1,7):
    login = salida_comando[i]
    print(i+4)
    fecha = salida_comando[i+4]
    hora = salida_comando[i+5]
    ip = salida_comando[i+6]
    fecha_hora =" ".join([fecha,hora])
    if ip in salida:
        salida[ip].add(fecha_hora)
    else:
        salida[ip]=set([fecha_hora])


pickle.dump( salida, open( "salida.p", "wb" ) )

print(salida)