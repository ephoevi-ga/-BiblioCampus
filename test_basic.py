import unittest
from books import ajouter_livre, lister_livres

class TestBooks(unittest.TestCase):
    def test_ajouter_livre(self):
        livre = ajouter_livre("1984", "George Orwell")
        self.assertIn(livre, lister_livres())

if __name__ == "__main__":
    unittest.main()
