import unittest
from algoritm import Algo

career = Algo()
career.read_file('in/career.in')

file_to_write = 'out/career.out'

def write_data(file_to_write, change_data):
    file_to_write = file_to_write.replace('in', 'out')
    with open(file_to_write, 'w') as file:
        file.write(str(change_data))


practice_career = career.max_practice()
write_data(file_to_write, practice_career)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(practice_career, 12)
