#import pila
'''Clase Pila'''
class Pila:
    def __init__ (self):
        self.items=[]

    def estavacia(self):
        return self.items==[]

    def incluir(self,item):
        self.items.append(item)

    def inspeccionar(self):
        return self.items[len(self.items)-1]

    def extraer(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)

    def imprimir(self):
        print (self.items)

    def dar_vuelta(self):
        self.items = (self.items)[::-1]

    def vaciar(self):
       while not(self.estavacia()):
            self.extraer()

'''revertir una cadena de palabras'''
def revertir(a):
    p = Pila()
    for x in a.split(" "):
        p.incluir(x)
    l=[]
    while not p.estavacia():
        l = l + [p.extraer()]
    return " ".join(l)
#print(revertir("Mi diario Python"))

'''Misma cantidad de 0 que de 1'''
def cantidad(m):
    p=Pila()
    l=Pila()
    for x in range(len(m)):
        if m[x]=='0':
            p.incluir(0)
        elif m[x]=='1':
            l.incluir(1)
    if p.tamano() == l.tamano():
        return True
    else:
        return False
#print(cantidad("1010"))

'''Parentesis balanceado'''
def parentesis(c):
    resp=True
    p=Pila()
    for i in range(len(c)):
        if c[i] == '(':
            p.incluir(c[i])
        if c[i] == ')':
            if p.estavacia():
                resp=False
            if not p.estavacia():
                p.extraer()
    if p.tamano() != 0:
        resp=False
    return resp
#print(parentesis('(())('))

'''Validez de una cadena de paréntesis'''
def validez(v):
    p=Pila()
    for i in range (len(v)):
        if v[i] == '(' or v[i] == '[' or v[i] == '{':
            p.incluir (v[i])
        if not p.estavacia():
            if v[i] == ')':
                if p.inspeccionar() == '(':
                    p.extraer() 
                else:
                    return False
            elif v[i] == ']':
                if p.inspeccionar() == '[':
                    p.extraer()
                else:
                    return False
            elif v[i] == '}':
                if p.inspeccionar()== '{':
                    p.extraer()
                else:
                    return False
        if p.tamano() == 0:
            return True
        else:
            return False
#print(validez('(())'))

'''Palabra capicua'''
def capicua(num):
    p=Pila()
    j=0
    for i in range (len(num)):
        p.incluir(num[i])
    while not p.estavacia():
        if p.inspeccionar() == num[j]:
            j=j+1
            p.extraer()
        else:
            return False
    return True
#print (capicua("neuquen"))
#print (capicua("neuque"))

'''Implementar la clase pila nuevamente de manera que se comporte de la misma manera
utilizando listas, pero donde el tope no esté en la punta de la lista sino al principio de la lista.
Es decir '''
class Pila2: 
    def __init__(self):
        self.items = [] 
    def estaVacia(self):
        return self.items == [] 
    def incluir(self, item):
        self.items.insert(0,item)
    def extraer(self):
        return self.items.pop(0)
    def inspeccionar(self):
        return self.items[-1] 
    def tamano(self):
        return len(self.items)
    def imprimir(self):
        print (self.items)

p=Pila2()
(p.incluir(1))
(p.incluir(2))
(p.incluir(3))
(p.imprimir())
print(p.extraer())
#print(p.extraer())
#print(p.inspeccionar())
#print (p.items)
#(p.vaciar())
#print (p.imprimir())


