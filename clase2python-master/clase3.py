"""import random


numero = random.randint(1,10)
print(numero)

from math import  sqrt

n = sqrt(2)
print(n)"""

import turtle

window = turtle.Screen()
square = turtle.Turtle()

numero = int (input("ingrese tamaño"))

def linea(numero):


    for i in range(4):
        square.forward(numero)
        square.left(90)
    turtle.mainloop()


linea(numero)




"""if i<=4:
    linea()


    turtle.mainloop()
i+1"""

