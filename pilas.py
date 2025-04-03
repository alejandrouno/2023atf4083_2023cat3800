class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self) -> None:
        self.tope = None
        self.longitud = 0

    def apilar(self, valor) -> None:
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.longitud += 1

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        valor = self.tope.valor
        self.tope = self.tope.siguiente
        self.longitud -= 1
        return valor

    def esta_vacia(self) -> bool:
        return self.tope is None

    def ver_cima(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.tope.valor

    def obtener_longitud(self) -> int:
        return self.longitud


pila = Pila()

pila.apilar(10)
pila.apilar(20)
pila.apilar(30)

print("Cima de la pila:", pila.ver_cima())  
print("Longitud de la pila:", pila.obtener_longitud())  
print("Elemento desapilado:", pila.desapilar())  
print("Elemento desapilado:", pila.desapilar())  
print("¿La pila está vacía?", pila.esta_vacia())  
print("Longitud de la pila:", pila.obtener_longitud())  
print("Elemento desapilado:", pila.desapilar())  
print("¿La pila está vacía?", pila.esta_vacia())  
print("Longitud de la pila:", pila.obtener_longitud())  
