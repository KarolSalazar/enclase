import math
class Vector:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    self.magnitud = (self.x**2 + self.y**2 + self.z**2)**0.5
  def __str__(self):
    cadena = "( "+str(self.x)+" , "+str(self.y)+" , "+str(self.z)+" )"
    return(cadena)
  def __mul__ (self, otro):
    if type(self)==type(otro):
      return(self.x*otro.x+self.y*otro.y+self.z*otro.z)
    else:
      return(self.x*otro+self.y*otro+self.z*otro)
    

# Defino vectores
x_1 = float(input("Ingrese coordenada X1: "))
y_1 = float(input("Ingrese coordenada Y1: "))
z_1 = float(input("Ingrese coordenada Z1: "))

x_2 = float(input("Ingrese coordenada X2: "))
y_2 = float(input("Ingrese coordenada Y2: "))
z_2 = float(input("Ingrese coordenada Z2: "))

vec_1=Vector(x_1, y_1, z_1)
vec_2=Vector(x_2, y_2, z_2)

escalar = float(input("Ingrese escalar: "))

print("Al multiplicar vector_1 con vector_2 obtenemos: " + str(vec_1.__mul__(vec_2)))
print("Al multiplicar vector_1 con escalar obtenemos: " + str(vec_1.__mul__(escalar)))


"""
  def __add__(self, otra):
    respuesta = Vector(self.x+otra.x,self.y+otra.y, self.z+otra.z)
    return(respuesta)
  def __sub__(self, otra):
    respuesta = Vector(self.x-otra.x,self.y-otra.y, self.z-otra.z)
    return(respuesta)
  def escalar(self, otra):
    return(self.x*otra.x+self.y*otra.y)

    

1# Defino vectores
x_1 = float(input("Ingrese coordenada X1: "))
y_1 = float(input("Ingrese coordenada Y1: "))
z_1 = float(input("Ingrese coordenada Z1: "))

x_2 = float(input("Ingrese coordenada X2: "))
y_2 = float(input("Ingrese coordenada Y2: "))
z_2 = float(input("Ingrese coordenada Z2: "))

x_3 = float(input("Ingrese coordenada X3: "))
y_3 = float(input("Ingrese coordenada Y3: "))
z_3 = float(input("Ingrese coordenada Z3: "))

vec_1=Vector(x_1, y_1, z_1)
vec_2=Vector(x_2, y_2, z_2)
vec_3=Vector(x_2, y_2, z_2)

"""