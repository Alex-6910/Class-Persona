# Class-Persona
Ejercicio class persona con phyton
ejercico1 

class Persona:
    def __init__(self, nom, sou):
        self.__nom = nom
        self.__sou = sou

    def calcular_sou(self):
        return self.__sou 
   
    def saber_nom(self):
        return self.__nom

class Fixe(Persona):
    def calcular_sou(self):
        return super().calcular_sou() * 1.2

class Temporal(Persona):
    def calcular_sou(self):
        return super().calcular__sou()

# Exemple d’ús
empleats = [Fixe("Anna", 2000), Temporal("Marc", 1800)]
for e in empleats:
    print(e.saber_nom(), "-", e.calcular_sou())
