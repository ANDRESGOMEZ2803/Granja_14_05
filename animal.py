class Animal:
    def _init_(self, nombre, tipo, produccion):
        self.nombre = nombre
        self.tipo = tipo
        self.produccion = produccion

    def calcular_produccion(self):
        return self.produccion

    def _str_(self):
        return f"Animal: {self.nombre}, Tipo: {self.tipo}, Producción: {self.produccion}"