import unittest
from ex_3_1 import Stack  # Assurez-vous que le fichier contenant Stack est bien nommé "ex_3_2.py"

class TestStack(unittest.TestCase):
    def setUp(self):
        """Initialisation d'une nouvelle stack pour chaque test"""
        self.s = Stack()
    
    def test_push_and_pop(self):
        """Test de l'ajout et suppression d'éléments"""
        self.s.push(1)
        self.s.push(5)
        self.assertEqual(self.s.pop(), 5)
        self.assertEqual(self.s.pop(), 1)
    
    def test_max(self):
        """Test de la fonction max()"""
        self.s.push(3)
        self.s.push(7)
        self.s.push(2)
        self.assertEqual(self.s.max(), 7)
        self.s.pop()
        self.s.pop()
        self.assertEqual(self.s.max(), 3)
    
    def test_min(self):
        """Test de la fonction min()"""
        self.s.push(4)
        self.s.push(1)
        self.s.push(6)
        self.assertEqual(self.s.min(), 1)
        self.s.pop()
        self.s.pop()
        self.assertEqual(self.s.min(), 4)
    
    def test_pop_empty(self):
        """Test pop() sur une stack vide"""
        with self.assertRaises(IndexError):
            self.s.pop()
    
    def test_max_empty(self):
        """Test max() sur une stack vide"""
        with self.assertRaises(ValueError):
            self.s.max()
    
    def test_min_empty(self):
        """Test min() sur une stack vide"""
        with self.assertRaises(ValueError):
            self.s.min()

if __name__ == '__main__':
    unittest.main()