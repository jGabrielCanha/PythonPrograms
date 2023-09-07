#A partir da orbita vista no código exemplo, construir um sistema que reproduza a orbita de um satélite em relação ao planeta que esta circulando o Sol.

from vpython import *
#Web VPython 3.2
def orb1(coordX):
    return sqrt(pow(15,2)-pow(coordX,2))
def orb2(coordX):
    return sqrt(pow(25,2)-pow(coordX,2))
scene.background=color.black
sol = sphere(pos=vector(0,0,0),color=color.red,radius=6)
Planet = sphere(pos = vector(25,0,0),color=color.blue,radius=1)
Lua = sphere(pos = vector(45,0,0),color=color.white,radius=3.5)
controle=0
delta = 0.0001
x=-15 #coordenada x da Lua
x_x = -25
y=0
y_x=0
direcao='direita'
direcao_x='direita'
while controle < 5:
    rate(100)
    if direcao == 'direita':
        x = x + 0.25
        if x == 15:
            direcao = 'esquerda'
    else:
        x = x - 0.25
        if x == -15:
            direcao = 'direita'
    if direcao_x == 'direita':
        x_x = x_x + 0.50
        if x_x == 25:
            direcao_x = 'esquerda'
    else:
        x_x = x_x - 0.50
        if x_x == -25:
            direcao_x = 'direita'
    Lua.pos.x = x
    Planet.pos.x= x_x
    y = orb1(x)
    y_x = orb2(x_x)
    if direcao == 'direita':
        Lua.pos.y = y
    else:
        Lua.pos.y = -y
    if direcao_x == 'direita':
        Planet.pos.y=y_x
    else:
        Planet.pos.y=-y_x
    controle = controle + delta
    


