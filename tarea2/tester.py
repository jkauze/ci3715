# Archivo de prueba unitarias que debera pasar el programa
# Los casos expuestos en este programa son casos maliciosos y bordes en el que el programa pudiera fallar
# AUTORES:

# David Segura #13-11341
# Jesus Kauze #12-10273

import unittest
from pension import *

class testing(unittest.TestCase):

    #Casos de calculo de Edad

    # CASO 1: Fecha supera los 140 anos de edad
    def test1(self):
        self.assertEqual(CalcularEdad(datetime.date(1794,12,13)), False)

    # CASO 2: fecha futura
    def test2(self):
        self.assertEqual(CalcularEdad(datetime.date(3000,12,13)), False)

    # CASO 3: La fecha es correcta
    def test3(self):
        self.assertEqual(CalcularEdad(datetime.date(1994,12,13)), True)

    # CASO 4: Hombre que cumple con la edad y semanas, sin salubridad
    def test4(self):
        self.assertEqual(pensionado("h",60,750,0), True)
    
    # CASO 5: Hombre que no ha cumplido la mayoría de edad y ni la semanas, sin salubridad
    def test5(self):
        self.assertEqual(pensionado("h",59,749,0), False)
    
    # CASO 6: Hombre que cumple con la mayoría de edad y no la semanas, sin salubridad
    def test6(self):
        self.assertEqual(pensionado("h",60,749,0), False)
    
    # CASO 7: Hombre que cumple la mayoría de edad por salubridad y la semanas
    def test7(self):
        self.assertEqual(pensionado("h",55,750,20), True)
    
    # CASO 8: Hombre que cumple la mayoría de edad por salubridad y no las semanas
    def test8(self):
        self.assertEqual(pensionado("h",55,749,20), False)
    
    # CASO 9: Hombre que no cumple la mayoría de edad por salubridad y ni las semanas
    def test9(self):
        self.assertEqual(pensionado("h",55,749,19), False)
    
    # CASO 10: Hombre que no cumple la mayoría de edad por salubridad y si las semanas
    def test10(self):
        self.assertEqual(pensionado("h",55,750,19), False)
    
    # CASO 11: Hombre que cumple con la edad y semanas, con salubridad
    def test11(self):
        self.assertEqual(pensionado("h",60,750,20), True)
    
    # CASO 12: Hombre que no ha cumplido la mayoría de edad y ni la semanas, con salubridad
    def test12(self):
        self.assertEqual(pensionado("h",59,749,19), False)
    
    # CASO 13: Hombre que cumple con la mayoría de edad y no la semanas, con salubridad
    def test13(self):
        self.assertEqual(pensionado("h",60,749,4), False)
    
    # CASO 14: Mujer que cumple con la edad y semanas, sin salubridad
    def test14(self):
        self.assertEqual(pensionado("m",55,750,0), True)
    
    # CASO 15: Mujer que no ha cumplido la mayoría de edad y ni la semanas, sin salubridad
    def test15(self):
        self.assertEqual(pensionado("m",54,749,0), False)
    
    # CASO 16: Mujer que cumple con la mayoría de edad y no la semanas, sin salubridad
    def test16(self):
        self.assertEqual(pensionado("m",55,749,0), False)
    
    # CASO 17: Mujer que cumple la mayoría de edad por salubridad y la semanas
    def test17(self):
        self.assertEqual(pensionado("m",50,750,20), True)
    
    # CASO 18: Mujer que cumple la mayoría de edad por salubridad y no las semanas
    def test18(self):
        self.assertEqual(pensionado("m",50,749,20), False)
    
    # CASO 19: Mujer que no cumple la mayoría de edad por salubridad y ni las semanas
    def test19(self):
        self.assertEqual(pensionado("m",50,749,19), False)
    
    # CASO 20: Mujer que no cumple la mayoría de edad por salubridad y si las semanas
    def test20(self):
        self.assertEqual(pensionado("m",50,750,19), False)
    
    # CASO 21: Mujer que cumple con la edad y semanas, con salubridad
    def test21(self):
        self.assertEqual(pensionado("m",55,750,20), True)
    
    # CASO 22: Mujer que no ha cumplido la mayoría de edad y ni la semanas, con salubridad
    def test22(self):
        self.assertEqual(pensionado("m",54,749,19), False)
    
    # CASO 23: Mujer que cumple con la mayoría de edad y no la semanas, con salubridad
    def test23(self):
        self.assertEqual(pensionado("m",55,749,4), False)
    
    

if __name__ == '__main__':
    unittest.main()