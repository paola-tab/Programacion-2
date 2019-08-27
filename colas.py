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

''' Escriba una función que reciba una Cola C y mueva sus elementos a una nuevaCola
pero manteniendo el orden de salida de los elementos.
Al finalizar la Cola C no debe contener elementos'''
def nuevaCola(c):
    nueva=Cola()
    while not c.estaVacia():
        nueva.agregar(c.avanzar())
        nueva.darVuelta()
        return nueva
print(nuevaCola('123'))
      
#c=Cola()
#(c.agregar(1))
#(c.agregar(2))
#(c.agregar(3))
#c.imprimir()
#c.darVuelta()
#c.imprimir()
#c.vaciar()
#c.imprimir()