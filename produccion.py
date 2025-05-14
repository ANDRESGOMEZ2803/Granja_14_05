class Produccion:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self, nombre):
        self.elementos = [e for e in self.elementos if e.nombre != nombre]

    def consultar(self):
        return self.elementos

    def calcular_total(self):
        return sum(e.calcular_produccion() for e in self.elementos)

    def mostrar_todos(self):
        for e in self.elementos:
            print(e)
