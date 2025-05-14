from cultivo import Cultivo
from animal import Animal
from produccion import Produccion

class Granja:
    def __init__(self):
        self.cultivos = Produccion()
        self.animales = Produccion()

    def agregar_cultivo(self):
        nombre = input("Nombre del cultivo: ")
        tipo = input("Tipo de cultivo: ")
        area = float(input("Área de cultivo: "))
        rendimiento = float(input("Rendimiento por área: "))
        cultivo = Cultivo(nombre, tipo, area, rendimiento)
        self.cultivos.agregar(cultivo)

    def agregar_animal(self):
        nombre = input("Nombre del animal: ")
        tipo = input("Tipo de animal: ")
        produccion = float(input("Producción del animal: "))
        animal = Animal(nombre, tipo, produccion)
        self.animales.agregar(animal)

    def mostrar_reporte(self):
        print("\n-- Cultivos Registrados --")
        self.cultivos.mostrar_todos()
        print(f"Producción total de cultivos: {self.cultivos.calcular_total()}\n")

        print("-- Animales Registrados --")
        self.animales.mostrar_todos()
        print(f"Producción total de ganado: {self.animales.calcular_total()}\n")

        total = self.cultivos.calcular_total() + self.animales.calcular_total()
        print(f"Producción total de la granja: {total}")
