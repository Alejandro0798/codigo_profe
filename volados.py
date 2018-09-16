import os

def obtieneToken(cadena):
    token = ""
    indice = 0
    while indice < len(cadena):
        letra = cadena[indice]        
        if letra == " ":
            indice +=1
            if indice == 0:
                None
            else:
                break
        elif letra in operadores:
            indice +=1
            break
        elif letra == "=":
            if indice < len(cadena) - 1:
                if cadena[indice+1] != '=':
                    identificador.append(token)
            indice +=1
            break
        else:
            token = token + letra
            indice +=1

    if token != "":
        if token in dic_reservadas.keys():
            dic_reservadas[token]+=1
        else:
            tokens.append(token)
        
    nuevaCadena =cadena[indice:]            
    return nuevaCadena

dic_reservadas = {"int":0,"input":0,"while":0}
operadores = ["(",")"]
cadena = "numero= int(int(input(while s'¿Qué número quieres saber si es primo? ')))"
cadena2= "while int input"
identificador = []
tokens = []

#archivo = open("reservadas.txt", "r") 
#reservadas= archivo.read().splitlines()  
#archivo.close() 
for i in range(2):#len(reservadas)
    if i==1:
        cadena=cadena2
    while len(cadena) > 0:
        os.system('cls')
        cadena = obtieneToken(cadena)
        #input()
print("Nueva Cadena:"+cadena)
print("Tokens:", tokens)
print("Identificadores:",identificador)
print("Cantidad Reservadas:",dic_reservadas)