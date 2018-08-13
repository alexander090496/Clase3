a = {1,2,3}

b="alex"
c="angulo"
e='10'

f="false"

print(a)
print("Mi nombre es {} y mi apellido es {}".format(b,c))

print(int(e))


#
#dato =input("cual es tu nombre??")

#print(dato)

num1=1
num2=2
num3=3
if (num1<num2):
    print("num{} es menor que {}".format(1,2))
elif num2==num1:
    print("son iguales")
else:
    print("son diferentes")

x=1
while x < 10:
    print(x)
    x = x+1





def saludo():
    print("saludos")
saludo()

def cuadrado(n):
    print(n*n)
cuadrado(2)

def retornar(n):
    return 'nombre {} y apellido angulo'.format(n)
r = retornar("alex")
print(r)

##tuplas listas y diccionarios

tupla= (1,"a", True,10.4 )
print(tupla [0])

lista=["al","we"]

lista[0]="wu"
print(lista)

dic={'juan':"a", 'edad':2, 'año':3}
print(dic)

clase=[{'nombre':"a", 'edad':2, 'año':3},{'nombre':"b", 'edad':4, 'año':5}, ("ca",23)]

print(clase[1])





