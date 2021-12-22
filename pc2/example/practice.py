url = "https://raw.githubusercontent.com/pshiguihara/AWS_Proyecto_Prueba/master/PY01.csv"
import pandas as pd
datos = pd.read_csv(url)
print(datos)

import numpy as np

def opcion1():
  N = int(input("Ingrese cantidad de cliente: "))
  d1 = datos.groupby("cliente").agg({"monto":np.size})
  print((d1.sort_values("monto", ascending = False)).head(N))
  print("")

def opcion2():
  N = int(input("cantidad de clientes: "))
  d1 = datos.groupby("clientes").agg({"descuentos":np .size})
  print((d1.sort_values("monto", ascending = False)).head(N))
  print("") 
  
def opcion3():
  N = int(input("Ingrese la primera edad: "))
  M = int(input("Ingrese la segunda edad: "))
  e = datos.assign(EDAD = datos["fecha"]-datos["fecNacimiento"])

def opcion4():
  import numpy as np
  print(datos.groupby(['cliente','fecha']).agg({'monto':[np.mean]}))
  años = []
  b = datos["fecha"]
  for i in b:
    años.append(i[5:7])
  datos.assign(año=años)
  print(datos.groupby(["cliente", "año"]).agg({"monto":np.mean}))

def opcion5():
  print(datos.groupby(['fecha']).agg({'monto':np.mean}))
  año = str(input("año: "))
  b2 = str(input("mes: "))
  b3 = str(input("dia: "))
  f = año + "-" + b2 + "-" + b3
  datos["fecha"]==f  

opc = 1
while (opc != 0):
  print("Bienvenido a nuestro menú")
  print("[1] Seleccionar los N clientes que más compran")
  print("[2] Seleccionar los N clientes con más descuentos")
  print("[3] Seleccionar los clientes por rango de edad")
  print("[4] Seleccionar clientes por promedios")
  print("[5] Buscador universal")
  print("[6] Cerrar el menú")
  opc = int(input('Opción: '))
  if opc == 1:
      opcion1()
  elif opc == 2:
      opcion2()
  elif opc == 3:
     opcion3()
  elif opc == 4:
     opcion4()
  elif opc == 5:
     opcion5()
  elif opc == 6:
     break