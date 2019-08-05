from random import randint, uniform,random

'''EJERCICIO NUMERO 1: IMPRIMIR HOLA'''
def hola():
    print ("Hola Mundo")
#hola() 

''' SUMA'''
def suma(a,b):
    return a+b
#print (suma(2,6))

'''EL MAYOR ENTRE DOS NUMEROS'''
def cual_es_mayor(c,d):
    if c>d:
        return c
    if d>c:
        return d
#print (cual_es_mayor(9,3))

'''VERIFICA SI EL EL NUMERO ESTA ENTRE 0 y 10'''
def entre0y10(e):
    if e >= 0 and e <= 10:
        return "EL NUMERO INGRESADO ESTA ENTRE 0 Y 10"
    else:
        return "EL NUMERO INGRESADO NO ESTA ENTRE 0 Y 10"
#print (entre0y10(8))

''' VERIFICA SI EL EL NUMERO ESTA ENTRE 0 Y 10, 11 Y 20, Y ENTRE 21 Y 30''' 
def entre(e):
    if e >= 0 and e <= 10:
        return "EL NUMERO ESTA ENTRE 0 Y 10"
    if e >= 11 and e <=20:
        return "EL NUMERO ESTA ENTRE 11 Y 20"
    elif e >= 21 and e<=30:
        return "EL NUMERO ESTA ENTRE 21 y 30"
#print (entre(22))

'''IMPRIMIR LOS NUMEROS DEL 1 AL 100 CON WHILE'''
def hasta100():
    a=1
    while a <= 100:
        print (a)
        a=a+1
#hasta100()

'''IMPRIMIR LOS NUMEROS DEL 1 AL 100 CON FOR'''
def imprimir100():
    for x in range (1,101):
        print x
#imprimir100()

'''IMPRIMIR CADA CARACTER DE HOLA MUNDO'''
def holaMundo():
    h= "Hola Mundo"
    for i in range(len(h)):
        print h[i]
#holaMundo()

'''DETERMINA SI EL NUMERO INGRESADO ES PAR O NO'''
def es_par(a):
    if a%2 == 0:
        return True
    else:
        return False
#print (es_par(4))

'''MUESTRA LOS NUMEROS PARES ENTRE 1 Y 100'''
def pares():
    for x in range(2,101,2):
        print x
#pares()

'''IMPRIME LOS NUMEROS DEL 0 AL 100'''
def cien():
    for x in range (0,101):
        print x
#cien() 

''' Genera un numero aleatorio entre 5 y 10'''
def generar():
    return randint(5,10)
#print(generar())

''' Genera un rango de 10 a 0'''
def rango():
    for x in range (10,-1,-1):
        print x
#rango()

'''INTERCAMBIA LOS DOS PRIMEROS CARACTER'''
def intercambio(a,s):
    l=s[0:2] + a[2:] +" "+ a[0:2] + s[2:]
    return l
#print (intercambio ("hola", "mundo"))

'''ADIVINA EL NUMERO'''
def aleatorio(a):
    n= randint (1,100) 
    print n
    if n == a:
        return "Ganaste"
    else:
        return "Perdiste"
#print (aleatorio(42))

'''EL MAXIMO DE 3 NUMEROS'''
def max_de_tres(a,b,c):
    if a > b and a > c :
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
#print (max_de_tres(4,6,1))

'''CALCULA LA LONGITUD DE UNA LISTA'''
def longitud(l):
    total= 0
    for x in l:
        total +=1
    print total
#longitud("Paola")

'''VERIFICA SI LA LETRA INGRESADA ES UN VOCAL'''
def es_vocal(v):
    if v=="a" or v=="e" or v=="i" or v=="o" or v=="u":
        return True
    elif v=="A" or v=="E" or v=="I" or v=="O" or v=="U":
        return  True
    else:
        return False
print es_vocal("A")

'''SUMA LOS ELEMENTOS DE UNA LISTA'''
def sum(s):
    suma=0
    for i in s:
        suma= suma+i
    return suma
print sum([1,3,5]) 

'''MULTIPLICA LOS ELEMENTOS DE UNA LISTA'''
def multip(m):
    mul=1
    for i in m:
        mul= mul*i
    return mul
print multip([1,2,3,4])

'''INVIERTE UNA CADENA'''
def inversa(i):
    print i[::-1]
inversa ("estoy probando")


'''PALINDROMO'''
def palindromo(p):
    return p==p[::-1]
print palindromo ("neuquen")

'''DEVUELVE TRUE SI DOS LISTAS TIENEN ALGUN ELEMENTO EN COMUN'''
def superposicion(li,ta):
    for i in range(len(li)):
        for x in range(len(ta)):
            if (li[i] == ta[x]):
                return True
    for i in range(len(ta)):
        for x in range(len(ta)):
            if (li[i] == ta[x]):
                return True
        else:
                return False
#print superposicion(["paola","mar"],["hola","mar"])

'''TOMA UN ENTERO N Y UN CARACTER C , DEVUELVE EL CARACTER MULTIPLICADO POR N''' 
def n_caracteres(e,c):
    acomula=c
    for i in range(e-1):
        c=c+acomula
    return c
#print n_caracteres(5,"x")

'''TOMA UNA LISTA DE ENTEROS Y ME IMPRIME UN HISTOGRAMA'''
def procedimientos(l):
    for i in l:
        print "*"*int(i)
#procedimientos([2,3,4])

'''QUE HACE, QUE NOMBRE LE PONDRIAS '''

'''suma (n + n-1) hasta 0'''
def sumatoria(n):
    x = 0
    i = 0
    while i <= n:
        x += i
        i += 1
    return x
#print sumatoria(4)

'''suma (n + n-1) hasta 0, pero de la manera recursiva'''
def sumaRecursiva(n):
    if n == 0:
        return 0
    else:
        return n + sumaRecursiva(n-1)
#print sumaRecursiva(6)

'''multiplica (n + n-1) hasta 0'''
def productoria(n):
    x = 1
    for i in range(n):
        x = x *(i + 1)
    return x
#print productoria(5)


'''multiplica (n + n-1) hasta 0, de manuera recursiva'''
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
#print factorial(4)


