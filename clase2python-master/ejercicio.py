
print("Operaciones Aritmeticas")

num1 = int(input("ingrese primer numero: "))
num2 = int(input("ingrese segundo numero: "))

def menu(num1,num2):

    print("Menu")
    print("1. Sumar numeros")
    print("2. Restar numeros")
    print("3. Multiplicar numeros")
    print("4. Dividir numeros")
    opc= int (input("Digite operacion a realizar: "))

    if opc ==1:
        res= num1+num2
        #print("a"+str(res))
        print("El resultado de la operacion es: {}".format(res))
    elif (opc==2):
        res = num1 - num2
        print("El resultado de la operacion es: {}".format(res))
    elif (opc==3):
        res = num1 * num2
        print("El resultado de la operacion es: {}".format(res))
    elif (opc==4):
        res = num1 / num2
        print("El resultado de la operacion es: {}".format(res))
    else:
        print("Ha digitado una opcion incorrecta")
menu(num1, num2)




