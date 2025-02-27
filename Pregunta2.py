class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolExpresion:
    def __init__(self):
        self.raiz = None

    def construir_desde_postfija(self, expresion):
        pila = []
        for token in expresion:
            if token.isdigit():
                pila.append(Nodo(int(token)))
            else:
                nodo = Nodo(token)
                nodo.derecha = pila.pop()
                nodo.izquierda = pila.pop()
                pila.append(nodo)
        self.raiz = pila.pop()

    def evaluar(self, nodo):
        if isinstance(nodo.valor, int):
            return nodo.valor
        izquierda = self.evaluar(nodo.izquierda)
        derecha = self.evaluar(nodo.derecha)
        if nodo.valor == '+':
            return izquierda + derecha
        elif nodo.valor == '-':
            return izquierda - derecha
        elif nodo.valor == '*':
            return izquierda * derecha
        elif nodo.valor == '/':
            return izquierda / derecha

# Ejemplo de uso
expresion = ['3', '5', '2', '8', '-', '*', '+']  # Representa: 3 + 5 * (2 - 8)
arbol = ArbolExpresion()
arbol.construir_desde_postfija(expresion)
resultado = arbol.evaluar(arbol.raiz)
print("Resultado:", resultado)