# Archivo de prueba unitarias que debera pasar el programa
# Los casos expuestos en este programa son casos maliciosos y bordes en el que el programa pudiera fallar
# AUTORES:

# David Segura #13-11341
# Jesus Kauze #12-10273

import unittest
from pension.py import *

class testing(unittest.TestCase):

    #Casos de calculo de Edad

    # CASO 1: Fecha supera los 140 anos de edad
    def test1(self):
        self.assertEqual(CalcularEdad(datetime.date(1794,12,13)), False)

    # CASO 2: fecha invalida
    def test2(self):
        self.assertEqual(CalcularEdad(datetime.date(3000,122,13)), False)

    # CASO 3: La fecha es correcta
    def test3(self):
        self.assertEqual(CalcularEdad(datetime.date(1994,12,13)), True)

if __name__ == '__main__':
    unittest.main()