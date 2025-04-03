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


