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
    salida_comando = p.stdout.decode().split("\n")

    if p.returncode !=0:
        print(p.stderr.decode())
        sys.exit(1)
except:
    sys.exit(1)
print(salida_comando)
# salida_comando=salida_comando[6:]

for line in salida_comando[1:-1]:
    print(line)
    line_split = line.split()
    login = line_split[0]
    fecha = line_split[-3]
    hora = line_split[-2]
    ip = line_split[-1]
    fecha_hora = " ".join([fecha,hora])
    if ip in salida:
        salida[ip].add(fecha_hora)
    else:
        salida[ip]=set([fecha_hora])


pickle.dump( salida, open( file_name, "wb" ) )
sys.exit(0)