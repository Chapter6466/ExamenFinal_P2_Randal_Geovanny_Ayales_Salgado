# Randal Geovanny Ayales Salgado
# 2024-12-16 Programación 2 - Universidad Politécnica 

# Examen Final 

    # Instrucciones: Este es un examen acumulativo por lo cual puede tener preguntas de cualquiera de los temas vistos en clases, además se debe entregar un archivo .py donde venga las repuestas de las pregunta. Las preguntas que no sean crear código deberán venir en el mismo archivo con el numero de pregunta y la respuesta en un comentario (# 1. Respuesta). El examen debe ser entregado antes de media noche del 16 de diciembre del 2024.

# Parte 3.

import unittest
from parte2 import aplanar, permutaciones, diccionario_anidado

class TestParte2(unittest.TestCase):

    # Test for aplanar function
    def test_aplanar(self):
        # Test with a mix of empty and non-empty lists
        self.assertEqual(aplanar([[1, 2, 3], [], [3], [5, 6]]), [[1, 2, 3], [3], [5, 6]])
        # Test with only empty lists
        self.assertEqual(aplanar([[], [], []]), [])
        # Test with no empty lists
        self.assertEqual(aplanar([[1], [2], [3]]), [[1], [2], [3]])
        # Test with an empty outer list
        self.assertEqual(aplanar([]), [])

    # Test for permutaciones function
    def test_permutaciones(self):
        # Test with a list of 3 elements
        self.assertEqual(
            sorted(permutaciones([1, 2, 3])),
            sorted([
                [1, 2, 3], [1, 3, 2], [2, 1, 3],
                [2, 3, 1], [3, 1, 2], [3, 2, 1]
            ])
        )
        # Test with a single element
        self.assertEqual(permutaciones([1]), [[1]])
        # Test with an empty list
        self.assertEqual(permutaciones([]), [[]])
        # Test with a list of 2 elements
        self.assertEqual(sorted(permutaciones([1, 2])), sorted([[1, 2], [2, 1]]))
        # Test with a list of 4 elements
        self.assertEqual(
            sorted(permutaciones([1, 2, 3, 4])),
            sorted([
                [1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2],
                [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3],
                [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1],
                [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1],
                [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2],
                [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]
            ])
        )

    # Test for diccionario_anidado function
    def test_diccionario_anidado(self):
        # Test with a simple list and dictionary
        self.assertEqual(
            diccionario_anidado([8, 3, 2], {'python': 4, 'is': 5, 'best': 9}),
            {8: {'python': 4}, 3: {'is': 5}, 2: {'best': 9}}
        )
        # Test with mismatched lengths (should raise an IndexError)
        with self.assertRaises(IndexError):
            diccionario_anidado([1, 2], {'a': 1, 'b': 2, 'c': 3})
        # Test with empty inputs
        self.assertEqual(diccionario_anidado([], {}), {})
        # Test with a list of 1 element and a dictionary of 1 element
        self.assertEqual(diccionario_anidado([1], {'a': 1}), {1: {'a': 1}})

if __name__ == "__main__":
    unittest.main()