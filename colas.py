'''Clase Cola agregando metodo imprimir, vaciar y dar vuelta'''
class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)

    def imprimir(self):
        print (self.items)
        
    def vaciar(self):
        while not(self.estaVacia()):
            self.avanzar()
            
    def darVuelta(self):
        self.items = (self.items)[::-1]
        
#c=Cola()
#(c.agregar(1))
#(c.agregar(2))
#(c.agregar(3))
#c.imprimir()
#c.darVuelta()
#c.imprimir()
#c.vaciar()
#c.imprimir()
''' Escriba una función que reciba una Cola C y mueva sus elementos a una nuevaCola
pero manteniendo el orden de salida de los elementos.
Al finalizar la Cola C no debe contener elementos'''
def nuevaCola(C):
    nueva=Cola()
    while not C.estaVacia():
        nueva.agregar(C.avanzar())
    return nueva
#C=Cola()
#C.agregar(1)
#C.agregar(2)
#C.imprimir()
#nuevaCola(C).imprimir()
#print(C.estaVacia())

'''Escriba una rutina que reciba dos Colas C1 y C2 de números enteros y devuelva una
nueva Cola con los elementos concatenados en el orden C1 y C2.
Es de destacar que las Colas recibidas nodeben ser sufrir ningún tipo de cambio o alteración'''
def concatenados(C1,C2):
    conca=Cola()
    if C1.tamano() == C2.tamano():
        while not C1.estaVacia():
            conca.agregar(C1.avanzar())
            conca.agregar(C2.avanzar())
    else:
        if C1.tamano() < C2.tamano():
            while not C2.estaVacia():
                conca.agregar(C2.avanzar())
                while not C1.estaVacia():
                    conca.agregar(C1.avanzar())
        else:
            if C1.tamano() > C2.tamano():
                while not C1.estaVacia():
                    conca.agregar(C1.avanzar())
                while not C2.estaVacia():
                    conca.agregar(C2.avanzar())
    return conca
    
C1=Cola()
C2=Cola()
C1.agregar(1)
C1.agregar(2)
C2.agregar(3)
C2.agregar(4)
C2.agregar(5)
C2.imprimir()
C2.imprimir()
concatenados(C1,C2).imprimir()