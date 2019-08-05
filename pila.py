#import pila
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

#revertir una cadena de palabras
def revertir(a):
    p = Pila()    
    aux=Pila()
    for x in range(len(a)):
        p.incluir(a[x])
    while not(p.estavacia()):   
        if p.inspeccionar() != ' ':
            aux.incluir(p.extraer())
        else:
            aux.dar_vuelta() 
            aux.imprimir()
            p.extraer()
            aux.vaciar()
    aux.dar_vuelta() 
    aux.imprimir()
    
revertir("Mi diario Python")

        
        

        

#p=Pila()
#(p.incluir(1))
#(p.incluir(2))
#(p.incluir(3))
#(p.imprimir())
#print (p.items)
#(p.vaciar())
#print (p.imprimir())


