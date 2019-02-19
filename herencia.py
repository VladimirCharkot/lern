#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 08:44:16 2019

@author: vlad
"""

class Pato(object):
    
    def __init__(self, nom, edad):
        self.nombre = nom
        self.edad = edad
        
    def hola(self):
        return "Cuak! Imma duck, imma {}".format(self.nombre)
    
    def tendria_dentro_de(self, anios):
        print("Dentro de {} años tendré {} de edad".format(anios, self.edad+anios))
        
    
class PatoTartamudo(Pato):
    
    def hola(self):
        return "Papapapato {}".format(self.nombre[0:2]*3+self.nombre)


class Patx(Pato):
    
    def __init__(self, nombre, edad, sexo):
        self.sexo = sexo
        super().__init__(nombre, edad)
    
    def decir_sexo(self):
        print(self.sexo)


class Rinoceronte(object):
    def __init__(self, col):
        self.color = col
        
    def hola(self):
        return "Los rinos nos identificamos por el color, y yo soy {}".format(self.color)

def saludar(saludador):
    print("- Quién eres?")
    print("-", saludador.hola())
    print()
    

if __name__ == '__main__':
    
    # Instanciamos objetos
    p1 = Pato("Carlos", 11)
    p2 = Pato("José", 26)
    p3 = PatoTartamudo("roberto", 12)
    rino = Rinoceronte("violeta")
    pata = Patx("Mica", 29, "Mujer")
    
    saludar(p1)
    saludar(p2)
    saludar(p3)
    saludar(rino)
    saludar(pata)