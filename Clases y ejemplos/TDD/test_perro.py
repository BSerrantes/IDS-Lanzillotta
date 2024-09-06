#Así se define una prueba
import unittest
from perro import Perro

class TestPerro(unittest.TestCase):

    def test_perro_ladra(self): 
        perro = Perro()
        self.assertEqual(perro.ladrar(), "Woof!")


    def test_perro_pide_comida(self):
        perro = Perro()
        self.assertEqual(perro.pedir_comida(),"Quiero comer")
    
    def test_perro_persigue_gatos(self):
        perro = Perro()
        self.assertEqual(perro.perseguir_gato(),"corré wachin!")

    def test_perro_corre(self):
        perro = Perro()
        self.assertEqual(perro.correr(), "run run ctm!")

if __name__ == '__main__':
    unittest.main()