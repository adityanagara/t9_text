import unittest
from findWords import findAllWords


class TestFindwordMethod(unittest.TestCase):
    def test_even_length_words(self):
        inputDict = {"isWord": lambda x: len(x) > 0 and len(x) % 2 == 0}
        words = findAllWords("345", inputDict)
        self.assertEqual(len(words), 9)
    
    def test_all_words(self):
        numbers = "345"
        inputDict = {"isWord": lambda x: len(x) == len(numbers)}
        words = findAllWords(numbers, inputDict)
        self.assertEqual(len(words), 27)
    
    def test_large_words(self):
        numbers = "23456789"
        inputDict = {"isWord": lambda x: len(x) > 0 and len(x) % 2 == 0}
        words = findAllWords(numbers, inputDict)
        self.assertEqual(len(words), 12726)



if __name__ == '__main__':
    unittest.main()
