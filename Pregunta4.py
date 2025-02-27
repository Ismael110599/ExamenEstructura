class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class Cola:
    def __init__(self):
        self.frente = None
        self.ultimo = None

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.frente = self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo

    def desencolar(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return None
        valor = self.frente.valor
        if self.frente == self.ultimo:
            self.frente = self.ultimo = None
        else:
            self.frente = self.frente.siguiente
            self.frente.anterior = None
        return valor

    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.frente.valor

    def mostrar_cola(self):
        elementos = []
        actual = self.frente
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos


# Prueba de la cola
cola = Cola()

# Encolando elementos
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)

# Mostrando la cola
print("Estado actual de la cola:", cola.mostrar_cola())

# Desencolando un elemento
print("Elemento desencolado:", cola.desencolar())

# Mostrando el frente de la cola
print("Elemento en el frente de la cola:", cola.ver_frente())

# Mostrando el estado de la cola después de desencolar
print("Estado actual de la cola después de desencolar:", cola.mostrar_cola())
