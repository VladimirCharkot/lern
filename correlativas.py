#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:45:47 2019

@author: vlad
""" 

import json

# clase abstracta
class UTN(object):
    basicas =  {'lgb' : {'nombre' : 'Álgebra', 
                         'correlativas' : []},
                'am1' : {'nombre' : 'Análisis matemático I',
                         'correlativas' : []},
                'am2' : {'nombre' : 'Análisis matemático II',
                         'correlativas' : ['am1','lgb']}
                }
                
    especificas_sistemas = {'alg' : {'nombre' : 'Algoritmos',
                                     'correlativas' : []},
                            'sos' : {'nombre' : 'Sistemas operativos',
                                     'correlativas' : ['lgb','alg']},
                            'sim' : {'nombre' : 'Simulación',
                                     'correlativas' : ['sos','am2']}
                            }
                            
    especificas_quimica =  {'qm1' : {'nombre' : 'Química 1',
                                     'correlativas' : []},
                            'qm2' : {'nombre' : 'Química 2',
                                     'correlativas' : ['qm1','lgb','am1']},
                            'org' : {'nombre' : 'Química Orgánica',
                                     'correlativas' : ['qm2','am2']},
                            'sld' : {'nombre' : 'Sólidos',
                                     'correlativas' : ['qm2']}
                            }
 #PRUEBA ROMPETODO 1.0
 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
               
    sistemas = basicas.copy()
    sistemas.update(especificas_sistemas)
    
    quimica = basicas.copy()
    quimica.update(especificas_quimica)
                
    def checkear_consistencia(carrera):
        for m in carrera:
            for c in carrera[m]['correlativas']:
                if c not in carrera:
                    print("Se encontró una correlativa que no pertenence a la carrera. Ups...")
                    return False
        print("Carrera consistente! :D")
        return True
    
UTN.checkear_consistencia(UTN.sistemas)
UTN.checkear_consistencia(UTN.quimica)
                
class Alum(object):    
    
    def __init__(self, nombre, carrera):
        # en este método se definen e inicializan las variables del objeto
        self.nombre = nombre
        self.carrera = carrera
        self.cursadas = {}
        self.anotadas = []
        
    # este método define cómo se muestra el objeto en consola
    # > v = Alum('Vlad')
    # > print(v)
    def __repr__(self):
        if self.recibido():
            return "Ing. {}".format(self.nombre)
        return "Alum. {} ({}/{})".format(self.nombre, len(self.cursadas), len(self.carrera))
        
    def recibido(self):
        # cursó todas las materias de la carrera?
        return self.cursadas.keys() == self.carrera.keys()
        
    def mostrar_cursada(self):
        posibles = self.posibles_anotarse()
        for m in self.carrera:
            status = 'x'
            if m in self.cursadas:
                status = '✓'
            if m in self.anotadas:
                status = '*'
            if m in posibles:
                status = ' '
            print("[{}] - {}".format(status, self.carrera[m]['nombre']))
        
    def analitico(self):
        
        # lista de materias que están en 'carrera' y no están en 'cursadas'
        pendientes = [self.carrera[mat]['nombre'] 
                        for mat in self.carrera 
                        if mat not in self.cursadas]
        
        # lista de diccionarios con nombre y código de materia y nota
        # creada a partir del diccionario self.cursadas
        notas = [{'cod' : m, 
                  'nom' : self.carrera[m]['nombre'], 
                  'nota' : self.cursadas[m]} 
                    for m in self.cursadas]
        
        # suma de todas las notas numéricas dividida la cantidad de materias cursadas
        if self.cursadas:
            promedio = sum([self.cursadas[m] for m in self.cursadas])/len(self.cursadas)
        else:
            promedio = 0

        # objeto dict que se exporta como json con la 
        # función dumps de la librería json
        analitico = {'nombre' : self.nombre,
                     'promedio' : promedio,
                     'detalle' : notas,                     
                     'pendientes' : pendientes}
        return json.dumps(analitico, indent=4)
        
    def posibles_anotarse(self):
        l = []
        # de todas las materias de la carrera...
        for mat in self.carrera.keys():
            # ...me fijo cuales dan las correlativas y no se están cursando ni anotadas
            if self.checkear_correlativas(mat) and not(mat in self.cursadas) and not(mat in self.anotadas):
                l.append(mat)
        return l
    
    def mostrar_posibles_anotarse(self):
        posibles = self.posibles_anotarse()
        # print por nombre de materia
        for p in posibles:
            print("> {}".format(self.carrera[p]['nombre']))
        
    def checkear_correlativas(self, mat):
        if not(mat in self.carrera): return False
        # para cada materia correlativa en self.carrera...
        for corr in self.carrera[mat]['correlativas']:
            # ...chequeo si está cursada
            if not(corr) in self.cursadas:
                return False
        return True
    
    def cursada(self,mat,nota):
        if not(nota > 0 and nota < 10):
            print("Nota imposible boh!")
            return False
        if not(mat in self.anotadas): 
            print("No se puede cursar una materia sin anotarse!")
            return False
        
        if nota >= 4:
            # agrego la materia como clave y la nota como elemento
            # en el diccionario de cursadas
            self.cursadas[mat] = nota
            print('{} aprobada!'.format(self.carrera[mat]['nombre']))
        
        # la remuevo de anotadas
        self.anotadas.remove(mat)
        
    def anotar(self, mat):
        if not(mat in self.carrera): 
            print("Esa materia no existe!")
            return False
        
        # chequeo prerrequisitos
        if self.checkear_correlativas(mat):
            print("Todo en orden! Anotado en {}".format(self.carrera[mat]['nombre']))
            # append agrega un elemento a una lista ('mat' a 'anotadas')
            self.anotadas.append(mat)
            return True
        else:
            print("No dan las correlativas :(")
        
if __name__ == '__main__':
    v = Alum('Vlad', UTN.sistemas)
    v.anotar('lgb')
    v.anotar('am1')
    v.cursada('am1',8)
    v.cursada('lgb',6)
    v.anotar('alg')
    v.anotar('am2')
    v.cursada('alg',9)
    v.cursada('am2',4)
    v.anotar('sos')
    v.cursada('sos',8)
    v.anotar('sim')
    print("\nAnalítico en formato JSON:")
    print(v.analitico())