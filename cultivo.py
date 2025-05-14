class Cultivo:
    def _init_(self, nombre, tipo, area, rendimiento):
        self.nombre = nombre
        self.tipo = tipo
        self.area = area
        self.rendimiento = rendimiento

    def calcular_produccion(self):
        return self.area * self.rendimiento

    def _str_(self):
        return f"Cultivo: {self.nombre}, Tipo: {self.tipo}, Área: {self.area}, Rendimiento: {self.rendimiento}"