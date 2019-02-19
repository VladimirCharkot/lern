#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:56:13 2019

@author: vlad
"""

import unittest
import correlativas

# testea algunos aspectos de Alum
class TestAlum(unittest.TestCase):
    
    # set up... sin este método habría que volver a instanciar el alumno
    def setUp(self):
        self.alumno = correlativas.Alum('El Vlado',correlativas.sistemas)

    def test_recibido(self):
        # comprueba que recibido sea falso
        self.assertFalse(self.alumno.recibido())
        
    def test_analitico_json(self):
        # comprueba que en el analítico esté el nombre
        self.assertIn('Vlado', self.alumno.analitico())
        
    def test_corr_1(self):
        # comprueba que no permita cursar am2 de una
        self.assertFalse(self.alumno.checkear_correlativas('am2'))

    def test_anotar(self):
        # comprueba que si se aprueba am1 y lgb se habilite am2
        self.alumno.anotar('lgb')
        self.assertEqual(len(self.alumno.anotadas), 1)
        self.alumno.anotar('am1')
        self.assertEqual(len(self.alumno.anotadas), 2)
        self.alumno.cursada('am1',8)
        self.alumno.cursada('lgb',6)
        self.assertEqual(len(self.alumno.anotadas), 0)
        self.assertEqual(len(self.alumno.cursadas), 2)
        self.assertTrue(self.alumno.checkear_correlativas('am2'))
        

if __name__ == '__main__':
    unittest.main()