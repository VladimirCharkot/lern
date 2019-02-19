#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:45:47 2019

@author: vlad
""" 

import json

sistemas = {'lgb' : {'nombre' : 'Álgebra', 
                     'correlativas' : []},
            'am1' : {'nombre' : 'Análisis matemático I',
                     'correlativas' : []},
            'am2' : {'nombre' : 'Análisis matemático II',
                     'correlativas' : ['am1','lgb']},
            'alg' : {'nombre' : 'Algoritmos',
                     'correlativas' : []},
            'sos' : {'nombre' : 'Sistemas operativos',
                     'correlativas' : ['lgb','alg']},
            'sim' : {'nombre' : 'Simulación',
                     'correlativas' : ['sos','am2']}
            }

class Alum(object):    
    
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera
        self.cursadas = {}
        self.anotadas = []
        
    # este método define cómo se muestra el objeto en consola
    def __repr__(self):
        if self.recibido():
            return "Ing. {}".format(self.nombre)
        return "Alum. {} ({}/{})".format(self.nombre, len(self.cursadas), len(self.carrera))
        
    def recibido(self):
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
        # están en 'carrera' y no están en 'cursadas'
        pendientes = [mat for mat in self.carrera if mat not in self.cursadas]
        
        promedio = sum([self.cursadas[m] for m in self.cursadas])
        analitico = {'nombre' : self.nombre,
                     'cursadas' : self.cursadas,
                     'promedio' : promedio,
                     'pendientes' : pendientes}
        return json.dumps(analitico)
        
    def posibles_anotarse(self):
        l = []
        for mat in self.carrera.keys():
            if self.checkear_correlativas(mat) and not(mat in self.cursadas) and not(mat in self.anotadas):
                l.append(mat)
        return l
    
    def mostrar_posibles_anotarse(self):
        posibles = self.posibles_anotarse()
        for p in posibles:
            print("> {}".format(self.carrera[p]['nombre']))
        
    def checkear_correlativas(self, mat):
        if not(mat in self.carrera): return False
        for corr in self.carrera[mat]['correlativas']:
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
            self.cursadas[mat] = nota
            print('{} aprobada!'.format(self.carrera[mat]['nombre']))
        
        self.anotadas.remove(mat)
        
    def anotar(self, mat):
        if not(mat in self.carrera): 
            print("Esa materia no existe!")
            return False
        
        if self.checkear_correlativas(mat):
            print("Todo en orden! Anotado en {}".format(self.carrera[mat]['nombre']))
            self.anotadas.append(mat)
            return True
        else:
            print("No dan las correlativas :(")
        
    
v = Alum('Vlad', sistemas)
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